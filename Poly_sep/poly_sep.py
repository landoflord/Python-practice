from itertools import product


def main():
    #logic_value = input("Введите значность логики:")
    #var_counter = input("Введите число переменных:")
    path = "D:\\Vs code Projects\\Poly_sep\\func.txt"
    output = []
    logic_value = 2
    var_counter = 4
    output = x_input_generator(logic_value, var_counter, var_counter, output)
    tmp = function_dictionary_generator (output, path)
    print(tmp)
    polynomyal_sep_func_generator(2, 4, 2)


def x_input_generator (logic_value:int, var_counter: int, counter_etalon: int, output, prefix=None):
    """ Функция генерирует значения переменных для дискрутных функций по значности логики и
        количеству переменных
    """
    prefix = prefix or []
    if var_counter == 0:
        if len(prefix) == counter_etalon:
            output.append(tuple(prefix))
        return output
    for digit in range(logic_value):
        prefix.append(digit)
        x_input_generator(logic_value, var_counter-1, counter_etalon, output, prefix)
        prefix.pop()
    return output

def function_dictionary_generator (var_combinations, function_values_path):
    """ Генератор словаря для дискретных функций
    """
    discrete_functions = []
    with open (function_values_path) as func_values:
        lines = func_values.readlines()
        for line in lines:
            discrete_functions.append({x: y for x in var_combinations for y in line.split('#')[0].split(';')})
    return discrete_functions
    
def polynomyal_sep_func_generator (polynom_degree: int, var_counter: int, logic:int):
    """ Генератор функций полиномиального разделения
    """
    iterator = ''
    for i in range(logic):
        iterator += str(i)
    if logic == 2:
        print(*(''.join(it) for it in product(iterator, repeat=var_counter) if it.count('1') <= polynom_degree), sep='\n')


if __name__ == "__main__":
    main()