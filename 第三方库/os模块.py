"""
os 模块
os模块就是对操作系统进行操作，使用该模块必须先导入模块：
"""
import os

# getcwd() 获取当前工作目录(当前工作目录默认都是当前文件所在的文件夹)
result = os.getcwd()
print(result)

# chdir()改变当前工作目录
os.chdir('/home/sy')
result = os.getcwd()
print(result)

# listdir() 获取指定文件夹中所有内容的名称列表
result = os.listdir('/home/sy')
print(result)

# mkdir()  创建文件夹
os.mkdir('girls')
os.mkdir('boys', 0o777)

# makedirs()  递归创建文件夹
os.makedirs('/home/sy/a/b/c/d')

# rmdir() 删除空目录
os.rmdir('girls')

# removedirs 递归删除文件夹  必须都是空目录
os.removedirs('/home/sy/a/b/c/d')

# rename() 文件或文件夹重命名
os.rename('/home/sy/a', '/home/sy/alibaba')
os.rename('02.txt', '002.txt')

# stat() 获取文件或者文件夹的信息
result = os.stat('/home/sy/PycharmProject/Python3/10.27/01.py')
print(result)

# system() 执行系统命令(危险函数),获取隐藏文件
result = os.system('ls -al')
print(result)


"""
环境变量
就是一些命令的集合,操作系统的环境变量就是操作系统在执行系统命令时搜索命令的目录的集合
"""
# getenv() 获取系统的环境变量
result = os.getenv('PATH')
print(result.split(':'))

# putenv() 将一个目录添加到环境变量中(临时增加仅对当前脚本有效)
os.putenv('PATH', '/home/sy/下载')
os.system('syls')

# exit() 退出终端的命令
exit()

"""
os模块中的常用值
"""
# curdir  表示当前文件夹  .表示当前文件夹 ,一般情况下可以省略
print(os.curdir)

# pardir  表示上一层文件夹   ..表示上一层文件夹 ,不可省略!
print(os.pardir)

# 相对路径  从当前目录开始查找
os.mkdir('../../../man')

# 绝对路径  从根目录开始查找
os.mkdir('/home/sy/man1')

# name 获取代表操作系统的名称字符串,posix -> linux或者unix系统  nt -> window系统
print(os.name)

# sep 获取系统路径间隔符号 ,window ->\    linux ->/
print(os.sep)

# extsep 获取文件名称和后缀之间的间隔符号  window & linux -> .
print(os.extsep)

# linesep  获取操作系统的换行符号  window -> \r\n  linux/unix -> \n
print(repr(os.linesep))

"""
os.path子模块中
"""
# abspath()  将相对路径转化为绝对路径
path = './boys'
result = os.path.abspath(path)
print(result)

# dirname()  获取完整路径当中的目录部分
path = '/home/sy/boys'
result = os.path.dirname(path)
print(result)

# basename()获取完整路径当中的主体部分
result = os.path.basename(path)
print(result)

# split() 将一个完整的路径切割成目录部分和主体部分
path = '/home/sy/boys'
result = os.path.split(path)
print(result)

# join() 将2个路径合并成一个
var1 = '/home/sy'
var2 = '000.py'
result = os.path.join(var1, var2)
print(result)

# splitext() 将一个路径切割成文件后缀和其他两个部分,主要用于获取文件的后缀
path = '/home/sy/000.py'
result = os.path.splitext(path)
print(result)

# getsize()  获取文件的大小
path = '/home/sy/000.py'
result = os.path.getsize(path)
print(result)

# isfile() 检测是否是文件
path = '/home/sy/000.py'
result = os.path.isfile(path)
print(result)

# isdir()  检测是否是文件夹
result = os.path.isdir(path)
print(result)

# islink() 检测是否是链接
path = '/initrd.img.old'
result = os.path.islink(path)
print(result)

# getctime() 获取文件的创建时间 get create time
import time
path = '/initrd.img.old'
result = os.path.getctime(path)
print(time.ctime(result))

# getmtime() 获取文件的修改时间 get modify time
path = '/initrd.img.old'
result = os.path.getmtime(path)
print(time.ctime(result))

# getatime() 获取文件的访问时间 get active time
path = '/initrd.img.old'
result = os.path.getatime(path)
print(time.ctime(result))

# exists() 检测某个路径是否真实存在
filepath = '/home/sy/下载/chls'
result = os.path.exists(filepath)
print(result)

# isabs() 检测一个路径是否是绝对路径
path = '/boys'
result = os.path.isabs(path)
print(result)

# samefile() 检测2个路径是否是同一个文件
path1 = '/home/sy/下载/001'
path2 = '../../../下载/001'
result = os.path.samefile(path1, path2)
print(result)


"""
os.environ 用于获取和设置系统环境变量的内置值
"""
# 获取系统环境变量  getenv() 效果
print(os.environ['PATH'])

# 设置系统环境变量 putenv()
os.environ['PATH'] += ':/home/sy/下载'
os.system('chls')
