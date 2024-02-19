import TaxCalc
def interface():
    uInput=1
    total=0
    while uInput!=0:
        uInput=int(input("ENTER ITEMS (ENTER 0 TO END)"))
        total=total+uInput
        print("Cost of item:",uInput,"\nTotal bill",total)
    print("your total for this cart is",total)
    TaxCalc.calculate(total=total)