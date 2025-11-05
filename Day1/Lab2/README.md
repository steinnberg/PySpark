## LAB 2 — Pipeline batch distribué (logs web)

### 📁 lab2_pipeline_batch/README.md

### 🎯 Objectifs pédagogiques

* Créer un pipeline de traitement distribué sur plusieurs fichiers.
* Explorer le partitionnement et le parallélisme.
* Générer des agrégations temporelles.

---

### 📚 Concepts abordés

1. Lecture de données volumineuses (CSV, JSON, HDFS)
2. Pipeline ETL batch
3. Opérations groupées et jointures
4. Sauvegarde en Parquet partitionné

---

### 🧩 Étapes
-1️⃣ Charger les logs web
```python
df_logs = spark.read.option("header", True).csv("../data/logs_web.csv")
```

- 2️⃣ Extraire les champs utiles
```python
from pyspark.sql.functions import split, col
df_logs = df_logs.withColumn("url_path", split(col("url"), "/").getItem(1))
```

- 3️⃣ Agrégation par heure
```python
from pyspark.sql.functions import hour, count
df_stats = df_logs.groupBy(hour(col("timestamp")).alias("hour")).agg(count("*").alias("visits"))
```

- 4️⃣ Sauvegarder
```python
df_stats.write.mode("overwrite").parquet("../data/output/logs_hourly/")
```

---

### 🧠 À faire : Assiignements

- Ajouter une agrégation par navigateur (user_agent).
- Sauvegarder un top 10 des pages les plus vues.
- Documenter les performances (df.count(), df.rdd.getNumPartitions()).

---

### ✅ Livrable

* Script : pipeline_logs.py
* Dossier : output/logs_hourly/