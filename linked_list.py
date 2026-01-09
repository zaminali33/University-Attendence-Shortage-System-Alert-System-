class Student:
    def __init__(self, id, name, total_classes, attended_classes):
        self.id = id
        self.name = name
        self.total = total_classes
        self.attended = attended_classes
        self.next = None  # Linked List Pointer

    def attendance_percentage(self):
        return (self.attended / self.total) * 100

class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, id, name, total, attended):
        new_student = Student(id, name, total, attended)
        if self.head is None:
            self.head = new_student
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_student

    def show_all_students(self):
        temp = self.head
        print("
================ ALL STUDENTS DATA ================
")
        count = 1
        while temp:
            print(f"Student {count}")
            print(f"ID: {temp.id}")
            print(f"Name: {temp.name}")
            print(f"Total Classes: {temp.total}")
            print(f"Attended Classes: {temp.attended}")
            print(f"Attendance: {temp.attendance_percentage():.2f}%")
            print("--------------------------------------------------")
            count += 1
            temp = temp.next

    def show_shortage(self):
        temp = self.head
        shortage_found = False
        print("
=============== SHORTAGE STUDENTS (<75%) ===============
")
        while temp:
            percentage = temp.attendance_percentage()
            if percentage < 75:
                shortage_found = True
                print(f"ID: {temp.id}, Name: {temp.name}, Attendance: {percentage:.2f}%")
            temp = temp.next
        if not shortage_found:
            print("No student is in shortage.")


# -------- Main Program --------
students = StudentList()
for i in range(1, 11):
    id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    total = int(input("Enter Total Classes: "))
    attended = int(input("Enter Attended Classes: "))
    students.add_student(id, name, total, attended)

students.show_all_students()
students.show_shortage()
