#Temperture converter

#getting Temp in ferenhate

ferenhate=int(input("Enter Temprature in ferenhte"))
#Appling converion formula
celcious=(ferenhate - 32) * 5 / 9
#Using rtoun d the keep the decimle round
print("The tmperure in celcious is " + str(round(celcious, 2)) + "C")
