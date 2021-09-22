import math


def isPrecision(a, b, Precision = 8):
    return math.fabs(a - b) < 10 ** (-Precision)


def Function(x, index):
    result = [math.sin(x * 1.0) - 6 * x - 5, x ** 4 - x ** 3 - 10]
    if x < 0:
        result.append(1.0 / x)
        result.append(x ** 5 + x - 1)
        result.append(None)
    elif x == 0:
        result.append(None)
        result.append(x ** 5 + x - 1)
        result.append(None)
    else:
        result.append(1.0 / x)
        result.append(x ** 5 + x - 1)
        result.append(math.log(x * 1.0) + x ** 2 - 3)
    result.append(math.cos(x * 1.0) - math.sin(x * 1.0))
    return result[index]


def MiddleTheory(a, b):
    if a and b:
        return a * b <= 0
    else:
        return None


def SearchInt(index):
    for i in range(-100, 101):
        if MiddleTheory(Function(i, index), Function(i + 1, index)):
            return i


FunctionArray = ["sinx=6x+5", "x^4=x^3+10", "1/x", "x^5+x=1", "lnx+x^2=3", "cosx=sinx"]

for i in range(len(FunctionArray)):
    print("{}是\t{}".format(i, FunctionArray[i]))
print("请输入需要的函数的序号：")
Index = int(input())
print("请输入精度：")
D = int(input())

left = SearchInt(Index)
# left = 0
res = 0

if left is None:
    print("函数无零点")
else:
    right = left + 1

    print("函数\t <{}> \t的零点在\t <{:.10f}> \t 和\t <{:.10f}> \t之间".format(FunctionArray[Index], left, right))
    while not isPrecision(left, right, D):
        res += 1
        middle = (right - left) / 2
        if MiddleTheory(Function(left + middle, Index), Function(left, Index)):
            right = left + middle
        else:
            left = right - middle
    print("函数\t <{}> \t的零点在\t <{:.10f}> \t 和\t <{:.10f}> \t之间".format(FunctionArray[Index], left, right))
    print(res)
