# generator

# task1 ============================================================
def test():
    print("step01")
    yield 5
    print("step02")
    yield 10

gen=test()
# print(gen)
# 只要函式中有 yield 就是用來生成的函式，所以呼叫後也不會動

for g in gen:
    print("生成器內的資料：", g)


# task2-even ============================================================
def generateEven(maxNumber):
    number=0
    while number <= maxNumber:
        yield number
        number+=2

evenGenerator=generateEven(100)
for even in evenGenerator:
    print("偶數:", even)