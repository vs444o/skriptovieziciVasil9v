
string = input("Enter string: ")
before = string[0]
current = 0
newstr = ''

for i in range(len(string)):
    if string[i] == before:
        current += 1
    else:
        newstr += before
        newstr += str(current)

        before = string[i]
        current = 1

newstr += before
newstr += str(current)

print(newstr)
