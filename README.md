Das ist ein fantastischer Abschluss! Im Screenshot von **DBeaver** sieht man ganz deutlich die Tabelle `weather_data` mit echten Werten für Temperatur (8,9 und 8,6 Grad), Windgeschwindigkeit und Zeitstempel. Damit ist der Beweis erbracht: Deine ETL-Pipeline funktioniert von der API bis in die Datenbank einwandfrei.

Hier ist die professionelle, deutsche README für dein GitHub-Repository, die genau auf dein fertiges Projekt zugeschnitten ist:

---

# 🌦️ Berlin Weather ETL Pipeline

Dieses Projekt ist eine automatisierte **ETL-Pipeline** (Extract, Transform, Load), die mit **Apache Airflow** und der **Astro CLI** realisiert wurde. Es ruft Echtzeit-Wetterdaten ab, bereitet sie auf und speichert sie in einer PostgreSQL-Datenbank.

## 🚀 Projekt-Übersicht

Die Pipeline führt folgende Schritte vollautomatisch aus:

1. **Extract**: Abruf aktueller Wetterdaten für Berlin über die **Open-Meteo API**.
2. **Transform**: Aufbereitung der Rohdaten (Temperatur, Windgeschwindigkeit, Wettercode) mittels Python.
3. **Load**: Speicherung der sauberen Daten in einer **PostgreSQL** Datenbank.

---

## 🛠️ Technologie-Stack

* **Orchestrierung**: Apache Airflow (Astronomer Runtime)
* **Sprache**: Python 3.x
* **Datenbank**: PostgreSQL (Docker-Container)
* **Monitoring**: DBeaver Lite (für SQL-Abfragen)
* **Infrastruktur**: Docker & Astro CLI

---

## 📂 Projektinhalt

Das Projekt wurde mit der Astronomer CLI generiert und angepasst:

* **`dags/etlweather.py`**: Enthält die DAG-Logik und die Task-Definitionen (`@task`).
* **`requirements.txt`**: Installiert die notwendigen Provider für HTTP und Postgres.
* **`docker-compose.yml`**: Konfiguration der lokalen Infrastruktur (Datenbank & Airflow-Services).

---

## 💻 Lokale Ausführung & Nutzung

1. **Infrastruktur starten**:
```bash
astro dev start

```


Dies startet fünf Docker-Container: Postgres (Metadaten-DB), Scheduler, API-Server (UI), Triggerer und den DAG-Prozessor.
2. **Airflow UI**: Erreichbar unter `http://localhost:8080`.
3. **Daten prüfen**: Die Ergebnisse können direkt in einem SQL-Tool wie **DBeaver** über `localhost:5432/postgres` (User: `postgres` / Pass: `postgres`) mit folgendem Befehl abgefragt werden:
```sql
SELECT * FROM weather_data;

```



---
<img width="1907" height="853" alt="image" src="https://github.com/user-attachments/assets/244cd098-bab1-43e2-8c1d-7c2086117000" />


## 👤 Kontakt & Autor

**Rabie**
GitHub: [github.com/rabie23](https://github.com/rabie23)

---

### Was du jetzt tun kannst:

1. Erstelle die Datei `README.md` in deinem VS Code Ordner.
2. Kopiere diesen Text hinein.
3. Führe die `git`-Befehle von vorhin aus, um alles auf GitHub zu laden.

Soll ich dir noch helfen, einen kleinen "Azure"-Abschnitt hinzuzufügen, falls du planst, die DB später in dein Azure-Konto zu verschieben?
