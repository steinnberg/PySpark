# LAB 3 — Optimisation et fiabilité du cluster

## 📁 lab3_optimisation_spark/README.md

### 🎯 Objectifs pédagogiques

- Optimiser les performances du pipeline Spark.
- Utiliser les fonctions de cache, broadcast et repartition.
- Comprendre le plan d’exécution et le monitoring.

---

### 📚 Concepts abordés

* Spark UI, plan d’exécution
* Repartition, coalesce
* Broadcast join
* Cache et persist

---

### 🧩 Étapes
- 1️⃣ Charger le pipeline du Lab 2
```python
df_logs = spark.read.parquet("../data/output/logs_hourly/")
```

- 2️⃣ Étudier le plan
```python
df_logs.explain(True)
```

- 3️⃣ Optimiser le partitionnement
```python
df_opt = df_logs.repartition(8)
df_opt.cache()
```

- 4️⃣ Jointure optimisée
```python
from pyspark.sql.functions import broadcast
df_users = spark.read.csv("../data/users.csv", header=True, inferSchema=True)
df_joined = df_opt.join(broadcast(df_users), df_opt.user_id == df_users.id)
```

---

### 🧠 À faire : assaignement

1. Tester plusieurs niveaux de partitionnement (2, 4, 8).

2. Observer les temps d’exécution.

3. Ajouter un checkpoint pour tolérance aux pannes.
---

### ✅ Livrable

* Rapport Markdown : optimisation_notes.md

* Graphiques Spark UI (capture d’écran des stages)