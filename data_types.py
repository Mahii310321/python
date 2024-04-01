#  type 
# literal assignment
some_string='some String Value'
print(type(some_string)) # str
print(type(some_string)==str)# true
print(isinstance(some_string,str))# true

# constructor function
constructor_string='another strring'
print(type(constructor_string)) # str
print(type(constructor_string)==str)# true
print(isinstance(constructor_string,str))# true


# casting - converting type of a (number) to string
cast=str(2024)
print(type(cast),cast) # str, '2024'

# multiple lines
multilines='''
first line 
    second line 
                    and so on...
'''
print(multilines)


# escaping special characters
# \n - new line
# \t - tab space

# methods
print(some_string)
print(some_string.lower())
print(some_string.upper())
print(some_string)

print(multilines)
print(multilines.title())
print(multilines.replace('so on','etc'))
print(multilines)

print(len(multilines))
multilines +='                             '
multilines='               '+multilines
print(len(multilines))

print(len(multilines.strip())) # remove space
print(len(multilines.lstrip()))# remove left side spaces
print(len(multilines.rstrip()))# remove right side spaces


print('center method'.center(20,'=')) # ===center method====
# check ljust and rjust also

print(some_string.startswith('s'))
print(some_string.endswith('s'))

print(' end of strings '.center(50,'*'))


# Boolean

value=True 
# constructor
x =bool(False)
print(value, x ,type(x))

print(' end of Booleans '.center(50,'*'))



# Numerics
# same as others check for type


# float type
cp=8.7
cp2=float(2.45) # constructor 
print(cp, cp2, type(cp)) #8.7,2.45,float


# built in functions 
print(abs(cp))
print(abs(cp*-1)) # will not return negative
print(round(cp))
print(round(cp,1))

import math # put it on top
print(math.pi)
print(math.sqrt(25))
print(math.ceil(4.8))
print(math.floor(4.8))


# cast a string to number
num='1000'
conv_num=int(num)
print(conv_num,type(conv_num))

# cannot cast a string of non numeric to number 
# print(int('string-error')) # error -invalid literal for int() with base 10
