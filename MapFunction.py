# if you need to modify all the elements in list we can use map function
#map(function, list)

# Example: Squering all Numbers

l=[1,2,3,4,5,6]   #List Of Items
def sqr(n):
    return n**2         #Calculating The Squere root
print(list(map(sqr,l))) #Used The Map Function 



#Using The Lambda Function
k=[1,2,3,4,5,6]  #List Of Items
print(list(map(lambda q : q**3,k))) 