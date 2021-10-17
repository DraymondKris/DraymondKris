from fractions import *
import random


# 生成分数
def create_fraction(r):
    denominator = random.randint(1, r)  # 生成分母
    numerator = random.randint(1, denominator * r)  # 生成分子
    fraction = Fraction(numerator, denominator)  # 生成假分数
    if '/' in str(fraction):
        if numerator > denominator:
            return turn_fraction(denominator, numerator)
    return str(fraction)


# 假分数转换为带分数
def turn_fraction(denominator, numerator):
    integer = numerator // denominator
    real_fraction = Fraction(numerator - integer * denominator, denominator)
    return str(str(integer) + '`' + str(real_fraction))


# 选择运算符
def create_symbol():
    symbol = ['+', '-', '×', '÷']
    num = random.randint(0, 3)
    return symbol[num]


# 构建二叉树结点
class tree_Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None
        self.result=0


# 构建二叉树
class tree(object):

    def __init__(self, root):
        root = tree_Node(root)
        self.root = root

    # 创建树形左子树
    def create_left_tree(self, left_tree):
        temp=self.root
        if isinstance(left_tree, tree):
            temp.left = left_tree.root
            temp.result=left_tree.root.result


    # 创建数据左子树
    def create_left_children(self, data):
        newNode = tree_Node(data)
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        temp.left = newNode
        newNode.result=str_to_num(data)
        temp.result=newNode.result


    # 创建树形右子树
    def create_right_tree(self, right_tree):
        temp=self.root
        if isinstance(right_tree, tree):
            temp.right = right_tree.root
            if temp.elem == '+':
                temp.result +=right_tree.root.result
            elif temp.elem == '-':
                temp.result = temp.result - right_tree.root.result
                if temp.result < 0:
                    temp.result = -1
            elif temp.elem == '×':
                temp.result *= right_tree.root.result
            elif temp.elem == '÷':
                if right_tree.root.result <= 0:
                    temp.result = -1
                else:
                    temp.result = Fraction(temp.result, right_tree.root.result)


    # 创建数据右子树
    def create_right_children(self, data):
        newNode = tree_Node(data)
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        temp.right = newNode
        newNode.result=str_to_num(data)
        if temp.elem == '+':
            temp.result += newNode.result
        elif temp.elem == '-':
            temp.result = temp.result-newNode.result
            if temp.result < 0:
                temp.result=-1
        elif temp.elem == '×':
            temp.result *= newNode.result
        elif temp.elem == '÷':
            if newNode.result<=0:
                temp.result=-1
            else:
                temp.result = Fraction(temp.result,newNode.result)


    # 中序遍历
    def midshow(self, new_tree, express):
        if new_tree is None:
            return
        if (new_tree.left is not None and new_tree.right is not None):
            express.append('(')
        self.midshow(new_tree.left, express)
        print(new_tree.elem)
        print(new_tree.result)
        express.append(new_tree.elem)
        self.midshow(new_tree.right, express)
        if (new_tree.left is not None and new_tree.right is not None):
            express.append(')')
        return express


def str_to_num(string):
    if '`' in string:
        integer = int(string.split('`')[0])
        denominator = int(string.split('`')[1].split('/')[1])
        numerator = int(string.split('`')[1].split('/')[0])
        return Fraction((integer * denominator + numerator), denominator)
    elif '/' in string:
        denominator = int(string.split('/')[1])
        numerator = int(string.split('/')[0])
        return Fraction(numerator, denominator)
    else:
        return Fraction(int(string), 1)


def del_unuseful(express_list):
    del express_list[0]
    del express_list[-1]


# 判断字符是否为运算符
def judge_symbol(str_temp):
    if str_temp in ('+', '-', '×', '÷'):
        return True
    return False


# 通过后缀表达式构建表达式二叉树
def create_express_tree(express_list):
    stack = []
    for str_temp in express_list:
        if judge_symbol(str_temp) is True:
            tree_temp = tree(str_temp)
            if len(stack) <= 0:
                print('错误！')
                return

            right_node = stack.pop()
            left_node = stack.pop()
            if isinstance(left_node, tree):
                tree_temp.create_left_tree(left_node)
            else:
                tree_temp.create_left_children(left_node)
            if isinstance(right_node, tree):
                tree_temp.create_right_tree(right_node)
            else:
                tree_temp.create_right_children(right_node)

            stack.append(tree_temp)
        else:
            stack.append(str_temp)
    return stack.pop()


def create_data(r):
    temp = random.choice([1, 2])
    if temp == 1:
        data = random.randint(0, r)
    else:
        data = create_fraction(r)
    return data


def create_express(r):
    symbol_num = random.randint(1, 3)  # 标点符号个数
    express_list = []
    number_count = 0
    symbol_count = 0
    for num in range(0, 2 * symbol_num + 1):
        if num <= 1:
            number_count += 1
            data = create_data(r)
            express_list.append(str(data))
        else:
            if number_count <= symbol_count + 1:
                number_count += 1
                data = create_data(r)
                express_list.append(str(data))
            elif number_count < symbol_num + 1:
                symbol_or_data = random.choice([0, 1])
                if symbol_or_data == 1:
                    number_count += 1
                    data = create_data(r)
                    express_list.append(str(data))
                else:
                    symbol_count += 1
                    symbol = create_symbol()
                    express_list.append(symbol)
            else:
                symbol_count += 1
                symbol = create_symbol()
                express_list.append(symbol)
    express_tree = create_express_tree(express_list)
    express = []
    express_tree.midshow(express_tree.root, express)
    del_unuseful(express)
    express_str = ' '.join(express)
    express_str = express_str + ' = '
    return express_tree,express_list,express_str






