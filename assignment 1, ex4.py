grade = int(input("Enter your numeric grade: "))
if (grade >= 90):
  if (grade >= 97):
    letter_grade = "A+"
  elif (grade >= 94):
    letter_grade = "A"
  else:
    letter_grade = "A-"
elif (grade >= 80):
  if (grade >= 87):
    letter_grade = "B+"
  elif (grade >= 84):
    letter_grade = "B"
  else:
    letter_grade = "B-"
elif (grade >= 70):
  if (grade >= 77):
    letter_grade = "C+"
  elif (grade >= 74):
    letter_grade = "C"
  else:
    letter_grade = "C-"
elif (grade >= 60):
  if (grade >= 67):
    letter_grade = "D+"
  elif (grade >= 64):
    letter_grade = "D"
  else:
    letter_grade = "D-"
else:
  letter_grade = "F"

print(grade, " is equivalent to ", letter_grade)