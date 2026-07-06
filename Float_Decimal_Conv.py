
#Simple Tip calculator

#Getting total bill and percentage
bill=float(input("Please enter your Total bill amount"))
tip_percentage=float(input("Please enter the tip percentge (e.g ,15,20,30): "))


#Calculating The tip
tip_ammount=bill *(tip_percentage/100) 
total_bill=bill + tip_ammount

#Printing The Total ammount and Tip ammount
print(f"Your tip ammount is {tip_ammount}")
print(f"Your total bills comes to {total_bill}")
