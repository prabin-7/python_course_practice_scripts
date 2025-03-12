import os
#get dir of the script
what = os.path.abspath(__file__)
print(what)
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
file_name = 'file.txt'
file_path = os.path.join(script_dir,file_name)
print(file_path)

# with open(file_path,'a+') as file1:
#     file1.write('hello this is new written file\n')
#     file1.seek(0)
#     contents = file1.readlines()
# print(contents)