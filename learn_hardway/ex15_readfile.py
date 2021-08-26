
# Python program to Read a file 

from sys import argv

script, filename = argv
txt = open(filename) #create a file object
print(f"Here's your file {filename}:") #print the file name
print(txt.read()) #read the file object "txt" and print it to terminal

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())