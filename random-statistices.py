# 隨機模組
import random
data=random.choice([1,5,6,10,20])
print(data)
data=random.sample([1,5,6,10,20],3)
print(data)
data=[1,5,6,10,20]
random.shuffle(data)
print(data)
data=random.random()
print(data)
data=random.uniform(0,100)
print(data)
data=random.normalvariate(100,10)
print(data)

#統計模組
import statistics as stat
data=stat.mean([1,4,5,8,20,100])
print(data)
data=stat.median([1,4,5,8,20,100])
print(data)
data=stat.stdev([1,4,5,8,9,10])
print(data)