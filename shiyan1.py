import random
#冒泡排序函数
def maopao(n):
    l = len(n)                                  #获取数组长度
    for i in range(l-1):
        for j in range (l-i-1):   
            if n[j]>n[j+1]:                     #相邻两个元素比较
                n[j],n[j+1] = n[j+1],n[j]       #交换两个元素
#快速排序函数
def kssort(n):
    if len(n)<=1:
        return n
    left = []                                   #初始化左集
    right = []                                  #初始化右集
    base = n[0]                                 #设置基点  
    del n[0]                                    #删去数组中的基点
    for i in n:
        if i<=base:
            left.append(i)                      #小于等于基点则加入左集
        else:
            right.append(i)                     #大于基点则加入右集
    return kssort(left) + [base] + kssort(right)#进行递归运算

#测试函数
n = []
print('请输入你要排序的数组，输入p以终止输入')
while(1):                                       #设置输入循环，让用户自主输入想要排序的数字
    a = input()
    if a == 'p':
        break
    else:
        n.append(int(a))
print('你需要排序的数组为：',n)
maopao(n)
print('冒泡排序的结果为：',n)
random.shuffle(n)                               #打乱数组以重新排序
print('你需要排序的数组为：',n)
print('快速排序的结果为：',kssort(n))
