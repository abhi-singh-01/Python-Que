## Create an empty dictionary to store employee details
#employee = {}

# Add employee details (key, value pairs)
#employee["name"] = "Alice"
#employee["department"] = "Engineering"
#employee["salary"] = 80000
#employee["experience"] = 5

# Print employee details using a loop
#print("Employee Details:")
#for key, value in employee.items():
 # print(f"{key.capitalize()}: {value}")#
 
 
 
 
 
 
 
 
 
 # Initialize an empty dictionary to store employee details
employees = {}

# Function to add an employee to the dictionary
def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))
    
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'position': position,
        'salary': salary
    }

# Take input from the user to add multiple employees
num_employees = int(input("How many employees do you want to add? "))
for _ in range(num_employees):
    add_employee()

# Display the values with respect to each key
for emp_id, details in employees.items():
    print(f"\nEmployee ID: {emp_id}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")

  
