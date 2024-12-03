if __name__ == "__main__":
    # 시스템 생성
    system = System()

    # 학생 추가
    student1 = system.add_student("2024001", "김수정")
    student2 = system.add_student("2024002", "이철수")

    # 교수 추가
    professor1 = system.add_professor("P001", "홍길동")
    professor2 = system.add_professor("P002", "이영희")

    # 강의 추가
    course1 = system.add_course(professor1, "프로그래밍", "월", "09:00", "12:00", 30)
    course2 = system.add_course(professor2, "데이터베이스", "화", "13:00", "16:00", 25)

    # 학생 수강 신청
    student1.enroll_course(course1)  # 성공
    student2.enroll_course(course2)  # 성공
    student1.enroll_course(course2)  # 성공

    # 시간 충돌 테스트
    course3 = system.add_course(professor1, "네트워크", "월", "11:00", "14:00", 20)
    student1.enroll_course(course3)  # 시간 충돌 발생

    # 정원 초과 테스트
    for _ in range(30):  # 정원을 채움
        system.add_student(f"2024{str(_).zfill(3)}", f"학생{_}").enroll_course(course1)
    student1.enroll_course(course1)  # 정원 초과 발생

    # 수강 취소 테스트
    student1.drop_course(course1)  # 성공

    # 시스템 데이터 확인
    system.show_all_data()



--------------------------------------------------


from 통합 import System  # 통합된 코드 파일을 불러옴

def main_menu(system):
    while True:
        print("\n=== 메인 메뉴 ===")
        print("1. 학생 관리")
        print("2. 교수 관리")
        print("3. 강의 관리")
        print("4. 시스템 상태 확인")
        print("5. 종료")
        choice = input("선택: ")

        if choice == "1":
            student_menu(system)
        elif choice == "2":
            professor_menu(system)
        elif choice == "3":
            course_menu(system)
        elif choice == "4":
            system.show_all_data()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

def student_menu(system):
    while True:
        print("\n=== 학생 관리 ===")
        print("1. 학생 추가")
        print("2. 수강 신청")
        print("3. 수강 취소")
        print("4. 시간표 확인")
        print("5. 메인 메뉴로 돌아가기")
        choice = input("선택: ")

        if choice == "1":
            id = input("학번 입력: ")
            name = input("이름 입력: ")
            system.add_student(id, name)
        elif choice == "2":
            student_id = input("학번 입력: ")
            student = system.find_student(student_id)
            if student:
                course_name = input("강의명 입력: ")
                course = system.find_course(course_name)
                if course:
                    student.enroll_course(course)
        elif choice == "3":
            student_id = input("학번 입력: ")
            student = system.find_student(student_id)
            if student:
                course_name = input("강의명 입력: ")
                course = system.find_course(course_name)
                if course:
                    student.drop_course(course)
        elif choice == "4":
            student_id = input("학번 입력: ")
            student = system.find_student(student_id)
            if student:
                student.view_schedule()
        elif choice == "5":
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

def professor_menu(system):
    while True:
        print("\n=== 교수 관리 ===")
        print("1. 교수 추가")
        print("2. 강의 추가")
        print("3. 수강생 확인")
        print("4. 메인 메뉴로 돌아가기")
        choice = input("선택: ")

        if choice == "1":
            id = input("교수 ID 입력: ")
            name = input("이름 입력: ")
            system.add_professor(id, name)
        elif choice == "2":
            professor_id = input("교수 ID 입력: ")
            professor = system.find_professor(professor_id)
            if professor:
                name = input("강의명 입력: ")
                day = input("요일 입력: ")
                start_time = input("시작 시간 입력 (HH:MM): ")
                end_time = input("종료 시간 입력 (HH:MM): ")
                max_capacity = int(input("최대 정원 입력: "))
                system.add_course(professor, name, day, start_time, end_time, max_capacity)
        elif choice == "3":
            professor_id = input("교수 ID 입력: ")
            professor = system.find_professor(professor_id)
            if professor:
                course_name = input("강의명 입력: ")
                course = system.find_course(course_name)
                if course:
                    professor.view_students(course)
        elif choice == "4":
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

def course_menu(system):
    while True:
        print("\n=== 강의 관리 ===")
        print("1. 강의 목록 보기")
        print("2. 메인 메뉴로 돌아가기")
        choice = input("선택: ")

        if choice == "1":
            for course in system.courses:
                print(f"{course.name}: {course.day} {course.start_time} ~ {course.end_time} (정원: {course.enrolled}/{course.max_capacity})")
        elif choice == "2":
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    # 시스템 초기화
    system = System()
    main_menu(system)
