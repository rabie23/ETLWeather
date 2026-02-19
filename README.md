

# 🚀 Multi-Source ETL Portfolio: Weather & Uber Data

Dieses Repository enthält zwei vollautomatisierte **ETL-Pipelines**, die mit **Apache Airflow** und der **Astro CLI** realisiert wurden. Es demonstriert den Umgang mit unterschiedlichen Datenquellen (REST-API und lokale CSV-Dateien) sowie deren Speicherung in einer PostgreSQL-Datenbank.

## 📈 Projekt-Übersicht

Das Repository besteht aus zwei Haupt-Workflows (DAGs):

### 1. 🌦️ Berlin Weather Pipeline (API-to-DB)

* **Quelle**: Echtzeit-Wetterdaten der **Open-Meteo API**.
* **Fokus**: Handling von HTTP-Requests und JSON-Transformationen.
* **Ziel**: Eine flache Tabelle (`weather_data`) mit aktuellen Temperatur- und Windwerten.

### 2. 🚖 Uber Data Pipeline (CSV-to-Star-Schema)

* **Quelle**: Lokale Datensätze (CSV) über Fahrten in New York City.
* **Fokus**: Komplexere Datenmodellierung (Transformation in ein **Sternschema**).
* **Ziel**: Aufteilung der Daten in eine Fakten-Tabelle (`fact_table`) und Dimension-Tabellen (`rate_code_dim`, `datetime_dim`) für optimierte SQL-Analysen.

---

## 🛠️ Technologie-Stack

* **Orchestrierung**: Apache Airflow (Astronomer Runtime)
* **Sprache**: Python (Pandas für Transformationen)
* **Datenbank**: PostgreSQL (Docker-basiert)
* **Monitoring**: DBeaver Lite (für SQL-Validierung)
* **Infrastruktur**: Docker & Astro CLI

---

## 📂 Repository-Struktur

* **`dags/etlweather.py`**: Pipeline für den API-Abruf der Wetterdaten.
* **`dags/etluber.py`**: Pipeline für die Uber-Datenverarbeitung.
* **`dags/uber_data.csv`**: Der zugrunde liegende Datensatz für die Uber-Pipeline.
* **`requirements.txt`**: Enthält notwendige Bibliotheken wie `pandas`, `sqlalchemy` und `psycopg2-binary`.

---

## 💻 Inbetriebnahme

1. **Container starten**:
```bash
astro dev start

```


Dies startet die Airflow-Umgebung inklusive Webserver, Scheduler und der Postgres-Datenbank.
2. **Airflow UI**: Navigiere zu `http://localhost:8080`, um beide DAGs zu starten und zu überwachen.
3. **Datenanalyse (DBeaver)**:
* **Wetter**: `SELECT * FROM weather_data;`
* **Uber**: `SELECT * FROM fact_table f JOIN rate_code_dim r ON f.datetime_id = r.rate_code_id;`



---

### 💡 Gelernte Konzepte

* Lösen von Port-Konflikten in Docker-Umgebungen (z.B. Port 5432).
* Installation zusätzlicher Python-Pakete in laufenden Airflow-Containern über `requirements.txt`.
* Datenmodellierung nach dem Sternschema-Prinzip für Business Intelligence.

---


---
<img width="1907" height="853" alt="image" src="https://github.com/user-attachments/assets/244cd098-bab1-43e2-8c1d-7c2086117000" />

<img width="1506" height="960" alt="image" src="https://github.com/user-attachments/assets/3b792346-f19e-4f4f-b38e-d0d69420e998" />

<img width="1520" height="861" alt="image" src="https://github.com/user-attachments/assets/fcafdf35-0de8-47ed-a395-2b89a6c0b012" />



