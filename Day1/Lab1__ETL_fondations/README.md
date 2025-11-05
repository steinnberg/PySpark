## 🧱 LAB 1 — Fondations du traitement distribué (PySpark ETL local)

### 📁 lab1_etl_fondations/README.md

---

### 🎯 Objectifs pédagogiques

* Comprendre le fonctionnement de Spark et PySpark.
* Manipuler des DataFrames distribués.
* Réaliser un premier pipeline ETL local.

---

### 📚 Concepts abordés

- **SparkSession** , **SparkContext**
- DataFrame, transformations (select, filter, groupBy, agg)
- Lazy evaluation et plan logique
- Sauvegarde de données (CSV, Parquet)

---

### 🧩 Étapes
- 1️⃣ Initialiser PySpark

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ETL-local").getOrCreate()
```

- 2️⃣ Charger un dataset local
* Ex. : data/users.csv

```python
df = spark.read.csv("../data/users.csv", header=True, inferSchema=True)
df.show(5)
```

- 3️⃣ Nettoyer les données
```python
df_clean = df.filter(df.age.isNotNull()).filter(df.country != "Unknown")
```

- 4️⃣ Transformer et agréger
```python
df_country = df_clean.groupBy("country").agg({"age": "avg", "salary": "avg"})
df_country.show()
```

- 4️⃣ Bis Transformation secondaire
```python
from pyspark.sql.functions import when, col
df = df.withColumn("age_category",
      when(col("age") < 30, "jeune")
      .when(col("age") < 45, "adulte")
      .otherwise("senior"))
```

- 4️⃣ ter Grouper par country et age_category :
```python
df.groupBy("country", "age_category").agg({"salary": "avg"}).show()
```


- 5️⃣ Sauvegarder en Parquet
```python
df_country.write.mode("overwrite").parquet("../data/output/country_stats.parquet")
```

---

### 🧠 À faire : Assignements

1. Ajouter une colonne “age_category” (jeune/adulte/senior).
2. Calculer le revenu moyen par catégorie et pays.
3. Visualiser le résultat sous Pandas.

---

### ✅ Livrable (mettre dans Repo Github)

* Script : etl_local.py
* Fichier : output/country_stats.parquet