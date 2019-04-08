# 第一隻程式
# print("hello world")
# //整數除法
# x=7//6
# print(x)
# **平方
# y=2**2
# print(y)
# #list
# l=[12,70,50,80,20]
# length=len(l)
# print(length)
# 集合
# s1={3,4,5}
# s2={4,5,6,7}
# s3=s1&s2 #交集
# print(s3)
# s3=s1|s2 #連集
# print(s3)
# s3=s1-s2 #差集 從s1減去s2
# print(s3)
# s3=s1^s2 #反交集
# print(s3)
# set(字串)
# s=set("hello")
# print(s)
# 字典
# dic={"apple":"蘋果","banana":"香蕉"}
# dic["apple"]="小蘋果"
# print(dic["apple"])
# del dic["apple"] #刪除字典中的鍵值對
# print(dic)
# dic2={a:a*2 for a in [3,4,5]}
# print(dic2)
# if
#x=input("請輸入數字:") #是字串型式
# x=int(x)
# if x>200:
#     print(">200")
# elif x>100:
#     print("100~200")
# else:
#     print("<100")

#迴圈
# n=1
# sum=0
# while n<=10:
#     sum=sum+n
#     print(sum)
#     n+=1
# sum=0
# for x in range(11):
#     sum=sum+x
#     print(sum)

#break continue
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print(n)

# n=0 
# for x in range(4):
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print("last n=",n)

# sum=0
# for n in range(11):
#     sum=sum+n
# else:
#     print(sum)

#定義函式
# def add(n1,n2):
#     result=n1+n2
#     return result

#呼叫函式
# x1=int(input())
# x2=int(input())
# value=add(x1,x2)
# print(value)

#無限參數
# def avg(*ns):
#     sum=0
#     for n in ns:
#         sum=sum+n
#     print(sum/(len(ns)))

# avg(3,4)
# avg(3,4,5)
# avg(3,4,5,6)

#模組
# import model
# result=model.distance(1,1,5,5)
# print(result)
# result=model.slope(1,2,5,6)
# print(result)

import sys
sys.path.append("models") #新增路徑
#print(sys.path)

import model
result=model.distance(1,1,5,5)
print(result)
