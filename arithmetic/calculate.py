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
        return Fraction(int(string), 1)


def turn_fraction(fraction):
    numerator=fraction.split('/')[0]
    denominator=fraction.split('/')[1]
    integer = numerator // denominator
    real_fraction = Fraction(numerator - integer * denominator, denominator)
    return str(str(integer) + '`' + str(real_fraction))



# 判断字符是否为运算符
def judge_symbol(str_temp):
    if str_temp in ('+', '-', '×', '÷'):
        return True
    return False


def calculate(houzui):
    num=[]
    result=[]
    for j in houzui:
        if judge_symbol(j) is False:
            num.append(str_to_num(j))
            result.append(str_to_num(j))
        else:
            num2=num.pop()
            num1=num.pop()
            if j=='+':
                num.append(num1+num2)
                result.append(num1+num2)
            elif j=='-':
                if num2>num1:
                    return -1
                else:
                    num.append(num1-num2)
                    result.append(num1 - num2)
            elif j=='×':
                num.append(num1*num2)
                result.append(num1 * num2)
            else:
                if num2==0:
                    return -1
                else:
                    num.append(Fraction(num1,num2))
                    result.append(Fraction(num1,num2))
    if num[0]>1 and '/' in str(num[0]):
        return result,turn_fraction(num[0])
    return result,num[0]

express=['4`1/2', '1', '-', '3`4/5', '÷']
result,num=calculate(express)
print(result)


