#函数式编程
#闭包
#旅行者问题:x在起点处为0,走三步，x=3.再走5步，x=8，再走2步，x=10.即需保存上一步的结果
origin = 0
def traveler(pos):
    def move(step):
        nonlocal pos
        pos_update = step + pos
        pos = pos_update
        return pos_update
    return move

f = traveler(origin)
print(f(5))
print(f(2))
print(f(3))

#除了上面闭包的方法，也可以用全局变量的方法
origin = 0
def tourist():
    def move(step):
        global origin
        origin +=step
        return origin
    return move
f = tourist()
print(f(5))
print(f(2))
print(f(3))
