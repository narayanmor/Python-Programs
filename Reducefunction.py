#when we need to aggregate the values (e.g sum,product,max)
#reduce is a part of functools and must be imported before use


from functools import reduce

l=[1,3,4,5,6]


#def smmation(a,b):
 #   return a+b
#b=reduce(smmation,l)
#print(b)


b=reduce(lambda a,b :a*b,l)

print(b)