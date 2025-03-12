# import os
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the text file
file_path = os.path.join(script_dir, 'file.txt')

file = open(file_path,'r')
# content = file.read() #reads the whole file as one strig
content= [line.strip() for line in file.readlines()]   #list comprehension and strip newline and white spaces form the extremes of the strings
# content= file.read()  if this is run two times the cursor set at the eof and doesnot get new data to read
file.close()
print(type(content))
print(content)