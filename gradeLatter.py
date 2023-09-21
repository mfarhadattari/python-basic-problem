def gradeLatter(gradePoint):
    if(gradePoint == 5):
        return "A+"
    elif(gradePoint >= 4):
        return "A"
    elif(gradePoint >= 3.50):
        return "A-"
    elif(gradePoint >= 3):
        return "B"
    elif(gradePoint >= 2):
        return "C"
    elif(gradePoint >= 1):
        return "D"
    else:
        return "F"

print(gradeLatter(4.5))