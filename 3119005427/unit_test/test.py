import unittest
from main.main import main_test


class MyTest(unittest.TestCase):
    def error_path(self):
        main_test('../textfile/orig.txt', '../orig.txt', '../result.txt')
        raise FileNotFoundError("文件不存在。")

    # 文件输入错误的单元测试
    def test1(self):
        with self.assertRaises(FileNotFoundError):
            self.error_path()

    #测试orig.txt与orig_0.8_add.txt
    def test2(self):
        main_test('../textfile/orig.txt','../textfile/orig_0.8_add.txt','../result.txt')

    #测试orig.txt与orig_0.8_del.txt
    def test3(self):
        main_test('../textfile/orig.txt', '../textfile/orig_0.8_del.txt', '../result.txt')

    #测试orig.txt与orig_0.8_dis_1.txt
    def test4(self):
        main_test('../textfile/orig.txt', '../textfile/orig_0.8_dis_1.txt', '../result.txt')

    #测试orig.txt与orig_0.8_dis_10.txt
    def test5(self):
        main_test('../textfile/orig.txt', '../textfile/orig_0.8_dis_10.txt', '../result.txt')

    #测试orig.txt与orig_0.8_dis_15.txt
    def test6(self):
        main_test('../textfile/orig.txt', '../textfile/orig_0.8_dis_15.txt', '../result.txt')

    #测试orig_0.8_add.txt与orig_0.8_del.txt
    def test7(self):
        main_test('../textfile/orig_0.8_add.txt', '../textfile/orig_0.8_del.txt', '../result.txt')

    #测试orig_0.8_add.txt与orig_0.8_dis_1.txt
    def test8(self):
        main_test('../textfile/orig_0.8_add.txt', '../textfile/orig_0.8_dis_1.txt', '../result.txt')

    #测试orig_0.8_dis_1.txt与orig_0.8_dis_10.txt
    def test9(self):
        main_test('../textfile/orig_0.8_dis_1.txt', '../textfile/orig_0.8_dis_10.txt', '../result.txt')

    #测试orig_0.8_dis_1.txt与orig_0.8_dis_15.txt
    def test10(self):
        main_test('../textfile/orig_0.8_dis_1.txt', '../textfile/orig_0.8_dis_15.txt', '../result.txt')


if __name__ == '__main__':
    unittest.main()