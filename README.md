# BigDataHomeWork


#1 HW

```bash
hadoop jar hadoop-streaming.jar \
-input star2002-sample.csv \ 
-output output0\ 
-file mapper0.py\ 
-file reducer0.py\ 
-mapper "python mapper0.py"\ 
-reducer "python reducer0.py"
```
```bash
hadoop jar hadoop-streaming.jar \
-input star2002-sample.csv \ 
-output output1\ 
-file mapper1.py\ 
-file reducer1.py\ 
-file output0\
-mapper "python mapper1.py"\ 
-reducer "python reducer1.py"
```
