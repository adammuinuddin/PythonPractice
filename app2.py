#take name of file and only output the extension
file_input = input("Type the name of your file with the extension: ")
file_type = file_input.split(".")
num_of_words = len(file_type)
#for word in file_type(0, 2):
    #print(word)

for x in range(num_of_words):
    if x == 1:
        print(file_type[x])
    if x == 4:
        print(file_type[x])
