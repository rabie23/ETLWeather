import pandas as pd


# 1. Eine Series erstellen (wie eine Liste mit Namen)
temperaturen = pd.Series([8.9, 10.2, 7.5, 9.1], name="Grad_Celsius")

# 2. Ein DataFrame erstellen (wie deine Wetter-Tabelle)
data = {
    'Stadt': ['Berlin', 'Berlin', 'Berlin', 'Berlin'],
    'Temperatur': [8.9, 10.2, 7.5, 9.1],
    'Wind': [16, 12, 18, 14]
}

df = pd.DataFrame(data)

# 3. Die Daten "explorieren" (Der erste Blick des Profis)
print("--- Die ersten Zeilen ---")
print(df.head(2))  # Zeigt nur die ersten 2 Zeilen

print("\n--- Statistik-Check ---")
print(df.describe()) # Berechnet sofort Durchschnitt, Min, Max etc.

# Und für deine Hausaufgabe von vorhin:
print("\n--- Max Temperatur ---")
print(temperaturen.max())