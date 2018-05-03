# Make new list with square's 1-10 1,4,9,16...
my_list = [i ** 2 for i in range(1, 11)]

# Make a variable to open "output.txt" in write-mode makes a new one if it does not exist
my_file = open("output.txt", "w")

# For every number in the list write the number into the file
# Convert it to string to let write to accept it, + start the next from next row'''
for value in my_list:
  my_file.write(str(value) + "\n")

# Remember to close your files after writing, Otherwise it won't write properly
my_file.close()