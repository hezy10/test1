from greenlet import greenlet
import time

def work1():
    while True:
        print('-------work1--------')
        g2.switch()
        time.sleep(1) # 模拟将来可能会出现的耗时操作


def work2():
    while True:
        print('-------work2--------')

        g1.switch()
        time.sleep(10)


if __name__ == '__main__':
    # 创建协程
    g1 = greenlet(work1)
    g2 = greenlet(work2)


    # 切换到g1中进行运行
    g1.switch()
