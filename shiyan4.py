import numpy as np 
#打印邻接矩阵函数
def printJ(g):
    print('该图的邻接矩阵为：')
    for i in range (n):                         #遍历邻接矩阵数组
        for j in range (n):
            if (j == n-1):
                print('      ',g[i][j])
            else:
                print('      ',g[i][j],end=' ')
#最小成本路径求解函数，使用向后处理法
def FindminPath(g,V,n,p):
    cost = [100 for i in range(n)]              #初始化成本数组，cost[j]相当于顶点j到源点的最小成本
    d = [0 for i in range(n)]                   #初始化连接点数组，d[j]相当于顶点j与下一阶段的最优连接点
    l = [0 for i in range(n)]                   #初始化连接点数组，l[j]相当于顶点j与上一阶段的最优连接点
    cost[0] = 0
    Vnum = len(V)
    for i in range(0,n-1,1):                    #计算cost，d和l数组
        tempmin = 100
        for j in range(len(g[i])):
            if (g[i][j]):
                if (cost[i]+g[i][j]<cost[j]):
                    cost[j] = cost[i]+g[i][j]
                    if (cost[j]<tempmin):
                        tempmin = cost[j]
                        l[j] = i
                        d[i] = j
    p[0] = 0
    for i in range(1,Vnum,1):               #找到一条最小成本路径
        if l[d[p[i-1]]] == p[i-1]:
            print(l[d[p[i-1]]])
            p[i] = d[p[i-1]]
        else:
            print(l[d[p[i-1]]])
            p[i-1] = l[d[p[i-1]]]
            p[i] = d[p[i-1]]
    print('最小成本为：',cost[n-1])

    
    
#路径打印函数
def printP(p):
    print('最小成本路径为：',end=' ')
    for i in range(len(p)):
        if (i == 0):
            print(p[i],end=' ')
        else:
            print('->',end=' ')
            print(p[i],end=' ')



#测试模块
n,m = map(int,input('请输入你要创建的多段图的顶点数n和边数m:').split())
g = np.zeros((m, n),np.int0)                    #生成初始邻接矩阵
temp = [0,0]
for i in range (m):
    temp[0],temp[1],g[temp[0]][temp[1]] = map(int,input('请输入边的起点,终点及其权重：').split())
printJ(g)
Vnum = int(input('请输入多段图的阶段数：'))
V = [[] for i in range(Vnum)]                   #根据输入的值创建阶段集合数组，存储各阶段的顶点名字
p = [0 for i in range(Vnum)]                    #根据输入的值创建路径数组
for i in range (n):                             #确定各顶点所处阶段
    t = int(input('请输入顶点%d所处的阶段:'%i))
    V[t-1].append(i)
print('源点S为: {} ,汇点T为: {}'.format(V[0][0],V[Vnum-1][0]))
for i in range(Vnum):                           #输出各阶段顶点，进行二次确认
    print('处于阶段%d的顶点有:'%(i+1),end=' ')
    print(V[i])
FindminPath(g,V,n,p)
printP(p)
