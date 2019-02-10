#输入一个三位数与随机的三位数进行比较
import random
#定义一个函数，用于随机输入字母和数字
def line():
    str_num = ''
    for i in range(4):
        Ac = random.randrange(97,123)
        alh = chr(Ac)
        str_num += alh
    for i in range(8):
        num = random.randrange(0,10)
        num = str(num)
        str_num += num
    return str_num

def num1_gamble(count,total):
    while 1:
        num_in = input('请输入一个三位数：')
        num_random = random.randrange(100,1000)
        total +=1
        print(total)
        if num_in == '-1':
            break
        if num_in.isdigit() == True and 99<int(num_in)<1000:
            num_int = int(num_in)
            if num_int > num_random:
                ge = num_int%10
                shi = num_int%100//10
                bai = num_int//100
                print('输入的三位数的个位是{0}十位是{1}百位是{2},大于随机数{3}'.format(ge,shi,bai,num_random))
            elif num_int == num_random:
                count += 100
                print('你中奖了，获得了%d分' % count)
            else:
                for i in range(10):
                    str_line = line()
                    with open('str_num.txt','a') as f:
                        f.write(str_line+'\n')

        else:
            print('请按要求进行输入' )

if __name__=='__main__':
    total = 0
    count = 0
    num1_gamble(count,total)
