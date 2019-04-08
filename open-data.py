# 網路連線
# import urllib.request as request
# src="http://www.ntcu.edu.tw/newweb/index.htm"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")
# print(data)
# 擷取json
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=b962a317-eb96-464b-b559-7c6e565d0b3d"
with request.urlopen(src) as response:
    data=json.load(response)
# 列表
clist=data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["D_Title"]+"\n")