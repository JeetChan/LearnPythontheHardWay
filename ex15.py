from sys import argv
script, filename = argv
txt = open(filename, mode='r', encoding='UTF-8')
print (f"Here's your file :{filename}") 
print (txt.read())
print ("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again, mode='r', encoding='UTF-8')
print (txt_again.read())