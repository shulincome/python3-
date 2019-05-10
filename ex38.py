ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that this,let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Frisbee", "corn", "Banana","Girl", "Boy"]

while len(stuff) != 10: 
    next_one = more_stuff.pop()  #pop()
    出现一次，指针就从后往前移动一次
    print(f"Adding: {next_one}")
    stuff.append(next_one)
    print(f"There's {len(stuff)} items now.")

print(f" There we go: {stuff}")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))    #jion()函数用法：将空格加入到各个元素之间
print('love'.join(stuff[3:5]))