
# coding: utf-8

"""
Data from: https://www.sgi.com/tech/mlc/db/churn.all

Fields:

state: discrete.
account length: continuous.
area code: continuous.
phone number: discrete.
international plan: discrete.
voice mail plan: discrete.
number vmail messages: continuous.
total day minutes: continuous.
total day calls: continuous.
total day charge: continuous.
total eve minutes: continuous.
total eve calls: continuous.
total eve charge: continuous.
total night minutes: continuous.
total night calls: continuous.
total night charge: continuous.
total intl minutes: continuous.
total intl calls: continuous.
total intl charge: continuous.
number customer service calls: continuous.
"""

from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark import SparkContext


sc = SparkContext()
sqlContext = SQLContext(sc)
schema = StructType([StructField("state", StringType(), True),
                     StructField("account_length", DoubleType(), True),
                     StructField("area_code", StringType(), True),
                     StructField("phone_number", StringType(), True),
                     StructField("international_plan", StringType(), True),
                     StructField("voice_mail_plan", StringType(), True),
                     StructField("number_vmail_messages", DoubleType(), True),
                     StructField("total_day_minutes", DoubleType(), True),
                     StructField("total_day_calls", DoubleType(), True),
                     StructField("total_day_charge", DoubleType(), True),
                     StructField("total_eve_minutes", DoubleType(), True),
                     StructField("total_eve_calls", DoubleType(), True),
                     StructField("total_eve_charge", DoubleType(), True),
                     StructField("total_night_minutes", DoubleType(), True),
                     StructField("total_night_calls", DoubleType(), True),
                     StructField("total_night_charge", DoubleType(), True),
                     StructField("total_intl_minutes", DoubleType(), True),
                     StructField("total_intl_calls", DoubleType(), True),
                     StructField("total_intl_charge", DoubleType(), True),
                     StructField("number_customer_service_calls", DoubleType(), True),
                     StructField("churned", StringType(), True)])

df = sqlContext.read.format('com.databricks.spark.csv').load('churn.all', schema = schema)
df.take(5)

# Assemble feature vectors


from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
    inputCols = [
        'number_customer_service_calls', \
        'total_night_minutes', \
        'total_day_minutes', \
        'total_eve_minutes', \
        'account_length'],
    outputCol = 'features')

# Transform labels
from pyspark.ml.feature import StringIndexer

label_indexer = StringIndexer(inputCol = 'churned', outputCol = 'label')
# Fit the model
from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier

classifier = RandomForestClassifier(labelCol = 'label', featuresCol = 'features')

pipeline = Pipeline(stages=[assembler, label_indexer, classifier])

(train, test) = df.randomSplit([0.7, 0.3])
model = pipeline.fit(train)


from pyspark.ml.evaluation import BinaryClassificationEvaluator

predictions = model.transform(train)
evaluator = BinaryClassificationEvaluator()
evaluator.evaluate(predictions)

