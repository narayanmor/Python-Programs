#filter function is used to extarct elements from an iterable(like,list,tuple) that satisfy given condition
#it works by applying functon to each elememnt and keeping only those value sthat function returns true.

l=[1,2,4,6,8,7,7,13]

print("Using the function")

def even(n):
 return n%2==0             #Condition to check even number
print(list(filter(even,l))) #hare using the filter to print only even number

print("Using the function")

def odd(m):
 return m%2!=0             #Condition to check odd number
print(list(filter(odd,l))) #hare using the filter to print only even number

print("Using the lambda function")

print(list(filter(lambda q:q%2!=0,l))) 
print(list(filter(lambda q:q%2==0,l))) 


#below is printing only those name having greate than 5 char
a=["banana","apple","mango","cheri","kiwi"]

print(list(filter(lambda l:len(l) > 5,a)))
