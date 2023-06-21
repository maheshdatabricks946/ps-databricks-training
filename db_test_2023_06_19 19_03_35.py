# Databricks notebook source
print("test files")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from samples.tpch.customer limit 10

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history samples.tpch.customer;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Understanding delta tables

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE employees
# MAGIC (id INT, name STRING, salary DOUBLE);

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO employees
# MAGIC VALUES (1, "Adam", 3500.0),
# MAGIC (2, "Sarah", 4020.5),
# MAGIC (3, "John", 2999.3),
# MAGIC (4, "Taroi",4000.3),
# MAGIC (5, "Anna", 2500.0),
# MAGIC (6, "Kishena",6200.3)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  * FROM  employees

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL employees

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees'

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE employees
# MAGIC SET salary = salary + 100
# MAGIC WHERE name LIKE "A%"

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees'

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL employees

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY employees

# COMMAND ----------

# MAGIC %fs ls dbfs:/user/hive/warehouse/employees/_delta_log/

# COMMAND ----------

# MAGIC %fs head 'dbfs:/user/hive/warehouse/employees/_delta_log/00000000000000000002.json'

# COMMAND ----------

# MAGIC %md
# MAGIC ## Advanced Delta Lake Features

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees VERSION AS OF 1

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE  FROM employees

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees

# COMMAND ----------

# MAGIC %sql
# MAGIC RESTORE TABLE employees TO VERSION AS OF 2

# COMMAND ----------

new_dataframe_name = _sqldf

# COMMAND ----------

display(new_dataframe_name)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY employees

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL employees

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE employees 
# MAGIC ZORDER BY (id)

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY employees

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM employees

# COMMAND ----------

# MAGIC %fs ls dbfs:/user/hive/warehouse/employees

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM employees RETAIN 0 HOURS

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.retentionDurationCheck.enabled = false;

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM employees RETAIN 0 HOURS

# COMMAND ----------

# MAGIC %fs ls dbfs:/user/hive/warehouse/employees

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees@v1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM employees@v2

# COMMAND ----------


