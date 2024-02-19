def calculate(total):
    taxRate=0.06
    taxTotal=total*taxRate
    taxTotal=round(taxTotal,2)
    print("Sales tax:",taxTotal)
    fullBill=taxTotal+total
    print("Total after tax:",fullBill)