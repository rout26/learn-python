from sys import argv

from os.path import exists

script, from_file, to_file = argv

#read the file

in_file = open(from_file)
in_data = in_file.rewad()

print(f'The input file is {len(in_data)} bytes long. ')
print(f"Does the output file exist? {exists(to_file)}") #Boolian to check if file exists
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("File copied.")

in_file.close()
out_file.close()
