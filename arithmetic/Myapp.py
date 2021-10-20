import creact_expression
import calculate
from tkinter import *


# 构建二叉树结点
class new_tree_Node(object):
    def __init__(self):
        self.elem = None
        self.left = None
        self.right = None


# 空节点添加数据为-1
def add_none_data(old_tree):
    new_tree = new_tree_Node()
    if old_tree is None:
        new_tree.elem = -1
        new_tree.left = None
        new_tree.right = None
        return new_tree
    new_tree.elem = old_tree.result
    new_tree.left = add_none_data(old_tree.left)
    new_tree.right = add_none_data(old_tree.right)
    return new_tree


# 判断两个题目是否相同
def judge_same_tree(tree1, tree2):
    if (tree1 is None and tree2 is not None) or (tree1 is not None and tree2 is None):
        return False
    if tree1 is None and tree2 is None:
        return True
    # 如果两棵树该结点的数据都相同且其a树的左子树等于b树的左子树且a树的右子树等于b树的右子树或者a树的左子树等于b树的右子树且a树的右子树等于b树的左子树时，认定两棵树相同
    if tree1.elem != tree2.elem:
        return False
    if (judge_same_tree(tree1.left, tree2.left) is False and judge_same_tree(tree1.right, tree2.right) is False) and (
            judge_same_tree(tree1.right, tree2.left) is False and judge_same_tree(tree1.left, tree2.right) is False):
        return False
    return True


def create_text(n, r):
    tree = []
    num = 0
    exp_file = 'Exercises.txt'
    answer_file = 'Answers.txt'
    f1 = open(exp_file, 'a', encoding='utf-8')
    f1.write(' ')
    f1.close()
    f2 = open(answer_file, 'a', encoding='utf-8')
    f2.write(' ')
    f2.close()
    f1 = open(exp_file, 'r+')
    f1.truncate()
    f1.close()
    f2 = open(answer_file, 'r+')
    f2.truncate()
    f2.close()
    while num < n:
        if len(tree) == 0:
            express_tree, express_list, express_str = creact_expression.create_express(r)
            answer = calculate.calculate(express_list)
            if answer == -1:
                continue
            tree.append(express_tree)
            f1 = open(exp_file, 'a', encoding='utf-8')
            f2 = open(answer_file, 'a', encoding='utf-8')
            f1.write(str(num + 1) + '. ' + express_str + '\n')
            f2.write(str(num + 1) + '. ' + str(answer) + '\n')
            f1.close()
            f2.close()
            num += 1
        else:
            express_tree, express_list, express_str = creact_expression.create_express(r)
            answer = calculate.calculate(express_list)
            if answer == -1:
                continue
            j = 0
            for i in range(len(tree)):
                old = add_none_data(tree[i].root)
                new = add_none_data(express_tree.root)
                if judge_same_tree(old, new) is True:
                    j = 1
                    break
            if j == 1:
                continue
            tree.append(express_tree)
            f1 = open(exp_file, 'a', encoding='utf-8')
            f2 = open(answer_file, 'a', encoding='utf-8')
            f1.write(str(num + 1) + '. ' + express_str + '\n')
            f2.write(str(num + 1) + '. ' + str(answer) + '\n')
            f1.close()
            f2.close()
            num += 1


def express_to_houzui(express):
    result = []
    stack = []
    s = express.split(' ')
    for item in s:
        if item.isnumeric() or '/' in item or '`' in item:
            result.append(item)
        else:
            if len(stack) == 0:
                stack.append(item)
            elif item in '×÷(':
                stack.append(item)
            elif item == ')':
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()
            elif item in '+-' and stack[-1] in '×÷':
                if stack.count('(') == 0:
                    while stack:
                        result.append(stack.pop())
                else:
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)
            else:
                stack.append(item)
    while len(stack) != 0:
        result.append(stack.pop())
    result.remove('')
    return result


def mark_grade(e, a):
    correct_num = 0
    correct = []
    wrong_num = 0
    wrong = []
    f1 = open(e, 'r', encoding='utf-8')
    f2 = open(a, 'r', encoding='utf-8')
    list1 = f1.readlines()
    list2 = f2.readlines()
    f1.close()
    f2.close()
    for i in range(len(list2)):
        express = list1[i].split('. ')[1].split('=')[0]
        houzui = express_to_houzui(express)
        answer = calculate.calculate(houzui)
        if len(list2[i].split('. ')) < 2:
            answer_user = '-1'
        else:
            answer_user = list2[i].split('. ')[1].split('\n')[0]
        if str(answer) == answer_user:
            correct.append(i + 1)
            correct_num += 1
        else:
            wrong.append(i + 1)
            wrong_num += 1
    if len(list2) < len(list1):
        num = len(list1) - len(list2)
        for i in range(num):
            wrong.append(len(list2) + i + 1)
            wrong_num += 1
    f3 = open('Grade.txt', 'a', encoding='utf-8')
    f3.write(' ')
    f3.close()
    f3 = open('Grade.txt', 'r+')
    f3.truncate()
    f3.close()
    f3 = open('Grade.txt', 'a', encoding='utf-8')
    f3.write('Correct: ')
    f3.write(str(correct_num) + '(')
    for j in range(len(correct)):
        f3.write(str(correct[j]))
        if j < len(correct) - 1:
            f3.write(',')
    f3.write(')\n')
    f3.write('Wrong: ')
    f3.write(str(wrong_num) + '(')
    for j in range(len(wrong)):
        f3.write(str(wrong[j]))
        if j < len(wrong) - 1:
            f3.write(',')
    f3.write(')\n')
    f3.close()


class UI(object):
    def __init__(self, master=None):
        self.root = master
        self.var = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        self.var.set('请选择你想要选择的功能')
        Label(self.page, textvariable=self.var).grid(row=1, column=1, stick=W)
        Button(self.page, text='出题', command=self.set_questions).grid(row=3, column=0, sticky=W, padx=10, pady=5)
        Button(self.page, text='改卷', command=self.correct).grid(row=3, column=1, sticky=W, padx=10, pady=5)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=2, sticky=W, padx=10, pady=5)

    def set_questions(self):
        self.page.destroy()
        set_UI(self.root)

    def correct(self):
        self.page.destroy()
        correct_UI(self.root)


class set_UI(object):
    def __init__(self, master=None):
        self.root = master
        self.n = StringVar()
        self.r = StringVar()
        self.result = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page, text='请输入想要生成的题目数量：').grid(row=0, column=0, stick=W)
        Entry(self.page, textvariable=self.n).grid(row=0, column=1, stick=E, padx=5, pady=5)
        Label(self.page, text='请输入想要生成的数值范围：').grid(row=1, column=0)
        Entry(self.page, textvariable=self.r).grid(row=1, column=1, padx=5, pady=5)
        Button(self.page, text='开始出题',
               command=lambda: self.create(self.n, self.r, self.result)).grid(
            row=2, column=0, sticky=W, padx=10, pady=5)
        Entry(self.page, textvariable=self.result, width=40).grid(row=4, column=0, columnspan=3)
        Button(self.page, text='退出', command=self.page.quit).grid(row=2, column=2, sticky=W, padx=10, pady=5)
        Button(self.page, text='返回', command=self.back).grid(row=2, column=1, sticky=W, padx=10, pady=5)

    def create(self, n, r, result):
        try:
            create_text(int(n.get()), int(r.get()))
            result.set('题目已生成，在当前目录下的Exercises.txt文件里')
        except ValueError:
            result.set('请输入正确的数值（自然数）')

    def back(self):
        self.page.destroy()
        UI(self.root)


class correct_UI(object):
    def __init__(self, master=None):
        self.root = master
        self.e = StringVar()
        self.a = StringVar()
        self.result = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page, text='请输入题目文件：').grid(row=0, column=0, stick=W)
        Entry(self.page, textvariable=self.e).grid(row=0, column=1, stick=E, padx=5, pady=5)
        Label(self.page, text='请输入答案文件：').grid(row=1, column=0)
        Entry(self.page, textvariable=self.a).grid(row=1, column=1, padx=5, pady=5)
        Button(self.page, text='开始改卷',
               command=lambda: self.correct(self.e, self.a, self.result)).grid(
            row=2, column=0, sticky=W, padx=10, pady=5)
        Entry(self.page, textvariable=self.result, width=40).grid(row=4, column=0, columnspan=3)
        Button(self.page, text='退出', command=self.page.quit).grid(row=2, column=2, sticky=W, padx=10, pady=5)
        Button(self.page, text='返回', command=self.back).grid(row=2, column=1, sticky=W, padx=10, pady=5)

    def correct(self, e, a, result):
        try:
            mark_grade(e.get(), a.get())
            result.set('成绩已出，请到当前目录下的Grade.txt文件查看')
        except FileNotFoundError:
            result.set('文件路径错误，请输入正确的文件路径')

    def back(self):
        self.page.destroy()
        UI(self.root)


if __name__ == '__main__':
    root = Tk()
    UI(root)
    root.mainloop()
