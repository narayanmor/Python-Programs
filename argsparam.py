#Allows the functon accept any number arguments all passed values collected into tuple
#which can be accessed or itireted in function

def adder (*num):
      a=0
      for i in  num:
        a+=i
      return a
print(adder(1,2,3,4,4,5,5))

