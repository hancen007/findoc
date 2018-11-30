age = 18
#大于或等于18
if age >=18:
    print("成年了，可以去网吧了。。。。")

you = input("你去不去")
youwife = input("你老婆去不去")
if you == "去" or youwife =="去":
    print("出发")
if you == "去" and youwife=="去":
    print("出去")

sex = input("请输入你的性别")

if sex =="男":
    print("你是男性")
elif sex == "女":
    print("you are a girl")
else:
    print("你是中间人")
