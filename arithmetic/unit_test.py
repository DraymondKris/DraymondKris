import unittest
import calculate
import creact_expression
import Myapp
from fractions import Fraction


class MyTest(unittest.TestCase):
    #测试将假分数转换为真分数
    def test1(self):
        self.assertEqual(creact_expression.turn_fraction(3,10),'3`1/3')

    #测试字符串转换为分数
    def test2(self):
        self.assertEqual(creact_expression.str_to_num('3`1/3'),Fraction(10,3))

    #测试生成表达式
    def test3(self):
        tree,list,expression=creact_expression.create_express(5)
        print(expression)

    #测试计算过程
    def test4(self):
        self.assertEqual(calculate.calculate(['1','3','3','4','×','+','×']),15)

    #测试e1-e2出现负数的情况
    def test5(self):
        self.assertEqual(calculate.calculate(['3','7','-']),-1)

    #测试除数为0的情况
    def test6(self):
        self.assertEqual(calculate.calculate(['3','4','4','-','÷']),-1)

    #测试两个式子相等
    def test7(self):
        self.assertTrue(Myapp.judge_same_tree(Myapp.add_none_data(creact_expression.create_express_tree(['1','2','+']).root),Myapp.add_none_data(creact_expression.create_express_tree(['2','1','+']).root)))

    # 测试两个式子不相等
    def test8(self):
        self.assertFalse(Myapp.judge_same_tree(Myapp.add_none_data(creact_expression.create_express_tree(['2', '2', '+']).root),Myapp.add_none_data(creact_expression.create_express_tree(['2', '1', '+']).root)))

    #测试判断是否为运算符
    def test9(self):
        self.assertTrue(creact_expression.judge_symbol('+'))

    #测试判断不是运算符
    def test10(self):
        self.assertFalse(creact_expression.judge_symbol('1`5/6'))

if __name__ == '__main__':
    unittest.main()
