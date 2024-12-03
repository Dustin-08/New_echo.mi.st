from 통합 import System

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
