#----------- Person ---------- 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#----------- Student ----------           
class Student(Person):
    count = 0
    def __init__(self, name, age, marks = None):
        super().__init__(name, age)
        if marks is None:
            self.marks = []
        else:
            self.marks = marks
        Student.count += 1
         
    def get_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
    def __str__(self):
        return f"{self.name}, {self.age}, {self.marks}"
    
    @classmethod  
    def from_string(cls, data):
        name, age, marks, = data.split(',')
        marks = eval(marks)
        return cls(name, int(age), marks)

#----------- Teacher ----------     
class Teacher(Person):
    def __init__(self, name, age, subject):  
        super().__init__(name, age)
        self.subject = subject
        
    def __str__(self):
        return f"{self.name}, {self.age}, {self.subject}"
    
    @classmethod   
    def from_string(cls, data):
        name, age, subject = data.split(',')
        return cls(name, int(age), subject)
        
#----------- School ---------- 
class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        
    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully")
    
    def show_student(self):
        if not self.students:
            print("NO satudent found")
            return
        for student in self.students:
            print(student)
            
        
    def add_teachers(self, teacher):
        self.teachers.append(teacher)
        print("Teacher added successfully")
        
    def show_techear(self):
        if not self.teachers:
            print("NO techear found")
            return
        for teacher in self.teachers:
            print(teacher)
        
    def remove_student(self, student):
        self.students.remove(student)
        print("Student remove successfully")
        
    
    
# file handling
        
    def save_data(self):
        try:
            
            with open('school_data.txt', 'w') as file:
                file.write("STUDENT\n")
                for s in self.students:
                    file.write(str(s) + '\n')
                    
                file.write("TEACHER\n")
                for t in self.teachers:
                    file.write(str(t) + '\n')   
                print("Data save successfully")
        except FileExistsError:
            print("File have Alredy Exist")  
           
    def read_file(self):
        try:
            with open("school_data.txt", 'r') as file:
                lines = file.readlines()
                
                mode = None
                for line in lines:
                    line = line.strip()
                    
                    if line == "STUDENT":
                        mode = "student"
                        continue
                    if line == "TEACHER":
                        mode = "teacher"
                        continue
                    
                    if mode == 'student':
                        student = Student.from_string(line)
                        self.students.append(student)
                        
                    if mode == 'teacher':
                        teacher = Teacher.from_string(line)
                        self.teachers.append(teacher)
                        print("Data loaded  successfully")    
                
        except FileNotFoundError:
            print("File not found")
            
def login_system():
    USERNAME = "Gwandu"
    PASSWORD = '688076'
    
    attemt = 3
    
    while attemt > 0:
        print("WELCOME TO OUR SCHOOL")
        
        username = input("Entet your Username: ")
        password = input("Enter your password: ")
        
        if username == USERNAME and password == PASSWORD:
            print("Login Succesuffly")
            return True
            
        else:
            attemt -= 1
            print("Encorrect Username or password")
            print(f"Try again [{attemt}] attempts left  ")
    print("Access denied")
    return False
                              

def menu():
    my_school = School()
    
    print("========= Menu ========")
    print("1. Add Student")
    print("2. Show Student")
    print("3. Add Teacher")
    print("4. Show Teacher")
    print("5. Save data")
    print("6. Load data")
    print("0. Exit ")
    print("========= Menu ========")
    

    while True:
        choice = input("Enter Your choice: ")  
        if choice == '1':
            name = input("Enter your name: ")
            age  = int(input("Enter  your age: "))
            marks = input('Enter your marks: ')
            marks = list(map(int, marks.split(',')))
            
            student = (name, age, marks)
            my_school.add_student(student)
            
        elif choice == '2':
            my_school.show_student()
            
        elif choice == '3':
            name  = input("Enter  your name: ")
            age  = int(input("Enter  your age: "))
            subject = input("Enter you subject: ")
            
            teacher = (name, age, subject)
            my_school.add_teachers(teacher)
            
        elif choice == '4':
            my_school.show_techear()
            
        elif choice == '5':
            my_school.save_data()
            
        elif choice == '6':
            my_school.read_file()
            break
        else:
            print("Invalid Choice Try again")
            
            
 
                 
                 
                 
if login_system():              
    menu()
    
