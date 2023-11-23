import re

def grade_assignment(file_to_be_read) -> str:   
    with open(file_to_be_read, "r") as file1:
        content = file1.readlines()

    for line in content:

        match = re.match(" (\d+)", line)

        if match:
            num = int(match.group(1))

            if 0 <= num <= 10:
                grade = "F"

            elif 11 <= num <= 20:
                grade = "D"

            elif 21 <= num <= 30:
                grade = "C"

            elif 31 <= num <= 40:
                grade = "B"

            elif 41 <= num <= 50:
                grade = "A"

            else:
                grade = "Not a valid score"
        else:
            continue
        
        return grade

    return "Invalid file"