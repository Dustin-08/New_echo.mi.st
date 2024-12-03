#plan.py

class Student:
    """
    student 클래스:
    - 학생의 정보를 관리하고, 수강신청, 취소, 시간표 확인 기능을 제공합니다.
    - 각 학생은 여러 강의를 신청할 수 있으며, 강의 정보는 courses 리스트에 저장됩니다.
    """
    def __init__(self, id, name):
        self.id = id #학번 (고유 식별자)
        self.name = name #학생 이름
        self.courses = [] #수강 리스트 (course 객체를 저장)

    # === 2번 담당자가 구현할 메서드 ===
    def enroll_course(self, course):
        for enrolled_course in self.courses:
            if enrolled_course.is_time_conflict(course):
                print(f"[오류] 시간 충돌: {enrolled_course.name}과(와) 시간이 겹칩니다.")
                return False

        if course.is_full():
            print(f"[오류] 정원 초과: {course.name} 강의는 정원이 가득찼습니다.")
            return False

        self.courses.append(course)
        course.enrolled_students.append(self)
        course.enrolled += 1
        print(f"[성공] {course.name} 강의를 신청했습니다.")

        
    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.enrolled_students.remove(self)
            course.enrolled -= 1
            print(f"[성공] {course.name} 강의를 취소했습니다.")
            return True
        else:
            print(f"[오류] {course.name} 강의를 수강 중이 아닙니다.")
            return False

    def view_schedule(self):
        if not self.courses:
            print("[정보] 현재 수강 중인 강의가 없습니다.")
        else:
            print(f"\n=== {self.name}님의 시간표 ===")
            for course in self.courses:
                print(f"- {course.name}: {course.day} {course.start_time} ~ {course.end_time}")

class Professor:
    """
    Professor 클래스:
    - 교수의 정보를 관리하고, 강의를 등록하거나 수강생 명단을 확인하는 기능을 제공합니다.
    - 각 교수는 여러 강의를 담당할 수 있으며, 강의 정보는 courses 리스트에 저장됩니다.
    """
    def __init__(self, id, name):
        self.id = id #교수 ID
        self.name = name # 교수 이름
        self.courses = [] #담당 강의 리스트

    # === 2번 담당자가 구현할 메서드 ===
    def add_course(self, name, day, start_time, end_time, max_capacity):
        course = Course(name, day, start_time, end_time, max_capacity)
        self.courses.append(course)
        print(f"[성공] {name} 강의가 추가되었습니다.")
        return course

    def view_students(self, course):
        if course in self.courses:
            print(f"\n==={course.name} 강의 수강생 목록 ===")
            for student in course.enrolled_students:
                print(f"-{student.id}: {student.name}")
        else:
            print(f"[오류] {course.name} 강의를 담당하지 않습니다.")

class Course:
    """
    Course 클래스:
    - 강의 정보를 관리하며 정원 관리 기능을 제공합니다.
    - 강의명, 강의 시간, 최대 정원, 현재 신청 인원 등의 정보를 저장합니다.
    """
    def __init__(self, name, day, start_time, end_time, max_capacity):
        self.name = name #강의 이름
        self.day = day
        self.start_time = start_time #강의 시작 시간
        self.end_time = end_time #강의 종료 시간
        self.max_capacity = max_capacity #최대 정원
        self.enrolled = 0 #현재 신청 인원
        self.enrolled_students = [] #수강생 리스트 (student 객체를 저장)

    # === 3번 담당자가 구현할 메서드 ===
    def is_time_conflict(self, other_course):
        if self.day != other_course.day:
            return False
        if self.start_time < other_course.end_time and self.end_time > other_course.start_time:
            return True
        return False

    def is_full(self):
        return self.enrolled >= self.max_capacity
        
    def update_enrollment(self, add_student=True):
        if add_student:
            if not self.is_full():
                self.enrolled += 1
                print(f"[성공] {self.name} 강의의 현재 수강생 수: {self.enrolled}/{self.max_capacity}")
                return True
            else:
                print(f"[오류] {self.name} 강의는 정원이 가득 찼습니다.")
                return False
        else:
            if self.enrolled > 0:
                self.enrolled -= 1
                print(f"[성공] {self.name} 강의의 현재 수강생 수: {self.enrolled}/{self.max_capacity}")
                return True
            else:
                print(f"[오류] {self.name} 강의에 수강생이 없습니다.")
                return False
   

class System:
    """
    System 클래스:
    - 전체 학생, 교수, 강의 정보를 관리하고, 데이터를 검색 / 추가하는 기능을 제공합니다
    """
    def __init__(self):
        self.students = [] #전체 학생 리스트 (student 객체를 저장)
        self.professors = [] #전체 교수 리스트 (professor 객체를 저장)
        self.courses = [] #전체 강의 리스트 (Course 객체를 저장)

    # === 4번 담당자가 구현할 메서드 ===
    def add_student(self, id, name):
        student = Student(id, name)
        self.students.append(student)
        print(f"[성공] 학생 {name}(학번: {id})이 추가되었습니다.")
        return student

    def add_professor(self, id, name):
        professor = Professor(id, name)
        self.professors.append(professor)
        print(f"[성공] 교수 {name}(ID: {id})이 추가되었습니다.")
        return professor

    def add_course(self, professor, name, day, start_time, end_time, max_capacity):
        course = Course(name, day, start_time, end_time, max_capacity)
        self.courses.append(course)
        professor.courses.append(course)
        print(f"[성공] 강의 {name}이 추가되었습니다. (담당 교수: {professor.name})")
        return course

    def find_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        print(f"[오류] 학번 {student_id}의 학생을 찾을 수 없습니다.")
        return None
    
    def find_professor(self, professor_id):
        for professor in self.professors:
            if professor.id == professor_id:
                return professor
        print(f"[오류] 교수 ID {professor_id}의 교수를 찾을 수 없습니다.")
        return None

    def find_course(self, course_name):
        for course in self.courses:
            if course.name == course_name:
                return course
        print(f"[오류] 강의명 {course_name}에 해당하는 강의를 찾을 수 없습니다.")
        return None

    def show_all_data(self):
        """
        시스템 내 모든 데이터를 출력합니다.
        """
        print("\n=== 학생 목록 ===")
        for student in self.students:
            print(f"{student.id}: {student.name}")

        print("\n=== 교수 목록 ===")
        for professor in self.professors:
            print(f"{professor.id}: {professor.name}")

        print("\n=== 강의 목록 ===")
        for course in self.courses:
            print(f"{course.name}: {course.day} {course.start_time} ~ {course.end_time} (정원: {course.enrolled}/{course.max_capacity})")
