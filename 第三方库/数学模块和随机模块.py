import random


# round  四舍五入操作
round(3.5)
# abs  对一个数值获取其绝对值操作
abs(-3)
# sum  将一个序列的数值进行相加求和
sum((1, 2, 3))
sum([1, 2, 3])


# random()  获取0～1之间的随机小数包含0不包含1
random.random()
# choice()  随机获取列表中的值
random.choice((1, 2, 3))
random.choice([1, 2, 3])
# shuffle  随机打乱序列
list_1 = [1, 2, 3]
random.shuffle(list_1)
print(list_1)
# randrange  获取指定范围内指定间隔的随机整数数
random.randrange(1, 11, 2)
random.randrange(1, 11, 2)
# uniform  随机获取指定范围内的所有数值包括小数
random.uniform(1, 11)
