# Point 實體物件設計
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5

# p=Point(3,4)
# p.show() #呼叫實體方法
# result=p.distance(0,0)
# print(result)


# class Fullname:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
# name1=Fullname("c.w","peng")
# print(name1.first,name1.last)

# file 包裝檔案讀取的程式
class File:
    def __init__(self,name):
        self.name=name
        self.file=None #初始未開啟檔案
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)