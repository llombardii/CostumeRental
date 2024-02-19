costumec={}
def display():
    count=0
    print("-------------------------------------------------")
    print("Costume_ID \tName  \tBrand \tPrice \tQuantity")
    print("-------------------------------------------------")

    file=open("file.txt","r")
    
    costume= file.read()
    costume= costume.split("\n")

    while("" in costume):
        costume.remove("")

    for i in range(len(costume)):
        if costume[i] != []:
            count=count+1
            costumec[count]= costume[i].split(",")

    for key,value in costumec.items():
        print(key,end="\t")
        for i in value:
            print(i,end="\t")
        print("\n")
    print("------------------------------------------------")

def validate(c):
    count=c
    costume_id= int(input("Enter the costume ID"))
    if costume_id > 0 and costume_id<= count:
        print("Ready to rent a costume.")
        Qty= int(input("Enter the quantity of the costume."))
        select_costume=costumec[costume_id]
        if Qty <= int(select_costume[3]):
            print("The quantity is available")
            update_Qty= int(select_costume[3]-Qty)
            select_costume[3]=str(update_Qty)
        else:
            print("Selected quantity is greater than available quantity")
    else:
        print("INVALID INPUT")

               
                            
                
