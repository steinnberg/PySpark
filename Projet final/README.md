# Projet Final – Pipeline Big Data PySpark

## Objectif  
Assembler les 4 briques de votre formation « Big Data avec PySpark » en un **pipeline complet** :  
1. ETL local (Lab 1)  
2. Pipeline batch distribué (Lab 2)  
3. Optimisation / fiabilité (Lab 3)  
4. Streaming en temps réel (Lab 4)  

Le dataset utilisé est le dataset industriel « Industrial Equipment Monitoring » (ou un équivalent), représentant des logs de capteurs d’équipements industriels.  

## Dataset  
- Source : [Industrial Equipment Monitoring Dataset](https://www.kaggle.com/datasets/dnkumars/industrial-equipment-monitoring-dataset) :contentReference[oaicite:6]{index=6}  
- Contenu typique : timestamp, equipment_id, sensor_id, vibration, temperature, pressure, status_code, etc.  
- Exemple de lignes :  
2025-10-11T08:00:00Z,EQ01,S1234,62.4,101.2,OK
2025-10-11T08:00:01Z,EQ01,S1234,62.8,100.8,OK

---

## Parcours pédagogique  
### Lab 1 – ETL local  
- Charger `industrial_monitoring_logs.csv` avec PySpark en mode local.  
- Nettoyer les données (valeurs manquantes, status_code, etc.).  
- Ajouter une colonne `health_category` (ex : « normal », « warning », « critical ») selon les capteurs/vibrations.  
- Agréger par équipement et catégorie de santé, sauvegarder en Parquet.

### Lab 2 – Pipeline batch distribué  
- Lire le même dataset mais en partitionnant/logs volumineux.  
- Extraire des métriques par heure et par équipement.  
- Joindre avec un fichier enrichissement éventuel (ex : equipment_metadata.csv).  
- Sauvegarder partitionné (par date ou équipement) en Parquet.

### Lab 3 – Optimisation & fiabilité  
- Analyser le plan d’exécution (`.explain()`, Spark UI).  
- Ajuster `repartition`, utiliser `broadcast join`, `cache`, etc.  
- Mettre en place un checkpoint ou gestion fail-safe.  
- Documenter avant/après performances.

### Lab 4 – Streaming en temps réel  
- Simuler un flux capteurs (socket ou Kafka) avec les données.  
- Lire en streaming avec PySpark Structured Streaming.  
- Appliquer une fenêtre temporelle (ex : 5 min glissantes) pour calculer la moyenne de vibration/température par équipement.  
- Écrire les résultats en temps réel vers Parquet ou console.  
- Bonus : détecter et alerter « critical » health_category.

## Livrables attendus  
- Scripts Python/notebooks pour chaque lab (`etl_local.py`, `pipeline_batch.py`, `optimize.py`, `streaming_iot.py`).  
- Dossier `output/` avec fichiers Parquet générés.  
- Documentation et captures d’écran des performances (Lab 3).  
- README.md pour chaque lab (déjà préparés).  

## Conseils pratiques  
- Commencez avec un sous-échantillon du dataset (ex. 1 M lignes) puis montez à 5-10 M pour ressentir l’effet Big Data.  
- Utilisez l’option `spark.sql.shuffle.partitions` pour tester l’impact.  
- Pour le streaming, assurez-vous d’utiliser une fenêtre raisonnable (ex. 1–5 minutes) afin que les résultats soient observables pendant l’exercice.

## Conclusion  
À la fin de ces 4 labs, vous disposerez d’un **pipeline de données distribué complet**, passant du batch au streaming, avec optimisation et architecture fonctionnelle, prêt à être déployé ou prolongé (ex : vers l’IoT, le ML, la maintenance prédictive).  

Bon courage et amusez-vous bien ! 🎓  
