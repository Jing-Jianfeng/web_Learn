"""
2017/03/27

web17 数据结构和算法分析
"""

"""
# 算法的时间复杂度

大 O 记法，是描述算法复杂度的符号
O(1)
    常数复杂度，最快速的算法。
    取数组第 1000000 个元素
    字典和集合的存取都是 O(1)
    数组的存取是 O(1)
O(lgN)
    对数复杂度
    假设有一个有序数组，以二分法查找
O(n)
    线性复杂度
    假设有一个数组，以遍历的方式在其中查找元素
O(nlgn)
    求两个数组交集，其中一个是有序数组      
    A 数组每一个元素都要在 B 数组中进行查找操作
    每次查找如果使用二分法则复杂度是 lgN
O(N^2)
    平方复杂度
    求两个无序数组的交集

"""

"""
问题：
o(1)与o(n)的区别：
    o(1)是确定的
    O（n）是随着数据规模增长而增长的


"""

"""
数据结构基础

name = 'gua'    # str
height = 1.69   # float
age = 18        # int

# list
scores = [90, 98, 100, 100]

# dict
student = {
    'name': 'gua',
    'score': 59,
}

# 类是高级字典，本质还是字典
class Student():
    def __init__(self):
        self.name = ''
        self.score = -1


# 针对常用的操作，我们发明了一套常用的数据结构
# 四大数据结构
1，数组
    连续的一块内存
    读取元素时间是 O(1)
    插入、删除是 O(n)
2，链表
    手拉手的盒子，一个盒子只能访问左右手的盒子
    以下标方式读取元素的时间是 O(n)
    插入、删除是 O(1)
    栈和队列是链表的改良型
3，字典
    把字符串转为数字作为下标存储到数组中
    字符串转化为数字的算法是 O(1)
    所以字典的存取操作都是 O(1)
    除非对数据有顺序要求，否则字典永远是最佳选择
    字符串转化为数字的算法
        1，确定数据规模，这样可以确定容器数组的大小 Size
        2，把字符当作 N 进制数字得到结果
            'gua' 被视为 g * 1 + u * 10 + a * 100 得到结果 n
            n % Size 作为字符串在数组中的下标
            通常 Size 会选一个 素数
4，搜索树（我们只用，不写，甚至只是隐含在用，你并不知道你用的是树）


额外的，图是一种有时候有用但你一辈子都可能写不到的数据结构
只了解，不用学习如何实现
图的应用举例
    地图导航
    全国几个大城市之间的出行方案(有价格/时间/路途等权重)
"""


# 一个简单的哈希函数
# def hash(s):
#     n = 1
#     f = 1
#     for i in s:
#         ascii = ord(i)
#         n += ascii * f
#         f *= 10
#     return n
#
# names = [
#     'gua',
#     'xiao',
#     'name',
#     'web',
#     'python',
# ]
#
# for key in names:
#     h = hash(key)
#     print(h, h % 3)


class Node():
    def __init__(self, element=None):
        self.e = element
        self.next = None

head = Node()
n1 = Node(111)
n2 = Node(222)
n3 = Node(333)
n1.next = n2
n2.next = n3

head.next = n1

def append(node, element):
    """
    我们往 node 的末尾插入一个元素
    :param node: 是一个 Node 实例
    :param element: 任意类型的元素
    """
    n = node
    while n.next is not None:
        n = n.next
    # n 现在是最后一个元素
    new_node = Node(element)
    n.next = new_node

def prepend(head, element):
    n = Node(element)
    n.next = head.next
    head.next = n

def pop(head):
    tail = head 
    while tail.next is not None:
        tail = tail.next
    # 现在 tail 是最后一个元素了
    n = head
    while n.next is not tail:
        n = n.next
    # 现在 n 是 tail 之前的元素了
    n.next = None
    return tail.e


def log_list(node):
    n = node
    s = ''
    while n is not None:
        s += (str(n.e) + ' > ')
        n = n.next
    print(s)

log_list(n1)
append(n1, 'gua')
log_list(n1)
prepend(head, 'hello')
log_list(head)
print('pop head ', pop(head))
log_list(head)
# class LinkedList():
#     def __init__(self):
#         self.head = Node()
