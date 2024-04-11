#Binary to hexadecimal

def Bin_to_hex(bin):
    l = len(bin)
    if l % 4 == 1:
        bin = '000' + bin
    elif l % 4 == 2:
        bin = '00' + bin
    elif l % 4 == 3:
        bin = '0' + bin

    fin = ''
    l = len(bin)
    s = ''
    for i in range(l):
        s = s + bin[i]
        if len(s) == 4:
            if s == '0000':
                fin = fin + '0'
            elif s == '0001':
                fin = fin + '1'
            elif s == '0010':
                fin = fin + '2'
            elif s == '0011':
                fin = fin + '3'
            elif s == '0100':
                fin = fin + '4'
            elif s == '0101':
                fin = fin + '5'
            elif s == '0110':
                fin = fin + '6'
            elif s == '0111':
                fin = fin + '7'
            elif s == '1000':
                fin = fin + '8'
            elif s == '1001':
                fin = fin + '9'
            elif s == '1010':
                fin = fin + 'A'
            elif s == '1011':
                fin = fin + 'B'
            elif s == '1100':
                fin = fin + 'C'
            elif s == '1101':
                fin = fin + 'D'
            elif s == '1110':
                fin = fin + 'E'
            elif s == '1111':
                fin = fin + 'F'
            else:
                print('Invalid Input')
                break
            s = ''

    print(fin) 


bin = str(input("Enter the Binary number : "))
Bin_to_hex(bin)

#Hexadecimal to Binary

def Hex_to_bin(x):
    fin = ''
    for i in x:
        if i == '0':
            fin = fin + '0000'
        elif i == '1':
            fin = fin + '0001'
        elif i == '2':
            fin = fin + '0010'
        elif i == '3':
            fin = fin + '0011'
        elif i == '4':
            fin = fin + '0100'
        elif i == '5':
            fin = fin + '0101'
        elif i == '6':
            fin = fin + '0110'
        elif i == '7':
            fin = fin + '0111'
        elif i == '8':
            fin = fin + '1000'
        elif i == '9':
            fin = fin + '1001'
        elif i == 'A':
            fin = fin + '1010'
        elif i == 'B':
            fin = fin + '1011'
        elif i == 'C':
            fin = fin + '1100'
        elif i == 'D':
            fin = fin + '1101'
        elif i == 'E':
            fin = fin + '1110'
        elif i == 'F':
            fin = fin + '1111'
        else:
            print('Enter A Valid number : ')

    print(fin)


x = str(input("Enter the Hex Number : "))
Hex_to_bin(x)
