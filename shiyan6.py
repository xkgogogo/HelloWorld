import numpy as np

def backtrackbag(i):
    global bestv,cw,cv,x,bestx          #cw为当前背包重量，cv为当前背包价值，bestv为当前最优价值，x为当前选取物品状态，bestx为最优选取物品状态
    if i>=n:                            #搜索到可行解   
        if bestv < cv:
            bestv = cv
            bestx = x[:]
    else:
        if cw+w[i]<=c:                  #走左子树
            x[i] = 1
            cw += w[i]
            cv += v[i]
            backtrackbag(i+1)
            cw -= w[i]
            cv -= v[i]
        x[i] = 0                        #走右子树
        backtrackbag(i+1)




# n = int(input('请输入你的物品个数:'))
# c = int(input('请输入你的背包所能承受的最大重量:'))
# w = np.zeros(n,int)
# v = np.zeros(n,int)
# 测试
n = 5
c = 10
w = [2,2,6,5,4]
v = [6,3,5,4,6]
cw,cv,bestv = 0,0,0                                     #初始化cw，cv，bestv
x =[0 for i in range(n)]                                #初始化物品选取状态数组x
bestx = None                                            #初始化最优物品选取状态数组
# for i in range(n):                                      #为初始重量，价值数组赋值
#     w[i] = int(input('请输入第%d件物品的重量:'%i))
#     v[i] = int(input('请输入第%d件物品的价值:'%i))
print('各物品的重量为:',w)
print('各物品的价值为:',v)
backtrackbag(0)
print('最优价值为:',end='')
print(bestv)
print('此时背包里的物品有:',end='')
for i in range(n):
    if bestx[i]:
        print(i,' ',end='')