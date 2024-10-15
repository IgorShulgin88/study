my_dict={'Vasya': 1986,'Leva':1982,'Masha':2000 }
print(my_dict)
print(my_dict['Leva'])
my_dict.update({'Mama':1968,'Kolya':1990})
print(my_dict)
del my_dict['Masha']
print(my_dict.get('Masha','2000'))
print(my_dict)
my_set={1,1,1,1,2,2,2,2,2,3,33,3,3,3,3,'summer',(1,5,'faust')}
print(my_set)
print(my_set.add(12))
print(my_set.add(9))
print(my_set)
print(my_set.remove(33))
print(my_set)