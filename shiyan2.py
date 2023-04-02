#二分查找函数
def binarySearch(f,begin,end,x):               
    if (begin>end):                             #如果查询不到元素，则返回-1
        return -1
    mid = int((begin + end)/2)                       #获取代查数组的中值
    if (x == f[mid]):                           #查询到目标元素，返回位置
        return mid
    if (x > f[mid]):                            #目标元素大于中间值，往右查找
        return binarySearch(f,mid+1,end,x)
    else:                                       #目标元素小于中间值，往左查找
        return binarySearch(f,begin,mid-1,x)
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

#测试模块
n = []
print('请输入初始数组，输入p以终止输入')
while(1):                                       #设置输入循环，让用户自主输入想要排序的数字
    a = input()
    if a == 'p':
        break
    else:
        n.append(int(a))
n = kssort(n)
print('排序后的数组为：',n)
print('请输入你要查找的元素，输入s以终止查找')
while(1):                                       #设置输入循环，让用户自主输入想要查找的数字
    b = input()
    if b == 's':
        break
    else:
        p = binarySearch(n,0,len(n)-1,int(b))
        if (p == -1):
            print('该元素不存在！')
        else:
            print('该元素的位置为：',p)
