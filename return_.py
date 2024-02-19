import random
import datetime
from bill import *

def invalid_message():
    print("\nIvalid input")
    print("\nPlese select the value as per the provied options\n")

         
def display_Return():
    file = open("file.txt","r")
    print("--------------------------------------------------------------")
    print("\tID \tCustome Name   \tCustome Brand  Price($)   Quantity")
    print("--------------------------------------------------------------")
    counterID = 0
    for line in file:
        counterID = counterID + 1
        print("\t", counterID, "\t" + line.replace(",","\t"))
        print("----------------------------------------------------------")
    file.close()



def dictionary_Return():
    file = open("file.txt", "r")
    counterID = 0
    dictionaryCostume = {}
    for line in file: 
        counterID = counterID + 1
        line = line.replace("\n","")
        line = line.split(',')

        dictionaryCostume[counterID] =  line

    #print(dictionaryCostume)
    return dictionaryCostume
    file.close()

def valid_costume_ID():
    continueLoop=True
    while continueLoop==True:
        try:
            validCostumeID = int(input("Enter the ID of costume you want to return: "))
            break
        except:
            print("Invalid option!!")
        
    while validCostumeID <= 0 or validCostumeID > len(dictionary_Return()):
        valid2=int(input("\nPlease provide a valid costume ID :"))
    return validCostumeID

def quantity_costume(stockQuantity):
    continueLoop=True
    while continueLoop==True:
        try:
            quantityOfCostume = int(input("\nEnter the quantity of costume: "))
            break
        except:
            print("Invalid option!!")
        

    while quantityOfCostume <=0 :
        if quantityOfCostume <= 0:
            valid_quantity()
        quantityOfCostume = int(input("Enter the quantity: "))
    return quantityOfCostume

def stock_costume(dictionary):
    file = open("file.txt","w")
    for i in dictionary.values():
        line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3])) 
        file.write(line)
        file.write("\n")
    file.close()
    

        



def bill():
    
    print()
    print("====================================================")
    print("                    Bill Details                    ")
    print("====================================================")
    print("Name of Customer: ", name)
    print("Date and time of return: ", todaysDate)
    print("Items returned are: ",", ".join(ReturnCostumeNameArray))
    print("Total fine: $",finecharged)
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
    bill.write("\n Items returned are: " + ", ".join(ReturnCostumeNameArray))
    bill.write("\nTotal fine: $"+str(finecharged))
    bill.write("\n===============================================")
    bill.close()




while True: 
    display_Return()
    dictionary_Return()

    dictionaryCostume = dictionary_Return()
        #print(dictionaryCostume)

    ReturnCostumeID = valid_costume_ID()

    ReturnCostumeNameArray = []

    if int(dictionaryCostume[ReturnCostumeID][3]) > 0:

        quantityOfCostume = quantity_costume(int(dictionaryCostume[ReturnCostumeID][3]))
        dictionaryCostume[ReturnCostumeID][3] = int(dictionaryCostume[ReturnCostumeID][3]) + quantityOfCostume

        print(dictionaryCostume)

        finecharged=0
        continueLoop=True
        while continueLoop==True:
            try:
                day = int(input("\n For how many days have you rented the costume? "))
                break
            except:
                print("Please enter the day in number.")
       
        if day <=7:
            days_of_fine= 0
            
        elif day >7:
            days_of_fine= day - 7
            finecharged += (days_of_fine*10)
            print("The total fine charged is: $",finecharged)
    
        
        name = input("Enter the name of customer: ")
        todaysDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ReturnCostumeNameArray.append(dictionaryCostume[ReturnCostumeID][0])

        stock_costume(dictionaryCostume)
            
        print("===================================================")
        print("Do you wannt to return any other costumes??")
        continueReturn = input("Please enter 'y' if another costume has been Returned else provide any other value: ").lower()
        
        
        while True:
            if continueReturn == "y":
                print()
                display_Return()
                dictionaryCostume = dictionary_Return()
                ReturnCostumeID = valid_costume_ID()

                if int(dictionaryCostume[ReturnCostumeID][3]) > 0:
                    

                    quantityOfCostume = quantity_costume(int(dictionaryCostume[ReturnCostumeID][3]))
                    dictionaryCostume[ReturnCostumeID][3] = int(dictionaryCostume[ReturnCostumeID][3]) + quantityOfCostume

                    print(dictionaryCostume)
                    
                    finecharged=0
                    continueLoop=True
                    while continueLoop==True:
                        try:
                            day = int(input("\n For how many days have you rented the costume? "))
                            break
                        except:
                            print("Please enter the day in number.")
       
                    if day <=7:
                        days_of_fine= 0
            
                    elif day >7:
                        days_of_fine= day - 7
                        finecharged += (days_of_fine*10)
                        print("The total fine charged is: $",finecharged)
                    
                    ReturnCostumeNameArray.append(dictionaryCostume[ReturnCostumeID][0])

                    stock_costume(dictionaryCostume)

                    print("==================================================")
                    print("Have the costumer returned another costume as well??")
                    continueReturn = input("Please enter 'y' if another costume has been Returned else provide any other value: ").lower()
            else:
                bill()
                break
                    

            
               
                    


                
            
                    

   
        
