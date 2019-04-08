#儲存檔案
# file=open("data.txt",mode="w",encoding="utf-8")
# file.write("""helloworld
# 123
# abc
# 中文成功""")
# file.close()
# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n3")

#讀取檔案
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()
#     for line in file:
#         sum=sum+int(line)
# print(data)
# print(sum)

#使用json
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典
# print("name:",data["name"])
# print("version:",data["version"])
data["name"]="new name"
with open("config.json",mode="w") as file:
    json.dump(data,file) #複寫json