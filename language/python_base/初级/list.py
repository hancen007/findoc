# 列表的相关操作
#append
import json

adict = {"name":"hancen","sex":"男性"}
print("字典打印" + adict["name"])
print(adict)
json_demo = json.dumps(adict)
print(json_demo)
json_load = json.loads(json_demo)
print(json_load)
json_load['name']


'''
A = ['xiaowang','xiaozhang','xiaoHuan']

print('----添加前的列表A数据----')

for tempName in A:
    print(tempName)

print('----添加元素----')
temp = 'suan'
A.append(temp)

for tempName in A:
    print(tempName)

# extend

a = [1,2]
b = [3,4]

a.append(b)
a.extend(b)

# insert
a = [1,2,3,4]
a.insert(1,3)

#列表的嵌套

schoolNames = [['','广东工业大学'],
                ['北京大学','清华大学']]



#应用
#一个学校，3个办公室，有8个老师分配工位
import random
#定义一个列表保存3个办公室
offices = [[],[],[]]
#定义8位老师的名字

names = ['a','b','c','d','e','f','g','h']
i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)

'''
