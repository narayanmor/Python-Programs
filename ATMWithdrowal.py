Ballance=int(input("Enter Amount Ballance"))
Amount=int(input("Enter Withdrawl Amount"))

if Amount % 100== 0:
    if Amount<=Ballance:
        Ballance=Ballance-Amount
        print("Transaction Successfull")

        print("Remaining Transaction" , + Ballance)

    else:
        print("Transaction Failed.....!")
        print("Insufficient Ballance")
else:
         print ("Withdrawl ammount should be multiple of 100")