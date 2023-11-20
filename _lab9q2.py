def squared_numbers(filename, outFile):
    line = ""
    file = open(filename, 'r')
    for i in file:
        i *= i
        line += i + '\n'
    file = open(outFile, 'w')
    file.write(line)
    file.close()

def main():
    squared_numbers("numbers.txt", "squaredNumbers.txt")

main()
