#!/usr/bin/env python3


# list 列表中的元素可以是：数字，字符串，列表，布尔值
li = [1,2,3,"age","python",["列表","布尔值"],True,False]
# 索引取值
print(li[4])

# 切片，切片结果也是列表
print(li[2:5])
# for
for item in li:
    print(item)

# while
while True:
    print(li)
    break
# 列表元素可以被修改
l2 = [1,2,3,"age","python",["列表","布尔值"],True,False]
l2[2] = 100
l2[3:5]="lawrence","Python3"
print(l2)
# 删除列表里的元素
del(l2[1])
print(l2)
del(l2[0:2])
print(l2)
# in
v = "python3" in l2
print(v)