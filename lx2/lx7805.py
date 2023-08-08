qs=[153,1,2,3,4,5,6,7,8,9]

while True:
    print("输入q退出")
    a=input("请猜一个数字，看看是否在盒子里：")
    if a=="q":
        print("猜数字结束")
        break
    a=int(a)
    if a in qs:
        a=str(a)
        print(a+"在盒子里")
    else:
        print("不在盒子里")

