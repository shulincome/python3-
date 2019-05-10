from sys import argv 

script, input_file, = argv
#定义函数阅读文本的函数
def print_all(f):
    print(f.read())

#对文件进行倒带,回到最开始
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First leyt's print the whole file:\n")

print_all(current_file)

print("Now let's rewind,kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
