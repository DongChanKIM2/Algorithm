def binarytodecimal(binary):
    for i in range(len(binary)):
        if binary[i] == 1:
            binary[i] = 0
            total = binaryconverter(binary)
            binary_decimal.append(total)
            binary[i] = 1
        elif binary[i] == 0:
            binary[i] = 1
            total = binaryconverter(binary)
            binary_decimal.append(total)
            binary[i] = 0
    return binary_decimal


def trinarytodecimal(trinary):
    for i in range(len(trinary)):
        if trinary[i] == 2:
            trinary[i] = 1
            total = trinaryconverter(trinary)
            trinary_decimal.append(total)
            trinary[i] = 0
            total = trinaryconverter(trinary)
            trinary_decimal.append(total)
            trinary[i] = 2
        elif trinary[i] == 1:
            trinary[i] = 2
            total = trinaryconverter(trinary)
            trinary_decimal.append(total)
            trinary[i] = 0
            total = trinaryconverter(trinary)
            trinary_decimal.append(total)
            trinary[i] = 1
        elif trinary[i] == 0:
            trinary[i] = 1
            total = trinaryconverter(trinary)
            trinary_decimal.append(total)
            trinary[i] = 2
            total = trinaryconverter(trinary)
            trinary_decimal.append(total)
            trinary[i] = 0

    return trinary_decimal


def binaryconverter(binary):
    total = 0
    for i in range(len(binary)-1, -1, -1):
        total += binary[i] * (2 ** (len(binary) - i - 1))
    return total

def trinaryconverter(binary):
    total = 0
    for i in range(len(trinary)-1, -1, -1):
        total += trinary[i] * (3 ** (len(trinary) - i - 1))
    return total


t = int(input())
for tc in range(t):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))
    binary_decimal = []
    trinary_decimal = []
    binarytodecimal(binary)
    trinarytodecimal(trinary)
    for i in binary_decimal:
        if i in trinary_decimal:
            print('#{} {}'.format(tc+1, i))
