# callback

# intro ============================================================
def test(arg):
    arg("Hello")

def handle(da):
    print(da)

test(handle)

# intro ============================================================
def add(n1, n2, func):
    func(n1+n2)

def handle1(result):
    print("加法的結果是：", result)

def handle2(result):
    print("Answer is: ", result)

add(3,4, handle1) 
add(3,4, handle2) 