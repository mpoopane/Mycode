#!/usr/bin/python
val=['a','b','c','d','e','f']
key=[0,1,2,3,4,5]

print("Key", key)
print("Value", val)

#Iterate over the list
for i in val:
    print('#Iterate over the list', i)

#Convert list to dict with index
data= dict(zip(key,val))
print('#Convert list to dict with index', data)

#iterare over dict
for k, v in data.items():
    print('#iterare over dict', k, v)

#Convert list to dict using enumerate
data = {k: v for k, v in enumerate(val)}
print('#Convert list to dict using enumerate', data)

#Create dict

ls = [('a',1), ('b',2), ('c',3), ('d',4)]
print("This is my list", ls)
print("Convert to dict by using:  dict(ls)", dict(ls))
