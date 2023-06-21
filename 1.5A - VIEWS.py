# Databricks notebook source
# MAGIC %md
# MAGIC ### 1.5A - VIEWS
# MAGIC
# MAGIC #### There are 3 types : 
# MAGIC ##### 1. view (permanent until drop)
# MAGIC #####           2. temp view (until session drop)
# MAGIC #####           3. global temp view (until cluster drop)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS smartphones
# MAGIC (id INT, name STRING, brand STRING, year INT);
# MAGIC
# MAGIC INSERT INTO smartphones
# MAGIC VALUES (1,'iphone 14', 'Apple', 2022),
# MAGIC (2,'iphone 13', 'Apple', 2021),
# MAGIC (3,'iphone 6', 'Apple', 2014),
# MAGIC (4,'ipad Air', 'Apple', 2013),
# MAGIC (5,'Galaxy S22', 'Samsung', 2022),
# MAGIC (6,'Galaxy Z Fold', 'Samsung', 2022),
# MAGIC (7,'Galaxy S9', 'Samsung', 2022),
# MAGIC (8,'12 Pro', 'Xiomai', 2022),
# MAGIC (9,'Redmia 11T Pro', 'Xiomai', 2022),
# MAGIC (10,'Redmi Note 11', 'Xiomai', 2021);

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLEs

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VIEW  view_apple_phones AS 
# MAGIC SELECT * FROM smartphones WHERE brand = 'Apple';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM view_apple_phones;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TEMP VIEW temp_view_phones_brands
# MAGIC AS SELECT DISTINCT brand FROM smartphones;
# MAGIC
# MAGIC SELECT * FROM temp_view_phones_brands;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE GLOBAL TEMP VIEW global_temp_view_latest_phones
# MAGIC AS SELECT * FROM smartphones WHERE year > 2020 ORDER BY year DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM global_temp.global_temp_view_latest_phones;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN global_temp;

# COMMAND ----------


