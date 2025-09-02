if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Extract unique grades and sort them
    unique_grades = sorted({score for name, score in students})
    
    # Get the second lowest grade
    second_lowest = unique_grades[1]
    
    # Find all students with the second lowest grade
    second_lowest_students = [name for name, score in students if score == second_lowest]
    
    # Sort names alphabetically and print
    for name in sorted(second_lowest_students):
        print([name],"these the second lowest grade in the list")
