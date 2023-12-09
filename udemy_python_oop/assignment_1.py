from assignments import MaxSizeList

#int will define the length of the list

a = MaxSizeList(3) 
b = MaxSizeList(1)

a.push('hey')
a.push('hi')
a.push('lets')
a.push('go')

b.push('hey')
b.push('hi')
b.push('lets')
b.push('go')

print(a.get_list())
print(b.get_list())