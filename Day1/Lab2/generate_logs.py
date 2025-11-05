import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Nombre de lignes à générer
N = 1_000_000   # 1 million (≈ 150–200 Mo)

# Génération des colonnes
start_time = datetime(2025, 10, 12, 8, 0, 0)
timestamps = [start_time + timedelta(seconds=i) for i in range(N)]
user_ids = np.random.randint(1, 5000, N)
urls = np.random.choice([
    "https://edf.com/home",
    "https://edf.com/dashboard",
    "https://edf.com/login",
    "https://edf.com/settings",
    "https://edf.com/contact",
    "https://edf.com/analytics",
    "https://edf.com/help"
], N)
response_times = np.round(np.random.uniform(0.05, 1.5, N), 3)
status_codes = np.random.choice([200, 200, 200, 403, 404, 500], N, p=[0.7, 0.1, 0.05, 0.05, 0.05, 0.05])
user_agents = np.random.choice(["Chrome", "Firefox", "Edge", "Safari"], N)

# Création du DataFrame
df = pd.DataFrame({
    "timestamp": timestamps,
    "user_id": user_ids,
    "url": urls,
    "response_time": response_times,
    "status_code": status_codes,
    "user_agent": user_agents
})

# Sauvegarde
df.to_csv("data/logs_web.csv", index=False)

print(f"✅ Dataset généré avec succès : {N:,} lignes dans data/logs_web.csv")
