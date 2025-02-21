# 定義類別、類別屬性 ===========================================================================
class IO:
    supportedSrcs=['console', 'file']
    def read(src):
        if src not in IO.supportedSrcs:
            print('Not Supported')
        else:
            print('Read from', src)

# # 使用類別 （類別名稱.屬性名稱）
# print(IO.supportedSrcs)
# # 使用類別屬性
# IO.read('internet')

# 定義實體物件 ================================================================================
class Point:
    def __init__(self, x, y): #實體屬性
        self.x = x
        self.y = y
    def show(self): #實體方法
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5

p1=Point(3,4)
# 建立實體物件，使用實體屬性
print(p1.x, p1.y) # → 3, 4
p1.show() # 呼叫實體方法 → 3, 4
result = p1.distance(0,0)
print(result) # → 5

class File:
    def __init__(self,name):
        self.name= name
        self.file= None #尚未開啟檔案，初期是 None
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
# 讀取第一個檔案
f1=File("data.txt")
f1.open()
data=f1.read()
print(data)

# 讀取第二個檔案
f2=File("data.txt")
f2.open()
data=f2.read()
print(data)