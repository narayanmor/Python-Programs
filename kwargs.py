#it help to accept any number of arguments all arguments collected into dictionary

def namimg(**kwargs):
    for key,val in kwargs.items():
         
         print(key,val)
namimg(name="narayan",age=27)