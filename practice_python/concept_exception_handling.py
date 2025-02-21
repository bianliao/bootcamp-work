# try...except... ===========================================================================

data = input("請輸入數字:") #使用者如果輸入 abc
try:
    number=int(data)
except Exception:
    number= 0
number=number*2
print(number)

# try...except... advanced ===========================================================================
# 直到輸入成功才會下一步
while True:
    data1 = input("請輸入數字:") 
    try:
        number = int(data)
        break  
    except Exception:
        print("格式輸入錯誤，‘請重新輸入：")
number=number*2
print(number)