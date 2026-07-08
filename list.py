#List
list1=[1,2,3,4,5,6]
print (type(list))
print (list)

#Empty list
list2=[]
print(type(list2))

#orderd list-  (means list is always in sequntial order)
list3=[1,2,3,4,5,6]
print(list3[4]) #Index Start with 0
print(list3[-1]) #Index end with -1

#Mutable List - measns we can update any element in the list by assigning new value using index
list1=[1,2,3,4,5,6]
list1[1]=4 # Adding New values using index 
print(list1) #printing new values


#hetrogenios -  list (means any type of values acceptable in list like int,string,float)
list4=[1,2,4,3,12.5] #list having string values as well as float

#------------------------LiST METHODS-------------------------------#

#Append() :-    is used  to add values in the end of the list
list4.append(8)
print(list4)

#Insert() :-    Insert an element at specific index
list4.insert(2,10)
print(list4)

#Remove():-     Remove the values from list
list4.remove(2)
print(list4)

#pop() -        pop remove the element it removes that last element
list4.pop()
print(list4)

#sort() -       sort is used to sort the list is ascending order if in a list string is there it will through error
list4.sort()
print(list4)

#reverse() -    reverse method is used to reverse the list
list4.reverse()
print(list4)

#Extend() -     method is used to add elements from another list
l=[1,2,3,4,4]
l1=[5,6,7,8,9]

l.extend(l1)
print(l)

#Count()  -     COUNT METHOD USED TO COUNT THE OCCURANCE OF THE VALUES
l.count(4)
print(l)

#iterating Using Loop.
for i in l:
    print(i)




