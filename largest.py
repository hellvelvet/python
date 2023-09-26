

def largest(file1):
    with open(file1) as file:
        a = []
 
        for line in file:
            a.append(int(line))
        a.sort()
        print(a[-1])

largest("numbers.txt")

