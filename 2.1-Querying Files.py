# Databricks notebook source
# MAGIC %md
# MAGIC ### 2.1-Querying Files

# COMMAND ----------

# MAGIC %run ../Includes/Copy-Datasets

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/databricks-datasets/tpch/delta-001/customer'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM parquet.`dbfs:/databricks-datasets/tpch/delta-001/customer/part-00000-42170dab-f850-4f82-990d-142ffeacc45a.c000.snappy.parquet`

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/databricks-datasets/flights/'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM text.`dbfs:/databricks-datasets/flights/airport-codes-na.txt`

# COMMAND ----------

# MAGIC %sql
# MAGIC REFRESH TABLE employees

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM employees;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE airport_codes_na AS 
# MAGIC SELECT * FROM text.`dbfs:/databricks-datasets/flights/airport-codes-na.txt`;
# MAGIC
# MAGIC DESCRIBE EXTENDED airport_codes_na;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM airport_codes_na LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE departure_delays AS 
# MAGIC SELECT * FROM csv.`dbfs:/databricks-datasets/flights/departuredelays.csv`;
# MAGIC
# MAGIC DESCRIBE EXTENDED departure_delays;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM departure_delays LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TEMP VIEW departure_delays_view 
# MAGIC (date INT, delay INT, distance INT, origin STRING, destination STRING)
# MAGIC USING CSV
# MAGIC OPTIONS (
# MAGIC   path = "dbfs:/databricks-datasets/flights/departuredelays.csv",
# MAGIC   header = "true",
# MAGIC   delimiter=","
# MAGIC );
# MAGIC
# MAGIC CREATE TABLE departure_delays_dlt AS 
# MAGIC SELECT * FROM departure_delays_view;
# MAGIC
# MAGIC SELECT * FROM  departure_delays_dlt LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC --DROP TABLE departure_delays_view;
# MAGIC --DROP TABLE departure_delays_dlt;
# MAGIC DESCRIBE EXTENDED departure_delays_view;

# COMMAND ----------


