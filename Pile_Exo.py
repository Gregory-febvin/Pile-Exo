def empiler(value):
    p.append(value)

def depiler():
    return p.pop()

def IsEmpty(Stack):
    return Stack == []

def IsFull(Stack):
    if int(pile_size) == int(len(Stack)):
        return True
    else:
        return False

def Stack_Print(Stack):
    String_Data = ''

    for x in Stack:
        String_Data = "\t" + str(x) + "\t \n" + String_Data

    String_Data = "\n// Pile Data // \n" + String_Data
    return String_Data

def OperationChoice(operation_number):

    if operation_number == '1':
        operator1 = float(input("Enter a number: \n"))
        empiler(operator1)     

    elif operation_number == '2':
        depiler()  

    elif operation_number == '3':
        print(IsEmpty(p)) 

    elif operation_number == '4':
        print(IsFull(p))  
    elif operation_number == '5':
        print(Stack_Print(p))

pile_size = input("Enter a number for the size of the pile: \n")
p = list("") * int(pile_size)

while True:

    print("Selectione une opération :")
    print("1 . Empile")
    print("2 . Depile")
    print("3 . Is Empty")
    print("4 . Is Full")
    print("5 . Stack Print")

    operation_number = input("Entre ton choix(1/2/3/4/5): ")

    if operation_number in ('1', '2', '3', '4', '5'):
        OperationChoice(operation_number)

        next_calculation = input("Something Else? (oui/non): ")
        if next_calculation == "non":
          break
    else:
        print("Entré Invalide")