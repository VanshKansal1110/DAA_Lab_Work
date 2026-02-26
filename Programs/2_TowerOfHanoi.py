step_count = 0

def toh(n, F, U, T):
    global step_count
    if n > 0:
        toh(n - 1, F, T,U)
        print("Step:-",step_count,"->\t Move From Plate-",F," To Plate-",T,"\n")
        step_count += 1
        toh(n - 1, U,F,T)


num=int()
num=input("Enter the Number of the Plates:-\t")
print( "\n\n\tLet the Plates Are in the \t'A' Stack.\n\tWe need to transfer it to the \t'C' Stack.\n" )
print( "\tWe have the \t'B' Stack \tempty To Use For the Transfer of the plates.\n\nSteps to Follow to Transfer plates from 'A->C:- '\n")

toh(num, 'A', 'B','C');
