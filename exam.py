def stat():
    data = []
    count = 0
    grade1s = 0
    grade2s = 0
    grade3s = 0
    grade4s = 0
    grade5s = 0
    grade0s = 0

    eb = []
    a = 0
    grade5 = "  5: "
    grade4 = "  4: "
    grade3 = "  3: "
    grade2 = "  2: "
    grade1 = "  1: "
    grade0 = "  0: "

    while True:
        input1 = input("Enter exam points (or press Enter to exit): ")
        if input1 == "":
            break
        
        input2 = int(input("Enter exercises completed: "))
        points = int(input1)
        
        if input2 >= 90:
            points += 9
        elif input2 >= 80:
            points += 8
        elif input2 >= 70:
            points += 7
        elif input2 >= 60:
            points += 6
        elif input2 >= 50:
            points += 5
        elif input2 >= 40:
            points += 4
        elif input2 >= 30:
            points += 3
        elif input2 >= 20:
            points += 2
        elif input2 > 100:
            return False
        
        count += 1
        a += 1
        data.append((input1, input2, points))
        eb.append(points)
        
        result = "Total points: " + str(points) + " (Exam points: " + str(input1) + ", Exercises completed: " + str(input2) + ")"
        print(result)
    
    total_points = sum(eb)
    averagee = total_points / count
    
    print("Points average:", averagee)
    print("Data collected:")
    
    for entry in data:
        print("Exam points:", entry[0], "| Exercises completed:", entry[1], "| Total points:", entry[2])
    
    print("Total entries:", count)
    print("Total points:", total_points)
    
    for points in eb:
        if points >= 28:
            grade5s += 1
        elif points >= 24:
            grade4s += 1
        elif points >= 21:
            grade3s += 1
        elif points >= 18:
            grade2s += 1
        elif points >= 15:
            grade1s += 1
        else:
            grade0s += 1

    pass_percentage = 100 * (grade1s + grade2s + grade3s + grade4s + grade5s) / count

    print("Statistics:")
    print(f"Points average: {averagee:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}%")
    print("Grade distribution:")
    print(grade5 + grade5s * "*")
    print(grade4 + grade4s * "*")
    print(grade3 + grade3s * "*")
    print(grade2 + grade2s * "*")
    print(grade1 + grade1s * "*")
    print(grade0 + grade0s * "*")

stat()
