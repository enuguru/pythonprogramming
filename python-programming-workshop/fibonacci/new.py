# write a python script to create a new file and write some text to it
with open('new_file.txt', 'w') as file:
    file.write('Hello, this is a new file created by Python!')
# print the contents of the file to verify
with open('new_file.txt', 'r') as file:
    content = file.read()
    print(content)
# check if the file exists and print a message
