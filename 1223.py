import threading
import time

timer = 0
basket = 0
shouytr = 0
lock = threading.Lock()


class eggTart(threading.Thread):
    chus = ''
    jis = 0

    def run(self) -> None:
        global timer
        global basket
        global shouytr
        while timer < 30:
            if basket >= 500:
                lock.acquire()
                print('篮子已经满了')
                lock.release()
                time.sleep(3)
            else:
                self.jis += 1
                basket = basket + 1
                shouytr -= 1.5
                lock.acquire()
                print(self.chus, '一共做了', self.jis, '个', '篮子里剩下', basket, '个', '工资是', round(self.jis * 1.5, 1))
                lock.release()


class guke(threading.Thread):
    guke = ''
    wallet = 3000
    shus = 0

    def run(self) -> None:
        global shouytr
        global timer
        global basket
        while timer < 30:

            if basket > 0 and self.wallet >= 3:
                self.wallet -= 3
                self.shus += 1
                basket -= 1
                shouytr += 3
                lock.acquire()
                print(self.guke, '买了', self.shus, '个', '还剩', self.wallet, '元')
                lock.release()

            elif self.wallet < 3:
                pass

            else:
                lock.acquire()
                print('已经卖完，等待2秒')
                lock.release()
                time.sleep(2)


class Time(threading.Thread):
    def run(self) -> None:
        global shouytr
        global timer
        while timer < 30:
            time.sleep(1)
            timer += 1
            lock.acquire()
            print('还剩', 30 - timer, '秒')
            lock.release()
        print('收入', shouytr)


p1 = eggTart()
p2 = eggTart()
p3 = eggTart()
p4 = guke()
p5 = guke()
p6 = guke()
p7 = guke()
p8 = guke()
p9 = guke()
timer1 = Time()
p1.chus = '厨师1'
p2.chus = '厨师2'
p3.chus = '厨师3'
p4.guke = '顾客1'
p5.guke = '顾客2'
p6.guke = '顾客3'
p7.guke = '顾客4'
p8.guke = '顾客5'
p9.guke = '顾客6'
timer1.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()
