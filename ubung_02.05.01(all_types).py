int_variable = 5
float_variable = 10.2
komplex_variable = 5+3j
str_variable = 'Violetta'

print(f"Der Datentyp von ganze_zahl ist: {type(int_variable)}")
print( "Der Datentyp von", "int_variable", "ist:", type(int_variable))
print( "Der Datentyp von", "float_variable", "ist:", type(float_variable))
print( "Der Datentyp von", "komplex_variable", "ist:", type(komplex_variable))
print( "Der Datentyp von", "str_variable", "ist:", type(str_variable))

int_to_float = float(int_variable) #konventierung von int to float
int_to_str = str(int_variable) #konventierung von int to string

print(type(int_to_float))
print(type(int_to_str))


variable_tupel = (6, 'z', 7.3, 4.5, 'b', 5)
variable_list = [4, 'a', 7, 2.5, 'b', 5]
# I know the number of cylinders is always at index 1
car_description = ('red', 6, 'Mazda')
# The order may be important, but the index does not give information about the element type
my_cars = ['Nissan Leaf', 'Toyota Pickup', 'Toyota Pickup']
print(my_cars)

cars_set = {'Nissan Leaf', 'Toyota Pickup', 'Toyota Pickup'}
print(cars_set)

print(type(variable_tupel))
print(type(variable_list))
print(type(car_description))
print(type(my_cars))
print(type(cars_set))

neue_liste = []
neue_liste.extend(variable_list[:2])
print(neue_liste)
neue_liste.extend(variable_tupel)
print(neue_liste)

neue_liste2 = [variable_list[0], variable_list[1], variable_tupel[-1]]
print(f"Neue Liste: {neue_liste2}")
#neue_liste = liste[:2]
#if tupel[-1] not in neue_liste:
#    neue_liste.append(tupel[-1])
#print(neue_liste)  # [1, 'Zwei', 3.0]

cars_set.add('Nissan Leaf')
print(cars_set)
cars_set.add('Audi')
print(cars_set)