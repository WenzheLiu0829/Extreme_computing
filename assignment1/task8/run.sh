hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapreduce.partition.keycomparator.options="-k1,1nr"  -D mapred.map.task=10 -D mapred.reduce.tasks=1 -input /user/$USER/data/uniLarge -output /user/$USER/assignment1/task8/output.out -mapper task8_mapper.py -file task8_mapper.py -reducer task8_reducer.py -file task8_reducer.py 
