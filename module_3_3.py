def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(5, 'pyramid', False)
print_params(455, 'COLT')
print_params('folk', 23)
print_params(b=25)
print_params(c = [1,2,3])
# Распаковка
value_list= [12 ,'String', False]
value_dict= {'a':5, 'b':20, 'c':60}
print_params(*value_list)
print_params(**value_dict)
# Распаковка + отдельные параметры
value_list_2= ['stone', 30]
print_params(*values_list_2, 42)
