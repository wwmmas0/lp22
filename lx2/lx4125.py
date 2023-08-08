
try:
    """
    编写一个将字符串转换为float对象并返回该结果的函数。使用异常处理来捕获可能发生的异常。
    """
    a=input("type a nubmer:")
    a=float(a)
    print(a)
except(ValueError):
    print("Invalid input.")
