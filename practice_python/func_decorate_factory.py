# decorate ===========================================================================
# 無法傳遞參數進到 decorate
def myDec(cb):
    def run():
        print("裝飾器內的程式")
        cb()
    return run

@myDec
def test():
    print("普通函式的程式")

test()

# decorate factory ===========================================================================
# 可以傳遞參數進到 decorate
def myFactory(base):
    def myDec(cb):
        def run():
            print("Factory 裝飾器內的程式", base)
            result=base*2
            cb(result)
        return run
    return myDec

@myFactory(3)
def test(result):
    print("Factory 普通函式的程式", result)

test()

# decorate factory ===========================================================================
def myFact1(max):
    def myDec(cb):
        def run():
            total = 0
            for r in range(max+1):
                total += r
            print("結果是：", total)
            cb(total)
        return run
    return myDec

@myFact1(50)
def showZh(total):
    print("總共是", total)

@myFact1(50)
def showEn(total):
    print("Total is: ", total)

showZh()
showEn()