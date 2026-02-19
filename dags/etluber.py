from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from pendulum import datetime
import pandas as pd
import os
import json

# Konfiguration (wie in deinem Wetter-Beispiel)
POSTGRES_CONN_ID = 'postgres_default'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1)
}

with DAG(
    dag_id='uber_etl_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:
    
    @task()
    def extract_uber_data():
        # Findet den Ordner, in dem dieses Skript (etluber.py) liegt
        base_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_path, 'uber_data.csv')
        
        df = pd.read_csv(file_path)
        return df.to_json(orient='records')
   
    @task()
    def transform_uber_data(json_data):
        df = pd.read_json(json_data)
        
        # 1. Spalten säubern
        df.columns = [c.strip() for c in df.columns]
        
        # 2. Zeitstempel umwandeln
        pickup_col = 'tpep_pickup_datetime'
        dropoff_col = 'tpep_dropoff_datetime'
        df[pickup_col] = pd.to_datetime(df[pickup_col])
        df[dropoff_col] = pd.to_datetime(df[dropoff_col])
        
        # --- NEU: Datetime Dimension erstellen ---
        datetime_dim = df[[pickup_col, dropoff_col]].reset_index(drop=True)
        datetime_dim['pick_hour'] = datetime_dim[pickup_col].dt.hour
        datetime_dim['pick_day'] = datetime_dim[pickup_col].dt.day
        datetime_dim['pick_month'] = datetime_dim[pickup_col].dt.month
        datetime_dim['pick_year'] = datetime_dim[pickup_col].dt.year
        datetime_dim['pick_weekday'] = datetime_dim[pickup_col].dt.weekday
        datetime_dim['datetime_id'] = datetime_dim.index
        # -----------------------------------------

        # 3. Rate Code Dimension
        rate_col = 'RatecodeID' if 'RatecodeID' in df.columns else df.columns[df.columns.str.contains('Ratecode', case=False)][0]
        rate_code_type = {1:"Standard rate", 2:"JFK", 3:"Newark", 4:"Nassau or Westchester", 5:"Negotiated fare", 6:"Group ride"}
        rate_code_dim = df[[rate_col]].reset_index(drop=True)
        rate_code_dim['rate_code_id'] = rate_code_dim.index
        rate_code_dim['rate_code_name'] = rate_code_dim[rate_col].map(rate_code_type)
        
        # 4. Fact Table
        cols_to_keep = ['VendorID', 'passenger_count', 'trip_distance', 'fare_amount', 'total_amount']
        existing_cols = [c for c in cols_to_keep if c in df.columns]
        fact_table = df[existing_cols]
        fact_table['datetime_id'] = fact_table.index
        
        # GANZ WICHTIG: Alle drei Tabellen hier zurückgeben!
        return {
            "fact_table": fact_table.to_json(orient='records'),
            "datetime_dim": datetime_dim.to_json(orient='records'),
            "rate_code_dim": rate_code_dim.to_json(orient='records')
        }



    @task()
    def load_uber_data(transformed_data):
        """Lädt die Tabellen in Postgres."""
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        engine = pg_hook.get_sqlalchemy_engine()
        
        # Wir laden jede Tabelle einzeln hoch
        # .to_sql ist viel einfacher als manuelle INSERT-Befehle!
        for table_name, data_json in transformed_data.items():
            temp_df = pd.read_json(data_json)
            temp_df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Tabelle {table_name} erfolgreich geladen.")

    # Workflow Definition
    raw_data = extract_uber_data()
    clean_data = transform_uber_data(raw_data)
    load_uber_data(clean_data)