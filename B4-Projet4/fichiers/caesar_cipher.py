string = input("Enter string: ")
shift = input("Enter shift number(Prefix 'L' for left shift and 'R' for right shift): ")

cipher = ''
if (shift[0].lower()== 'r'):
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + int(shift[1:]) - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + int(shift[1:]) - 97) % 26 + 97)
        print (char + '->' + cipher[-1] )

elif (shift[0].lower()== 'l'):
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - int(shift[1:]) - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - int(shift[1:]) - 97) % 26 + 97)
        print(char + '->' + cipher[-1])

else:
    print ("Invalid shift")

print ('*************')
print('Original text: '+ string)
print('Encrypted text: '+cipher)