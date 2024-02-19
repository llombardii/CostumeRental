

def bill2():
    
    print()
    print("====================================================")
    print("                    Bill Details                    ")
    print("====================================================")
    print("Name of Customer: ", name)
    print("Date and time of rent: ", todaysDate)
    print("Total Price: $", totalPrice)
    print("Items Rented are: ",", ".join(rentCostumeNameArray))
    print("----------------------------------------------------")
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|     Rent Details Bill has been generated.     |")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    
    num=str(random.randint(999999999,9999999999))
    bill = open("Rent_"+name+"_"+num+".txt","w")
    bill.write("===============================================\n")
    bill.write("                    Invoice                    \n")
    bill.write("===============================================\n")
    bill.write(" Name of Customer: " + str(name))
    bill.write("\n Date and time of rent: " +str(todaysDate))
    bill.write("\n Total Price: $" + str(totalPrice))
    bill.write("\n Items rented are: " + ", ".join(rentCostumeNameArray))
    bill.write("\n===============================================")
    bill.close()

    

def bill():
    
    print()
    print("====================================================")
    print("                    Bill Details                    ")
    print("====================================================")
    print("Name of Customer: ", name)
    print("Date and time of return: ", todaysDate)
    print("Items returned are: ",", ".join(rentCostumeNameArray))
    print("----------------------------------------------------")
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("|     Return Detail Bill has been generated.     |")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    
    num=str(random.randint(999999999,9999999999))
    bill = open("Return_"+name+"_"+num+".txt","w")
    bill.write("===============================================\n")
    bill.write("                    Invoice                    \n")
    bill.write("===============================================\n")
    bill.write(" Name of Customer: " + str(name))
    bill.write("\n Date and time of return: " +str(todaysDate))
    bill.write("\n Items returned are: " + ", ".join(rentCostumeNameArray))
    bill.write("\n===============================================")
    bill.close()
