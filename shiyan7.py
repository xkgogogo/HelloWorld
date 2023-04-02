import heapq
import numpy as np

# 上界函数：计算当前结点下的价值上界
def Bound(i):
	global cw,cv,n,w,v,c
	cleft = c-cw		#剩余背包容量
	b= cv				#价值上界
	#以物品单位重量价值递减顺序装填剩余容量
	while i < n and w[i] <= cleft:
		cleft -= w[i]	
		b += v[i]
		i += 1
	#装填剩余容量装满背包
	if i < n:
		b += (v[i]/w[i])*cleft
	return b

# 分支限界算法求解01背包
def MaxKnapsack(n,c,w,v):
	#bestx为最佳物品选取状态，cw为当前背包重量，cv为当前背包价值，x为当前物品选取状态，bestv为最优价值，heap为优先队列堆
    global bestx,cw,cv,x,bestv,heap 
    i=0
    up=Bound(i)	#计算当前结点相应的价值上界
    while(i!=n):
		#检查当前扩展结点的左儿子结点是否为可行结点
        if cw + w[i] <= c :
            if cv + v[i] > bestv:
                bestv = cv + v[i]
                x[i] = 1
                heapq.heappush(heap,[1/up,cw+w[i],cv+v[i],i+1,x])	#将左儿子结点插入到优先队列中
        up = Bound(i+1)
		#检查当前扩展结点的右儿子结点是否为可行结点
        if(up >= bestv):
            heapq.heappush(heap,[1/up,cw,cv,i+1,x])					#将右儿子结点插入到优先队列中
        #从优先级队列中取出下一个扩展结点node
        node = heapq.heappop(heap)
        up = 1/node[0]
        cw = node[1]
        cv = node[2]
        i = node[3]
        x = node[4]
    bestx = x[:]
	
#冒泡排序函数，对物品按价值率排序
def bsort(n,w,v):
	e = [0,0,0,0,0]
	for i in range(n):
		e[i] = v[i]/w[i]
	for i in range(n-1):
		for j in range(n-i-1):
			if e[j] < e[j+1]:
				e[j],e[j+1] = e[j+1],e[j]
				w[j],w[j+1] = w[j+1],w[j]
				v[j],v[j+1] = v[j+1],v[j]
	print(e)

n = int(input('请输入你的物品个数:'))
c = int(input('请输入你的背包所能承受的最大重量:'))
w = np.zeros(n,int)
v = np.zeros(n,int)
for i in range(n):                                      #为初始重量，价值数组赋值
    w[i] = int(input('请输入第%d件物品的重量:'%i))
    v[i] = int(input('请输入第%d件物品的价值:'%i))
# 测试
# n = 5
# c = 10
# w = [2,2,6,5,4]
# v = [6,3,5,4,6]
cw,cv,bestv = 0,0,0                                     #初始化cw，cv，bestv
x =[0 for i in range(n)]                                #初始化物品选取状态数组x
bestx = None
e = bsort(n,w,v)                                            #初始化最优物品选取状态数组
print('各物品的重量为:',w)
print('各物品的价值为:',v)
heap=[]
heapq.heapify
MaxKnapsack(n,c,w,v)
print('最优价值为:',end='')
print(bestv)
print('此时背包里的物品有:',end='')
for i in range(n):
    if bestx[i]:
        print(i,' ',end='')

