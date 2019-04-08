#抓取
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#解析
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title") #找class_title的標籤
for title in titles:
    print(title.a.string)

