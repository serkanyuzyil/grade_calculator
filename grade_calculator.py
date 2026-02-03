while True:

  print("***********************")
  print("Welcome to Grade Calculator")
  print("For calculation press 1 please.")
  print("For list your all grades press 2 please.")
  print("For deleting selected grade press 3 please.")
  print("For quit press 4 please.")
  print("***********************")
  menu_choice = int(input("What do you want to do? (calculate(1)/list(2)/quit(3)):"))
  if menu_choice == 1:
    name_of_lecture = input("What is the name of the lecture?\n")
    midterm = float(input("Midterm Exam:"))
    midterm_weight = float(input("Midterm Weight(like 0.):"))
    final = float(input("Final Exam:"))
    final_weight = float(input("Final Weight (like 0.):"))
    homework = float(input("Homework:"))
    homework_weight = float(input("Homework Weight(like 0.):"))
    
    if (midterm_weight + final_weight + homework_weight) != 1:
      print("Error: The sum of weights must be 100%. Please try again.")
      continue
    elif midterm < 0 or final < 0 or homework < 0:
      print("Error: Scores cannot be negative. Please try again.")
      continue
    elif midterm > 100 or final > 100 or homework > 100:
      print("Error: Scores cannot exceed 100. Please try again.")
      continue
    score = (midterm*midterm_weight + final*final_weight + homework*homework_weight)
    if score >= 95 :
      result = "A1"
    elif score >= 90:
      result = "A2"
    elif score >= 85:
      result = "A3"
    elif score >= 80:
      result = "B1"
    elif score >= 75:
      result = "B2"
    elif score >= 70:
      result = "B3"
    elif score >= 65:
      result = "C1"
    elif score >= 60:
      result = "C2"
    elif score >= 55:
      result = "C3"
    elif score >= 50:
      result = "D"
    else:
      result = "F,you failed the course."
    if score is not None:
      print(f"Your letter grade for {name_of_lecture} is: {result} with a score of {score:.2f}\n") 
      try:
        with open(f"grades.txt","a") as file:
          file.write(f"{name_of_lecture}:{result} with a score of {score:.2f}\n")
          print("Grade saved succesfully.")
      except IOError as e:
        print(f"An error occured while saving the grade: {e}.")
  elif menu_choice ==2:
    try:
      with open(f"grades.txt","r",encoding="UTF-8") as file:
        grades =file.read()
        if not grades:
          print("No grades found.")
        else:
          print("Your Grades:\n",grades)
    except FileNotFoundError:
      print("No grades found. Please calculate and save a grade first.")
    except IOError as e:
      print("An error occured while reading the grades: {e}.")
  elif menu_choice == 3:
    try:
      with open("grades.txt","r",encoding="UTF-8") as file:
        grades = file.readlines()
        if not grades:
          print("NO found grades to delete.")
        else:
          print("Your Grades:")
          for index,grade in enumerate(grades, start=1):
            print(f"{index}. {grade.strip()}")
          delete_index = int(input("Enter the number of the grade you want to delete:"))
          if 1 <= delete_index <= len(grades):
            deleted_grade = grades.pop(delete_index - 1)
            with open("grades.txt","w",encoding="UTF-8") as file:
              file.writelines(grades)
            print(f"Deleted grade: {deleted_grade.strip()}")
          else:
            print("Invalid selection. Please try again.")
    except FileNotFoundError:
      print("No grades found. Please calculate and save a grade first.")
    except IOError as e:
      print(f"An error occureed while deleting the grade:{e}.")                
  elif menu_choice == 4:
    print("Exiting the grade calcualtor. Goodbye!")
    break            

