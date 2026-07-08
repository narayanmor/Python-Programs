#CREATING TUPLE

tuple=(1.2,3,4)     
print(tuple)            #PRINTING TUPLE

print(type(tuple))      #TYPE SHOWS THE TYPE EX. <class 'tuple'>
print(tuple[0])         #PRINT THE ELEMENT IS HAVING 0 INDEX (INDEXING START WITH 0 AND END WITH -1)

#WE CAN NOT ADD ITEMS TO A TUPLE FIRST NEED TO CONVERT INTO LIST .
tuple=(12.5,3,4)
TUP1=(5,4)              #COMA IS REQUIRED FOR SINGLE TUPLE WITHOUT COMA IS TREATED AS SINGLE JUST NUMBER INSIDE
                        #BRACKETS WITH COMA PYTHON IS RECOUGNIZED IT AS AN ORDERD IMMUTABLE SEQUENCE
tuple=tuple + TUP1      #HARE NEW TUPLE IS ADDING WITH EXISTING TUPLE
print(tuple)            #PRINTING THE TUPLE  

#tuple.remove()         #WE CAN NOT REMOVE ELEMENT FROM TUPLE AS SHOWING ERROR:(AttributeError: 'tuple' object has no attribute 'remove')

#DEL

#del TUP1                #DEL IS USED TO DELETE TUPLE 
#print(TUP1)             # PRINTING THE TUPLE VERIFY DELETED OR NOT (NameError: name 'TUP1' is not defined)

#COUNT()

tuple.count(4)
print(tuple)

tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
#li = [1, 2, 4, 5, 6]
#print(tuple(li))

# Using Built-in Function
#tup = tuple('Geeks')
#print(tup)

#SLICING 
#tuple=(12.5, 3, 4, 5, 4)
print(tuple[1:4])  #IT WILLPRINT NUMBER BETWEEN INDEX 1 TO 4 EX:- (3, 4, 5)

