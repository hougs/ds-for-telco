#!/bin/bash

export PYSPARK_DRIVER_PYTHON=ipython
export PYSPARK_DRIVER_PYTHON_OPTS="notebook --NotebookApp.ip='*' --NotebookApp.open_browser=False --NotebookApp.port=8880"

export HADOOP_CONF_DIR=/etc/hive/conf
export HIVE_CP=/opt/cloudera/parcels/CDH/lib/hive/lib/

pyspark --master local[2] --deploy-mode client --driver-memory 4G \
    --driver-class-path $HIVE_CP --packages com.databricks:spark-csv_2.10:1.2.0 \
    --conf spark.executor.extraClassPath=$HIVE_CP --conf spark.yarn.executor.memoryOverhead=1024
