import random
def save():
    str = ''
    for i in range(10):
        for j in range(12):
            if j < 4:
                m = random.randint(97,123)
                str += chr(m)
            if j >= 4:
                n = random.randint(0, 9)
                str += '{}'.format(n)
        str += '\n'
    print(str)
n = random.randint(100,999)
m = int(input('输入一个三位数：'))
if m > n:
    ge = m%10
    shi = m//10%10
    bai = m//100
    print('这个三位数:个位是 {0},十位是{1},百位是{2}'.format(ge,shi,bai))
if m ==n:
    print('你中奖了')
if m < n:
    save()