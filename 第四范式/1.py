# 实现一个装饰器，要求传入两个参数，第一个是时间单位，第二个是线程数
# 时间单位参数支持's','ms'
# 线程数传入整数
# 要求:被修饰的函数按照装饰器中指定的线程数启动线程，同时打印函数名与执行时间
from threading import Thread
import time
def time_thread_wapper(time_unit,thread_num,*args,**kwargs):
    def wrapper(fn):
        def __wrapper():
            thread_pool = []
            exec_time_pool =  [[] for i in range(thread_num)]
            alive_count = [1 for i in range(thread_num)]
            for i in range(thread_num):
                thread_pool.append(Thread(name="Thread-"+str(i),target=fn))
                exec_time_pool[i].append(time.time())
                thread_pool[i].start()
            while True:
                for i in range(thread_num):
                    if not thread_pool[i].is_alive():
                        exec_time_pool[i].append(time.time())
                        if alive_count[i] == 1:
                            if time_unit == 's':
                                print(thread_pool[i].name + "执行完毕,执行的函数是"+str(fn.__name__)+",执行时间为" + str(
                                    exec_time_pool[i][1] - exec_time_pool[i][0]) + "s")
                            else:
                                print(thread_pool[i].name + "执行完毕,执行的函数是"+str(fn.__name__)+",执行时间为" + str(
                                    (exec_time_pool[i][1] - exec_time_pool[i][0])*1000) + "ms")
                        alive_count[i] = 0
                if sum(alive_count) == 0:
                    break
        return __wrapper
    return wrapper

@time_thread_wapper(time_unit='ms',thread_num=3)
def my_test1_function():
    time.sleep(5)

@time_thread_wapper(time_unit='s',thread_num=4)
def my_test2_function():
    time.sleep(3)

my_test1_function()
my_test2_function()