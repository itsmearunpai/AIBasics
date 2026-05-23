from colorama import Fore, Style, init

#initialize colorama
init(autoreset=True)

course_catalog = {
    "Python Programming": {"trainer": "Alice", "hours": "40","price": 200},
    "Data Science": {"trainer": "Bob", "hours": "50", "price": 250},
    "Machine Learning": {"trainer": "Charlie", "hours": "60", "price": 300},
    "SAP BTP": {"trainer": "David", "hours": "45", "price": 220},
    "SAP Fiori": {"trainer": "Eve", "hours": "30", "price": 150}
}

selected_courses = []

print(Fore.GREEN + "Welcome to the Course Selection System!")

#Infinite loop to get the course name from the user till exits
while True:
    course_name = input("Enter the course name (or 'exit' to quit): ").strip().upper()  # Convert input to uppercase for case-insensitive comparison

    if course_name.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    if course_name in course_catalog:
        selected_courses.append(course_name)
        print(f"Course '{course_name}' added to your selection.")
    else:
        print(f"Course '{course_name}' not found. Please try again.")

#Display the selected courses and their total hours and price
# print("\n You have selected the following courses:")
total_hours = 0           
total_price = 0

for idx,course in enumerate(selected_courses, start=0):
    print(Fore.YELLOW + f"\nCourse {course[0]}: {course[1]}")
    print(course)
    course_info = course_catalog[course]
    print(f"{idx}. {course} - Trainer: {course_info['trainer']}, Hours: {course_info['hours']}, Price: ${course_info['price']}")
    total_hours += int(course_info['hours'])
    total_price += int(course_info['price'])

print(f"\nTotal Hours: {total_hours}")
print(f"Total Price: ${total_price}")