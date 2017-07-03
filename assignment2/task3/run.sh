hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.reduces=10 \
 -input /data/assignments/ex2/part2/stackLarge.txt \
 -output /user/$USER/assignment2/task3_temp \
 -mapper mapper.py -file mapper.py \
 -reducer reducer1.py -file reducer1.py

#use the first output as the second input
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.reduces=1 \
 -input /user/$USER/assignment2/task3_temp \
 -output /user/$USER/assignment2/task3 \
 -mapper /bin/cat \
 -reducer reducer2.py -file reducer2.py
