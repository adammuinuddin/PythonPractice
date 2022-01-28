#This program is a bmi calculator
name1 = "Adam"
height_m1 = 1.75
weight_kg1 = 69

name2 = "Adam's friend"
height_m2 = 2
weight_kg2 = 100

name3 = "Adam's friend 2"
height_m3 = 1.5
weight_kg3 = 500

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m **2)
    print("bmi: ")
    print(bmi)
    if bmi < 25: 
        return name + " is not overweight"
    elif bmi == 25:
        return name + " is average"
    else:
        return name + " is overweight" 

result1 = bmi_calculator (name1, height_m1, weight_kg1)
result2 = bmi_calculator (name2, height_m2, weight_kg2)
result3 = bmi_calculator (name3, height_m3, weight_kg3)
print (result1, "\n",result2, "\n",result3)

