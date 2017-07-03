hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.map.output.key.field.separator=" " \
 -D stream.map.output.field.separator=" " \
 -D stream.num.map.output.key.fields=2 \
 -D num.key.fields.for.partition=1 \
 -D mapreduce.job.reduces=10 \
 -input /data/assignments/ex2/part2/stackLarge.txt \
 -output /user/$USER/assignment2/task4_temp \
 -mapper mapper.py -file mapper.py \
 -reducer reducer1.py -file reducer1.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

#use the first output as the second input
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.reduces=1 \
 -input /user/$USER/assignment2/task4_temp \
 -output /user/$USER/assignment2/task4 \
 -mapper /bin/cat \
 -reducer reducer2.py -file reducer2.py
