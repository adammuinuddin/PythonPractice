#Get the number of fences
number_of_fences = int(input("Input a number of fence pieces between 1 and 10,000: "))
if number_of_fences > 10000:
    print("Can not complete calculation due to an error")
    quit()

print(number_of_fences)

#Get the heights of the different fence piecess
input_of_height = str(input("Input the height of the fence pieces: "))
height_of_fences = input_of_height.split()
length_of_height_array = len(height_of_fences)

for x in range(length_of_height_array):
    height_of_fences[x] = int(height_of_fences[x])
print(height_of_fences)

if length_of_height_array != number_of_fences +1:
    print("Can not complete calculation due to error")
    quit()

#Get the widths of the different fence pieces
input_of_width = str(input("Input the width of the fence piece: "))
width_of_fences = input_of_width.split()
length_of_width_array = len(width_of_fences)

for x in range(length_of_width_array):
    width_of_fences[x] = int(width_of_fences[x])
print(width_of_fences)

if length_of_width_array != number_of_fences:
    print("Can not complete calculation due to an error")
    quit()

#Calculating the total area
total_area = 0

for fencenumber in range(number_of_fences):
    left_height = height_of_fences[fencenumber]
    right_height =  height_of_fences[fencenumber + 1]
    width = width_of_fences[fencenumber]
    #If the left height is shorter than the right height
    if left_height < right_height:
        area_of_fence = (width * left_height) + ((abs((right_height - left_height)) * width) / 2)
    #If the left height is taller than the right
    else:
        area_of_fence = (width * right_height) + ((abs((right_height - left_height)) * width) / 2)
    total_area += area_of_fence


print("The total area of the fence is", total_area)