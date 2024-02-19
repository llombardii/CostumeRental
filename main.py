from view import *

def opt():
    opt=open("file2.txt","r")
    print(opt.read())
          
welcome()

continueLoop = True
while continueLoop == True:
    opt()

    while True:
        try:
            a=int(input('Enter an option to continue:  '))
            break
        except:
            print("Invalid option!!")
    
    if a==1 :
        lets_rent()
        import rent
               
    elif a==2:
        lets_return()
        import return_

    elif a==3:
        thanks()
        break
    
    else:
        invalid()
        


