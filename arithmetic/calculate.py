from fractions import Fraction


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
        return int(string)


def turn_fraction(fraction1):
    fraction2=str(fraction1)
    numerator = int(fraction2.split('/')[0])
    denominator = int(fraction2.split('/')[1])
    integer = numerator // denominator
    real_fraction = Fraction(numerator - integer * denominator, denominator)
    return str(str(integer) + '`' + str(real_fraction))


# 判断字符是否为运算符
def judge_symbol(str_temp):
    if str_temp in ('+', '-', '×', '÷'):
        return True
    return False


def calculate(houzui):
    num = []
    for j in houzui:
        if judge_symbol(j) is False:
            num.append(str_to_num(j))
        else:
            num2 = num.pop()
            num1 = num.pop()
            if j == '+':
                num.append(num1 + num2)
            elif j == '-':
                if num2 > num1:
                    return -1
                else:
                    num.append(num1 - num2)
            elif j == '×':
                num.append(num1 * num2)
            else:
                if num2 == 0:
                    return -1
                else:
                    num.append(Fraction(num1, num2))
    if num[0] > 1 and '/' in str(num[0]):
        return turn_fraction(num[0])
    return num[0]
