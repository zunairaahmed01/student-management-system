import json
import os

filename = 'Comsats_management.json'

def load_file():
    # Create the file if it doesn't exist, then return an empty dict
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({}, f, indent=4)
        return {}
    # Otherwise, load and return existing data
    else:
        with open(filename, 'r') as f:
            return json.load(f)
            
def save_data(data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"{len(data)} student record(s) saved successfully.")


def input_data():
    print("---------- Welcome to the Comsats Page ------------")
    print("---------- Fill The Form -------------")
    name = input("Enter your full name: ").strip()
    father_name = input("Enter your father's name: ").strip()
    id_card = int(input("Enter your ID card no.: "))
    age = int(input("Enter your age: "))
    mobile = input("Enter your mobile no.: ").strip()
    roll_number = input("Enter your roll number: ").strip()
    department = input("Enter your department: ").strip()

    info = {
        "Student Name": name,
        "Father Name": father_name,
        "Age": age,
        "Mobile Number": mobile,
        "Roll Number": roll_number,
        "Department": department
    }
    return id_card, info
def main():
    while True:
        print("""
                 1. Check Student List
                 2. Add New Student Data
                 3. Check Spacific Student With ID_Card
                 4. Delete SpacifiC Student Through ID_Card
                 5. Exits
                 -----------------------------""")
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 5.")
            continue
        
        student=load_file()
        
        if choice == 1:
            if not student:
                print("No Student Data Availabel.")
            else :
                for id , info in student.items():
                    print(f"Id Card : {id}")
                    for key ,value in info.items():
                        print(f"{key} : {value}")
                    print("-------------------------")
        elif choice == 2:
            id_card, info = input_data()
            student[id_card] = info
            save_data(student)
        
        elif choice == 3:
                students = load_file()
                # print("DEBUG: loaded IDs =", list(students.keys()))   # ← add this
                search_id = input("Enter ID Card number to search: ").strip()
                if search_id in students:
                    # print(f"Data for ID {search_id}:")
                    for key, value in students[search_id].items():
                        print(f"  {key}: {value}")
                else:
                    print("Student not found.")

        elif choice == 4:
            students = load_file()
            search_id = input("Enter ID Card number to Delete : ").strip()
            if search_id in students:
                    del student[search_id]
                    save_data(student)
                    print("Student deleted successfully.")
            else:
                    print("Student not found.")
            
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")
    

if __name__ == '__main__':
    main()
