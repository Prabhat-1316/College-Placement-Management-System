import csv

class CollegePlacementApp:
    def __init__(self, database_file='students.csv'):
        self.database_file = database_file
        self.students = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.database_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                self.students = [dict(zip(['Name', 'Roll Number', 'Branch', 'Placed'], row)) for row in reader]
        except FileNotFoundError:
            # Create an empty file if it doesn't exist
            open(self.database_file, 'w').close()

    def save_data(self):
        with open(self.database_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Roll Number', 'Branch', 'Placed'])
            for student in self.students:
                writer.writerow([student['Name'], student['Roll Number'], student['Branch'], student['Placed']])

    def display_menu(self):
        print("1. View all students")
        print("2. Add a new student")
        print("3. Update student placement status")
        print("4. Exit")

    def view_all_students(self):
        for student in self.students:
            print(f"{student['Roll Number']} - {student['Name']} ({student['Branch']}) - Placed: {student['Placed']}")

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter student roll number: ")
        branch = input("Enter student branch: ")
        placed = input("Is the student placed? (True/False): ").capitalize()

        new_student = {
            'Name': name,
            'Roll Number': roll_number,
            'Branch': branch,
            'Placed': placed
        }

        self.students.append(new_student)
        self.save_data()
        print("Student added successfully!")

    def update_placement_status(self):
        roll_number = input("Enter the roll number of the student: ")
        student = next((s for s in self.students if s['Roll Number'] == roll_number), None)

        if student:
            new_placement_status = input("Update placement status (True/False): ").capitalize()
            student['Placed'] = new_placement_status
            self.save_data()
            print("Placement status updated successfully!")
        else:
            print("Student not found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_all_students()
            elif choice == '2':
                self.add_student()
            elif choice == '3':
                self.update_placement_status()
            elif choice == '4':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    app = CollegePlacementApp()
    app.run()