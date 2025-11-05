# 🔁 LAB 4 — Streaming en temps réel (capteurs IoT)

## 📁 lab4_streaming_realtime/README.md

### 🎯 Objectifs pédagogiques

- Mettre en place un pipeline Spark Streaming.
- Lire des flux temps réel (socket/Kafka).
- Appliquer des agrégations sur fenêtres temporelles.

---

### 📚 Concepts abordés

- Spark Structured Streaming
- Source Socket/Kafka
- Fenêtrage temporel
- Sink (console, fichier, base)

---

### 🧩 Étapes

- 1️⃣ Créer une session Spark Streaming
```python
spark = SparkSession.builder.appName("Streaming-IoT").getOrCreate()
```
- 2️⃣ Lecture depuis une socket (simulation)

Dans un terminal :
```bash
nc -lk 9999
```

Puis envoie quelques lignes JSON :
```json
{"sensor_id": 1, "temp": 23.4, "timestamp": "2025-10-11T09:00:00"}
```

- 3️⃣ Lecture du flux :

```python
df_stream = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
```

- 4️⃣ Parsing JSON et agrégation
```python
from pyspark.sql.functions import from_json, col, avg, window
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

schema = StructType([
    StructField("sensor_id", StringType()),
    StructField("temp", DoubleType()),
    StructField("timestamp", StringType())
])

df_parsed = df_stream.select(from_json(col("value"), schema).alias("data")).select("data.*")

df_agg = df_parsed.groupBy(
    window(col("timestamp"), "5 minutes"), col("sensor_id")
).agg(avg("temp").alias("avg_temp"))

```
- 5️⃣ Sortie vers console
```python
query = df_agg.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()
```
---

### 🧠 À faire par l’apprenant

- Ajouter une fenêtre de 1 min glissante.
- Sauvegarder les résultats en Parquet (sink = “parquet”).
- Bonus : connecter une source Kafka.

---

### ✅ Livrable

1. Script : streaming_iot.py
2. Fichier : output/streaming_temp.parquet
3. Capture : exemple du flux en console.