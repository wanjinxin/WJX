import math


# ceil  取大于等于x的最小的整数值，如果x是一个整数，则返回x
math.ceil(5.01)
# copysign  把y的正负号加到x前面，可以使用0
math.copysign(2, -3)
# cos  求x的余弦，x必须是弧度
math.cos(math.pi/4)
# degrees  把x从弧度转换成角度
math.degrees(math.pi/4)
# e  表示一个常量
math.e
# exp  返回math.e,也就是2.71828的x次方
math.exp(2)
# expm1  返回math.e的x(其值为2.71828)次方的值减１
math.expm1(2)
# fabs  返回x的绝对值
math.fabs(-2)
# factorial  取x的阶乘的值
math.factorial(3)
# floor  取小于等于x的最大的整数值，如果x是一个整数，则返回自身
math.floor(4.1)
# fmod  得到x/y的余数，其值是一个浮点数
math.fmod(20, 3)
# frexp  返回一个元组(m,e),其计算方式为：x分别除0.5和1,得到一个值的范围，
# 2**e的值在这个范围内，e取符合要求的最大整数值,然后x/(2**e),得到m的值
# 如果x等于0,则m和e的值都为0,m的绝对值的范围为(0.5,1)之间，不包括0.5和1
math.frexp(10)
# fsum  对迭代器里的每个元素进行求和操作
math.fsum([1, 2, 3])
math.fsum((1, 2, 3))
# gcd  返回x和y的最大公约数
math.gcd(6, 8)
# hypot  得到(x**2+y**2),平方的值
math.hypot(3, 4)
# isfinite  如果x是不是无穷大的数字,则返回True,否则返回False
math.isfinite(10)
# isinf  如果x是正无穷大或负无穷大，则返回True,否则返回False
math.isinf(-0.2)
# isnan  如果x不是数字True,否则返回False
math.isnan(2)
# ldexp  返回x*(2**i)的值
math.ldexp(3, 5)
# log  返回x的自然对数，默认以e为基数，base参数给定时，将x的对数返回给定的base,
# 计算式为：log(x)/log(base)  log(x[, base])
math.log(20)
# log10  返回x的以10为底的对数
math.log10(100)
# log1p  返回x+1的自然对数(基数为e)的值
math.log1p(10)
# log2  返回x的基2对数
math.log2(4)
# modf  返回由x的小数部分和整数部分组成的元组
math.modf(math.pi)
# pi  数字常量，圆周率
math.pi
# pow  返回x的y次方，即x**y
math.pow(2, 3)
# radians  把角度x转换成弧度
math.radians(45)
# sin  求x(x为弧度)的正弦值
math.sin(math.pi/4)
# sqrt  求x的平方根
math.sqrt(100)
# tan  返回x(x为弧度)的正切值
math.tan(math.pi)
# trunc  返回x的整数部分
math.trunc(math.pi)
