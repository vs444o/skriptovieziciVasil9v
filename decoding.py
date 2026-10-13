string = input("Enter RLE: ")

newstr = ''
i = 0
while i < len(string):
    newstr += string[i] * int(string[i+1])
    i += 2 

print(newstr)    