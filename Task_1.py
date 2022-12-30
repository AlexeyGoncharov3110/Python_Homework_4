def koef(int):
    import random
    degree_coefficient = {}
    for i in range(k, -1, -1):
        degree_coefficient[i] = random.randint(-100, 100)
    return degree_coefficient


for i in range(2):
    if i == 0:
        k = int(input('введите максимальную степень первого многочлена: '))
    deg_koef1 = koef(k)
    if i == 1:
        k = int(input('введите максимальную степень второго многочлена: '))
    deg_koef2 = koef(k)

print(deg_koef1)
print(deg_koef2)


def equation(my_dict):
    equation_str = ''
    for k, v in my_dict.items():
        if v == 0:
            equation_str.replace(f'0*x**{v}', '')
        elif v == 1 and k == 1:
            equation_str.replace(f'1*', 'x')
        elif v == 1 and k > 1:
            equation_str += f'x**{k} + '
        elif k == 1:
            equation_str += f'{v}*x + '
        elif k == 0:
            equation_str += f'{v} + '
        else:
            equation_str += f'{v}*x**{k} + '
    else:
        equation_str = equation_str[:-3]
        equation_str += ' = 0'
    return equation_str


equation_str1 = equation(deg_koef1)
print(equation_str1)
equation_str2 = equation(deg_koef2)
print(equation_str2)
with open('polynomial1.txt', 'w') as data:
    data.write(equation_str1)
with open('polynomial2.txt', 'w') as data:
    data.write(equation_str2)

with open('polynomial1.txt', 'r') as text:
    equat = text.readline()
with open('polynomial2.txt', 'r') as text:
    equat2 = text.readline()
print(equat)
print(equat2)


def convert_to_dict(equation):
    dictEquation = {}
    equation = equation.replace(
        ' + ', ' +').replace('*x ', '*x**1 ').replace(' = 0', '*x**0').split()

    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('*x**')
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    return dictEquation


final_dict1 = convert_to_dict(equat)
final_dict2 = convert_to_dict(equat2)
print(final_dict1)
print(final_dict2)


def sumEquation(dict1, dict2):
    dict_final = {}
    maximum = max(max(dict1), max(dict2))
    for i in range(maximum, -1, -1):
        first = dict1.get(i, 0)
        second = dict2.get(i, 0)
        dict_final[i] = first+second
    return dict_final


sum_equat = sumEquation(final_dict1, final_dict2)
print(sum_equat)


def final_str(dict):
    result = ''
    for i in dict.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + '*x**' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + '*x**' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + '*x**' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + '*x**' + str(abs(i[0]))
        result = result.replace(
            'x**1', 'x').replace('*x**0', '').replace('1x', 'x')
    result += ' = 0 '

    return result


final_equation = final_str(sum_equat)
print(final_equation)
with open('final_polynominal','w') as text:
    text.writelines(final_equation)
