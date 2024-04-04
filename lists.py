first_list=['django','python','javascript','postgresql',]

print(first_list.index('python')) # finds index in list
# print(first_list.index('react')) # error if there is no element in list
first_list.append('flask') # addes an element to the list
print(first_list)

# concat
second_list =['html','css','jquery']
#method 1
first_list+=second_list # it should be a list , if it is a string it will add all the individual characters inside the list

print(first_list)

#method 2
third_list =['vscode',]
first_list.extend(third_list)
print(first_list)
print('+++++++++++++++++++++++++++++')
first_list.insert(0,'react')
print(first_list)

second_list[2:2]=['nextjs','vuejs']
print(second_list)

second_list[0:3]=['hello','world']
print(second_list)
second_list.remove('hello')
del second_list[0]
# del second_list # this will delete the list
# second_list.clear() # this makes list empty
print(second_list)

# if we use global sorted method to sort it will not change the original array

# copy of list
copy1=first_list.copy() # using copy metho
copy2=list(first_list) # using constructor
copy3=first_list[:]# using list



#####################################

# tuples

mytuple=tuple(('32',False,'some text'))
anothertuple=['some','random','text']

# we cannot update tuple directly
mytuple_list=list(mytuple)
mytuple_list.append('last')
updated_tuple=tuple(mytuple_list)
print(updated_tuple)


# unpack
# * is like spread operator
(one,two,*three)=updated_tuple
print(one)
print(two)
print(three)
