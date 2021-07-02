# DATABRICKS NOTEBOOK
# @author: Murilo Gustineli

"""
Content written in this file was based on the 
"Apache Spark Programming with Databricks" course on Databricks learning
under the Data Scientists (Customes) pathway
"""


##############################################################################
# DATABRICKS PLATFORM
##############################################################################
# Databricks Notebook Utilities
# Magic commands: 
# https://docs.databricks.com/notebooks/notebooks-use.html#language-magic
%python, %scala, %sql, %r, %sh, %md

# DBUtils: 
# https://docs.databricks.com/dev-tools/databricks-utils.html
dbutils.fs (%fs), dbutils.notebooks (%run), dbutils.widgets

# Visualization: 
# https://docs.databricks.com/notebooks/visualizations/index.html 
display, displayHTML

# Run language specified by language magic command:
%python
print("Run python")

%scala
println("Run scala")

%sql
select "Run SQL"

%r
print("Run R", quote=FALSE)

# Render cell as Markdown using the magic command: %md
%md 
# Heading 1
### Heading 3
> block quote

1. **bold**
2. *italicized*
3. ~~strikethrough~~
---
- [link](https://www.markdownguide.org/cheat-sheet/)
- `code`

# Access DBFS (Databricks File System)
# Run the file system commands on DBFS using magic command: %fs
# %fs is shorthand for the DBUtils module: dbutils.fs
%fs ls

%fs ls /databricks-datasets

%fs head /databricks-datasets/README.md

dbutils.fs.ls("/")
dbutils.fs.ls("/databricks-datasets")

# Visualize results in a table using the Databricks display function
files = dbutils.fs.ls("/databricks-datasets")
display(files)

# Create table
# Run Databricks SQL Commands to create a table named `events` 
# using BedBricks event file on DBFS
%sql
CREATE TABLE IF NOT EXISTS events USING parquet (path "/mnt/training/ecommerce/events/events.parquet");

# See database name
print(databaseName)

# Use SQL to query `events` table
%sql
SELECT * FROM events;

%sql
SELECT traffic_source, SUM(ecommerce.purchase_revenue_in_usd) AS total_revenue
FROM events
GROUP BY traffic_source;

