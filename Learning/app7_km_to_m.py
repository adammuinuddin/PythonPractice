#This program will convert km to miles using functions

def convert(miles):
    return miles * 1.6

m = int(input("Input miles to convert to kilometers: "))
print(m, "miles is equal to", convert(m), "kilometers")