#Get the number of fences
number_of_fences = int(input("Input a number of fence pieces between 1 and 10,000: "))
print(number_of_fences)

#Get the heights of the different fence piecess
input_of_height = str(input("Input the height of the fence pieces: "))
height_of_fences = input_of_height.split()
length_of_height_array = len(height_of_fences)

for x in range(length_of_height_array):
    height_of_fences[x] = int(height_of_fences[x])
print(height_of_fences)


#Get the widths of the different fence pieces
input_of_width = str(input("Input the width of the fence piece: "))
width_of_fences = input_of_width.split()
length_of_width_array = len(width_of_fences)

for x in range(length_of_width_array):
    width_of_fences[x] = int(width_of_fences[x])
print(width_of_fences)

#Calculating the total area
total_area = 0

for fencenumber in range(number_of_fences):
    left_height = height_of_fences[fencenumber]
    right_height =  height_of_fences[fencenumber + 1]
    width = width_of_fences[fencenumber]
    print(left_height, right_height, width)
    if left_height < right_height:
        area_of_fence = (width * left_height) + ((abs((right_height - left_height)) * width) / 2)
    else:
        area_of_fence = (width * right_height) + ((abs((right_height - left_height)) * width) / 2)
    print(area_of_fence)
    total_area += area_of_fence

print(total_area)
