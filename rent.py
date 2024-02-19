
import datetime
import random
from view import *


       
def display_rent():
    file = open("file.txt","r")
    print("--------------------------------------------------------------")
    print("  ID \tCustome Name   \tCustome Brand  Price($)   Quantity")
    print("--------------------------------------------------------------")
    counterID = 0
    for line in file:
        counterID = counterID + 1
        print(" ", counterID, "\t" + line.replace(",","\t"))
        print("----------------------------------------------------------")
    file.close()


def dictionary_rent():
    file = open("file.txt", "r")
    counterID = 0
    dictionaryCostume = {}
    for line in file: 
        counterID = counterID + 1
        line = line.replace("\n","")
        line = line.split(',')
        dictionaryCostume[counterID] =  line
    return dictionaryCostume
    file.close()

def valid_costume_ID():
    continueLoop=True
    while continueLoop==True:
        try:
            validCostumeID = int(input("Enter the ID of costume you want to rent: "))
            break

        except:
            print("Invalid option!!")
        
    while validCostumeID <= 0 or validCostumeID > len(dictionary_rent()):
        invalid()
        validCostumeID=int(input("\nPlease provide a valid costume ID :"))
        
    return validCostumeID

def quantity_costume(stockQuantity):
    continueLoop=True
    while continueLoop==True:
        try:
            quantityOfCostume = int(input("\nEnter the quantity of costume: "))
            break
        except:
            print("Invalid option!!")
            
    while quantityOfCostume <=0 or quantityOfCostume > stockQuantity:
        if quantityOfCostume <= 0:
            valid_quantity()
            
        else:
            out_of_stock()

        quantityOfCostume = int(input("Enter the quantity: "))
    return quantityOfCostume

def stock_costume(dictionary):
    file = open("file.txt","w")
    for i in dictionary.values():
        line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3])) 
        file.write(line)
        file.write("\n")
    file.close()

def calculate_total_price(dictionary, quantityDetails, costumeID):
    price = float(dictionary[rentCostumeID][2].replace("$",""))
    print("The price of costume: ", price)
    pricePerItem = price * quantityDetails
    return pricePerItem

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

while True:

    display_rent()
    dictionary_rent()
    dictionaryCostume = dictionary_rent()
        #print(dictionaryCostume)

    rentCostumeID = valid_costume_ID()

    rentCostumeNameArray = []

    if int(dictionaryCostume[rentCostumeID][3])> 0:
        
        available()

        quantityOfCostume = quantity_costume(int(dictionaryCostume[rentCostumeID][3]))
        dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) - quantityOfCostume

        print(dictionaryCostume)

        name = input("Enter the name of customer: ")
        todaysDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        rentCostumeNameArray.append(dictionaryCostume[rentCostumeID][0])

        stock_costume(dictionaryCostume)

        totalPrice = calculate_total_price(dictionaryCostume,quantityOfCostume,rentCostumeID)
            
        print("===================================================")
        print("Have the costumer rented another costume as well??")
        continueRent = input("Please enter 'y' if another costume has been rented else provide any other value: ").lower()

        loop = True
        while loop == True:
            if continueRent == "y":
                display_rent()
                dictionaryCostume = dictionary_rent()
                rentCostumeID = valid_costume_ID()

                if int(dictionaryCostume[rentCostumeID][3]) > 0:
                    
                        quantityOfCostume = quantity_costume(int(dictionaryCostume[rentCostumeID][3]))
                        dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) - quantityOfCostume

                        print(dictionaryCostume)
                        rentCostumeNameArray.append(dictionaryCostume[rentCostumeID][0])

                        stock_costume(dictionaryCostume)

                        totalPrice = calculate_total_price(dictionaryCostume,quantityOfCostume,rentCostumeID) + totalPrice
                        print("Have the costumer rented another costume as well??")
                        continueRent = input("Please enter 'y' if another costume has been rented else provide any other value: ").lower()
                        if continueRent == "y":
                            display_rent()
                            dictionaryCostume = dictionary_rent()
                            rentCostumeID = valid_costume_ID()
                        else:
                            bill2()
            else:
                
                bill2()
                loop = False
            loop= False
            thanks()
        break

                    

    
        
