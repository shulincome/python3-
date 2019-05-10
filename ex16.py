from sys import argv

script, filename = argv 

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL_C(^C).")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye")
target.truncate()   #对原有文件进行擦出

print("Now I'm going to ask you for three lines.")
#接下来将进行新的文本录入
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1+"\n"+ line2 + "\n"+ line3+ "\n")
    
print("And finally, we close it.")

target.close()
