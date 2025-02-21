# intro ===========================================================================

def my_decorator(cb):
    def run():
        print("裝飾器中的程式碼")
        cb("Jack")  # 執行原本的函式
    return run

@my_decorator
def test(n):
    print("Hello, World!", n)
    
test()

# without decorate
def test_without_Decorate(n):
    print("Hello, World!", n)
    
test_without_Decorate("jay")

# 1+2+...+50 ===========================================================================
def calculate(callback):
    def run():
        result=0
        for r in range(51):
            result += r
        # print(result)
        callback(result)
    return run

@calculate
def showZh(n):
    print("普通函式的程式碼", n)

# 重複利用算數邏輯
@calculate
def showEn(n):
    print("Result is", n)

showZh()
showEn()