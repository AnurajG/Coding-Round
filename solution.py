from pyspark.sql import SparkSession,SQLContext,Row
from pyspark.sql.types import *
import os
cwd=os.path.abspath(os.getcwd())

# Creating spark context
spark = SparkSession.builder.appName("SparkSql example").getOrCreate()

# Reading both the CSV file using spark read
df_current = spark.read.load(cwd+"data/current.csv", format="csv")
df_voltage = spark.read.load(cwd+"daa/voltage.csv", format="csv")

# Creating temp view from the dataframe for current
df_current.createOrReplaceTempView("current")

# Creating temp view from the dataframe for voltage
df_voltage.createOrReplaceTempView("voltage")

#Logic-1 for power consumed
result=spark.sql('select v._c0 as time,v._c1 as voltage,c._c1 as current,(v._c1*c._c1) as power from current c inner join voltage v on c._c0 = v._c0')

# Creating view from the result set
result.createOrReplaceTempView("result1")

# For above we need to group the time interval for every 0.1 seconds
# Logic-2 calculate the MAX Power every 1/10th of second (0.1) from the above output.
result2 = spark.sql('select  time,max(power) from result1 group by time having sum(time)>=1/10')
# OR
result3 = spark.sql('select agg_time as time ,max(power) as power from (select case when time=0 then "0.0"" else substring(cast(time as varchar),0,3)) end as agg_time,power)a group by agg_time')

print(result2.collect())
