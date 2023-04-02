import numpy as np
import copy
#Prim算法
def Prim(g):
    S = [0]                             #实时顶点集，用于辅助建立最小生成树
    tempmin = [0,0]                     #中间变量初始化
    f = 0                               #中间变量初始化
    mintree = []                        #初始化最小生成树
    while(len(S)!=n):                   #如果顶点集未选满，则继续遍历剩下的边
        min = 999                       #初始化最小值
        m = 0
        for i in range (n):             
            if (g[f][i] !=0 and g[f][i] <min):
                if(i in S):
                    continue
                else:
                    min = g[f][i]
                    tempmin[0],tempmin[1] = f,i
                    m = 1
        if m == 0:                      #如果上一次循环取到的点的边所连接到的点都是已经在S中的点，则遍历之前的点的边
            for j in S:
                for i in range (n):
                    if (g[j][i] !=0 and g[j][i] <min):
                        if(i in S):
                            continue
                        else:
                            min = g[j][i]
                            tempmin[0],tempmin[1] = j,i
                            m = 1
        f = tempmin[1]
        temp = copy.copy(tempmin)
        mintree.append(temp)
        S.append(f)
        print('当前轮数选取的边：',mintree)
    print('用Prim算法求得的最小生成树为:',mintree)

#Kruskal算法
def Kruskal(g):
    g_temp = copy.copy(g)               #初始化临时邻接矩阵，用于边的大小排序
    E_sorted = []                       #初始化边的排序数组
    tempmin = [0,0]                     #中间变量初始化
    while(len(E_sorted)<m):             #先对边进行大小排序，得到排序后的边数组
        min = 999
        for i in range(n):
            for j in range (i,n,1):
                if (g_temp[i][j] !=0 and g_temp[i][j] <min):
                    min = g_temp[i][j]
                    tempmin[0],tempmin[1] = i,j
        temp = copy.copy(tempmin)
        g_temp[tempmin[0]][tempmin[1]] = 0
        E_sorted.append(temp)
    print('kruskal算法排序后的边：',E_sorted)
    S = [E_sorted[0]]                   #初始化实时连接边集，用于辅助建立最小生成树
    mintree = [E_sorted[0]]             #初始化最小生成树，将第一条边加入
    print('当前轮数选取的边：',mintree)
    for i in E_sorted:                  #遍历已排序的边集，根据各个条件判断是否加入最小生成树
        l = len(S)
        mark1 = mark2 = -1
        if (len(S[0]) == n):            #若图已连通，则退出遍历
            break
        for v in range(l):              #判断当前边在连接图中的情况
            if i[0] in S[v]:
                mark1 = v
            if i[1] in S[v]:
                mark2 = v
        if (mark1 == mark2 == -1):      #如果该边两个顶点都不在当前选择图中，则加入边
            S.append(i)
            mintree.append(i)
        elif (mark1 == mark2):          #若都在图中且在同一条连通分量中，则跳过
            continue
        elif (mark1 == -1):             #若其中一个顶点不在图中，则加入连通分量，加入边
            S[mark2].append(i[0])
            mintree.append(i)
        elif (mark2 == -1):             #若其中一个顶点不在图中，则加入连通分量，加入边
            S[mark1].append(i[1])
            mintree.append(i)
        else:                           #若都在图中但不在同一条连通分量中，则将两条连通分量连接，加入边
            S.append(list(set(S[mark1]+S[mark2])))
            del_index = [mark1,mark2]
            S = [h for side, h in enumerate(S) if side not in del_index]
            mintree.append(i)
        print('当前轮数选取的边：',mintree)
    print('用Kruskal算法求得的最小生成树为:',mintree)

#打印邻接矩阵函数
def printJ(g):
    print('该图的邻接矩阵为：')
    for i in range (n):                         #遍历邻接矩阵数组
        for j in range (n):
            if (j == n-1):
                print('      ',g[i][j])
            else:
                print('      ',g[i][j],end=' ')

#测试模块
g = [[0,6,1,5,0,0],[6,0,5,0,3,0],[1,5,0,5,6,4],[5,0,5,0,0,2],[0,3,6,0,0,6],[0,0,4,2,6,0]]   #初始化无向图
n = len(g)
m = 10
printJ(g)
Prim(g)
Kruskal(g)