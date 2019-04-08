# 定義類別
class IO:
    support=["consloe","file"]
    def read(src):
        if src not in IO.support:
            print("not supported")
        else:
            print(src)
# 使用類別
print(IO.support)
IO.read("file")
IO.read("internet")