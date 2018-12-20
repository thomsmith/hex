#Hex colour converter
#[2018-12-17] Challenge #370 [Easy] UPC check digits /r/dailyprogrammer

#Tom Smith 2018

#get rgb values. while True loops allow the data to be validated

while True:
    RGBa = int(input("Please input first RGB Integer "))
    if RGBa > 255:
        print("The value is out of range, try again")
    elif RGBa is None:
        raise TypeError("Non value")
    else:
        break
while True:
    RGBb = int(input("Please input second RGB Integer "))
    if RGBb > 255:
        print("The value is out of range, try again")
    else:
        break
while True:
    RGBc = int(input("Please input third RGB Integer "))
    if RGBc > 255:
        print("The value is out of range, try again")
    else:
        break

HEXa = hex(RGBa)[2:]
HEXb = hex(RGBb)[2:]
HEXc = hex(RGBc)[2:]

HEXfinal = str(("#" + HEXa + HEXb + HEXc))

print (HEXfinal.upper())
