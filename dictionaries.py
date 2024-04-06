# dictionaries
dict1={
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "English"]
}

#access
print(dict1['name'])
print(dict1.get('age'))

print(dict1.keys()) # list all keys
print(dict1.values()) # list all values


print(dict1.items()) # list all key?value as tuples

print('grade' in dict1)
print('subject' in dict1)

#  pop and poitem removes a key but returns value and key-value respectively

# del dict1['courses'] # delte a key
# del dict1 # delete object

dict2=dict1.copy() # creates a copy
dict3=dict(dict1)


# sets

nums={1,2,34,5,6,6,5,5,}
print(nums)
print(len(nums))
print(type(nums))

val={1,True,3,5,False,4,6,0,45}
print(val)# takes one and false because they are first than their duplicates of their 1& 0

#check if a value is init or not
print(45 in nums)

# but you cannot refer to an element in the set with an index or key

# add a new element
nums.add(8)
print(nums)

# update
nums2={237,4564}
nums.update(nums2)
# union() # merge two sets

# keep  only the duplicated
one={1,2,3}
two={2,3,5}
one.intersection_update(two)
print(one)

# //keep everything except duplicates
one={1,2,3}
two={2,3,5}
one.symmetric_difference_update(two)
print(one)