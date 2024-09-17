my_dict = {'Route': 27738, 'Route2': 27746, 'Route3': 27756}
print(my_dict)
print(my_dict.get('Route10'))
my_dict.update({'Route4': 27766,
                'Route5': 27776})
print(my_dict)
print(my_dict.pop('Route5'))
# Множество
my_set = { 1,1,2,2,2,True,'None',(4,5,6)}
print(my_set)
my_set.add(5)
my_set.add(8)
print(my_set)
print(my_set.remove(8))
