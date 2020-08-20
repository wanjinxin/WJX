import threading
import time

# def hello(name):
#     print("hello %s\n" % name)
#     global timer
#     timer = threading.Timer(2.0, hello, ["Hawk"])
#     timer.start()
#
# if __name__ == "__main__":
#     timer = threading.Timer(2.0, hello, ["Hawk"])
#     timer.start()



reset_time = time.strftime("%H:%M:%S", time.localtime())
print(reset_time)
if reset_time == '13:4:43':
    print('ddd')