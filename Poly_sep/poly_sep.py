from itertools import product, combinations_with_replacement, combinations
import os

def main():
    #logic_value = input("Введите значность логики:")
    #var_counter = input("Введите число переменных:")
    path = "D:\\Vs code Projects\\Poly_sep\\functions.txt"
    output = []
    logic_value = 2
    var_counter = 4
    polynom_degree = 4
    output = x_input_generator(logic_value, var_counter, var_counter, output)
    #output.sort(key = lambda x: [x[j] for j in reversed(range(var_counter))])
    functions, func_id = function_dictionary_generator (output, path)
    polynomyal_sep_func_generator(polynom_degree, var_counter, logic_value, functions, func_id)


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
        func_id = []
        lines = func_values.readlines()
        for line in lines:
            func = {}
            func_values =  line.split('#')[0].split(';')
            func_id.append(line.split('#')[1])
            n = len(var_combinations)
            for x in range(n):  
                func[var_combinations[x]] = func_values[x]
            discrete_functions.append(func)
            #discrete_functions.append({x: y for x in var_combinations for y in line.split('#')[0].split(';')})
    return discrete_functions, func_id
    
def polynomyal_sep_func_generator (polynom_degree: int, var_counter: int, logic:int, discr_funcs, discr_funcs_id):
    """ Генератор функций полиномиального разделения
    """
    iterator = []
    polynom_func = []
    for i in range(1, var_counter + 1):
        iterator.append(str(i))
    # Для булевых функций генерация без повторов тк x1*x1 эквивалентно x1
    if logic == 2:
        for i in range(polynom_degree):
            #for comb in product(iterator, repeat=i + 1):
            for comb in combinations(iterator, i + 1):
                eq = 'a' + ''.join(comb)
                term = [0 for x in range(var_counter)]
                for x in comb:
                    term[int(x) - 1] = 1
                    eq = eq + ' * x' + x
                polynom_func.append(term)
                #print(eq)
    else:
        for i in range(polynom_degree):
            #for comb in product(iterator, repeat=i + 1):
            for comb in combinations_with_replacement(iterator, i + 1):
                eq = 'a' + ''.join(comb)
                term = [0 for x in range(var_counter)]
                for x in comb:
                    term[int(x) - 1] = 1
                    eq = eq + ' * x' + x
                polynom_func.append(term)
                #print(eq)
    n = len(polynom_func)
    for func in range(len(discr_funcs)):
        inequalities_a = []
        inequalities_b = []
        for key, value in discr_funcs[func].items():
            coef = 1
            additional_thresholds = [0] * (logic - 1)
            if value == '0':
                cur_inequlity_a = []
                cur_inequlity_b = []
                for t in range(n):
                    lenght_poly = len(polynom_func[t])
                    for i in range(lenght_poly):
                        if polynom_func[t][i] != 0:
                            coef *= key[i]
                    cur_inequlity_a.append(coef)
                    coef = 1
                additional_thresholds [int(value)] = -1
                cur_inequlity_a += additional_thresholds
                cur_inequlity_b.append(0)
                inequalities_a.append(cur_inequlity_a)
                inequalities_b.append(cur_inequlity_b)
            elif value == str(logic - 1):
                cur_inequlity_a = []
                cur_inequlity_b = []
                for t in range(n):
                    lenght_poly = len(polynom_func[t])
                    for i in range(lenght_poly):
                        if polynom_func[t][i] != 0:
                            coef *= key[i]
                    cur_inequlity_a.append(str(-1 * coef))
                    coef = 1
                additional_thresholds [int(value) - 1] = 1
                cur_inequlity_a += additional_thresholds
                cur_inequlity_b.append(-1)
                inequalities_a.append(cur_inequlity_a)
                inequalities_b.append(cur_inequlity_b)
            else:
                additional_thresholds1 = [0] * (logic - 1)
                additional_thresholds2 = [0] * (logic - 1) 
                cur_inequlity_a1 = []
                cur_inequlity_b1 = []
                cur_inequlity_a2 = []
                cur_inequlity_b2 = []
                for t in range(n):
                    lenght_poly = len(polynom_func[t])
                    for i in range(lenght_poly):
                        if polynom_func[t][i] != 0:
                            coef *= key[i]
                    cur_inequlity_a1.append(coef)
                    cur_inequlity_a2.append(-1 * coef)
                    coef = 1
                additional_thresholds1 [int(value)] = -1
                additional_thresholds2 [int(value) - 1] = 1
                cur_inequlity_a1 += additional_thresholds1
                cur_inequlity_b1.append(0)
                cur_inequlity_a2 += additional_thresholds2
                cur_inequlity_b2.append(-1)
                inequalities_a.append(cur_inequlity_a1) 
                inequalities_a.append(cur_inequlity_a2)
                inequalities_b.append(cur_inequlity_b1)
                inequalities_b.append(cur_inequlity_b2)
        with open(os.path.dirname(os.path.realpath(__file__)) + '\\FOR_HACHIYAN' + '\\' + 'a_' + str(polynom_degree) + '_' + discr_funcs_id[func].strip('\n') + '.txt', 'w') as f:
            first = True
            for i in inequalities_a:
                if first:
                    first = False
                    print(*i, file=f, sep = ';', end = '')
                else:
                    print(file=f)
                    print(*i, file=f, sep = ';', end = '')
        with open(os.path.dirname(os.path.realpath(__file__)) + '\\FOR_HACHIYAN' + '\\' + 'b_' + str(polynom_degree) + '_' + discr_funcs_id[func].strip('\n') + '.txt', 'w') as f:
            first = True
            for i in inequalities_b:
                if first:
                    first = False
                    print(*i, file=f, end = '')
                else:
                    print(file=f)
                    print(*i, file=f, end = '')


if __name__ == "__main__":
    main()