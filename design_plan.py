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
        """
        수강 신청 메서드:
        - 강의 객체 (course)를 받아 학생의 수강 목록에 추가합니다.
        - 구현 내용:
        1) 현재 수강 중인 강의들과 시간이 겹치는지 검사.
        2) 강의 정원이 초과되었는지 확인.
        3) 조건을 만족하면 self.courses에 강의를 추가.
        4) course.enrolled_students에 학생 객체(self)를 추가
        - 반환값:
         - 성공 시: True
         - 실패 시: False
        """
        pass #2번: 구현 필요

    def drop_course(self, course):
        """
        수강 취소 메서드:
        - 학생의 수강 목록에서 특정 강의를 삭제합니다.
        - 구현 내용:
        1) self.courses에서 해당 강의를 제거
        2) course.enrolled_students에서 학생을 제거
        3) course.enrolled 수를 감소시킴.
        - 반환값:
         - 성공 시: true
         - 실패 시: False (해당 강의를 수강 중이 아닌 경우)
        """
        pass #2번: 구현 필요

    def view_schedule(self):
        """
        시간표 보기 메서드:
        - 현재 학생이 수강 신청한 강의들의 목록과 시간을 출력합니다.
        - 구현 내용:
        1) self.courses 리스트를 순회하며 강의명과 시간을 출력.
        2) 수강 중인 강의가 없을 경우, 적절한 메시지를 출력.
        """
        pass #2번: 구현 필요

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
    def add_course(self, name, start_time, end_time, max_capacity):
        """
        강의 등록 메서드:
        - 새로운 강의를 생성하여 교수의 강의 목록에 추가합니다.
        - 구현 내용:
        1) course 객체를 생성.
        2) self.courses에 해당 강의를 추가.
        - 반환값: 생성된 course 객체
        """
        pass #2번 구현 필요

    def view_students(self, course):
        """
        수강생 확인 메서드:
        - 특정 강의를 수강 중인 학생 명단을 출력합니다.
        - 구현 내용:
        1) course.enrolled_students 리스트를 순회하며 학생 정보를 출력.
        2) 해당 강의를 담당하지 않는 경우, 적절한 메시지를 출력.
        """
        pass #2번 구현 필요

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
    def update_enrollment(self):
        """
        정원 관리 메서드:
        - 수강 신청 시 강의의 현재 인원(enrolled)을 업데이트합니다.
        - 구현 내용:
        1) 정원이 초과되었는지 확인.
        2) 조건을 만족하면 수강생 리스트와 enrolled 값을 갱신.
        """
        pass #3번 구현 필요

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
        """
        학생 추가 메서드:
        - 새로운 학생 객체를 생성하여 시스템에 추가합니다
        - 구현 내용:
        1) student 객체를 생성.
        2) self.students 리스트에 추가.
        """
        pass #4번 구현 필요

    def add_professor(self, id, name):
        """
        교수 추가 메서드:
        - 새로운 교수 객체를 생성하여 시스템에 추가합니다
        - 구현 내용:
        1) Professor 객체를 생성.
        2) self.Professors 리스트에 추가.
        """
        pass #4번 구현 필요

    def add_course(self, professor, name, day, start_time, end_time, max_capacity):
        """
        강의 추가 메서드:
        - 교수와 강의를 연결하고, 시스템 강의 리스트에 추가합니다.
        - 구현 내용:
        1) Professor 객체의 add_course 메서드를 호출해 강의 생성.
        2) self.courses 리스트에 추가.
        """
        pass #4번 구현 필요

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
            print(f"{course.name}: {course.start_time} ~ {course.end_time} (정원: {course.enrolled}/{course.max_capacity})")
