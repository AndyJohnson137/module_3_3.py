def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(8), print_params(4,12),print_params(7, 'двадцать', False)
print_params(b = 74)
print_params(c = [1, 2, 3])

values_list = [True, 13, 'текст']
values_dict = {'a': 55, 'b': "word",'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32,'Строка']

print_params(*values_list_2,42)