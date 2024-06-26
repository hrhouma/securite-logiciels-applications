cipher = input("Enter the text encrypted using Caeser's cipher: ")
original = input("Enter the plain text of the first world/letter: ")

og_len = len(original)
sub_cipher = cipher[:og_len]

for i in range(0, 28):
    temp = ''
    string = original[0:og_len]
    for char in string:
        if char == ' ':
            temp = temp + char
        elif char.isupper():
            temp = temp + chr((ord(char) + i - 65) % 26 + 65)
        else:
            temp = temp+ chr((ord(char) + i - 97) % 26 + 97)
    if (temp == sub_cipher):
        print ("Shift towards right.\nKey= "+str(i))
        break

for i in range(0, 28):
    temp = ''
    string = original[0:og_len]
    for char in string:
        if char == ' ':
            temp = temp + char
        elif char.isupper():
            temp = temp + chr((ord(char) - i - 65) % 26 + 65)
        else:
            temp = temp + chr((ord(char) - i - 97) % 26 + 97)
    if (temp == sub_cipher):
        print("Shift towards left.\nKey= " + str(i))
        break

