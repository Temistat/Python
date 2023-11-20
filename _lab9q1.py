def consecutive_numbers(filename, n):
    line = ""
    file = open(filename, 'w')
    for i in range(1, n + 1):
        line += str(i) + '\n'
    file.write(line)
    file.close()
    
    
def main():
    consecutive_numbers("numbers.txt", 5) 

main()



