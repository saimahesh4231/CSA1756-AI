student('John Doe', 'CS101').
student('Alice Smith', 'CS101').
student('Bob Johnson', 'MATH201').
student('Emily Davis', 'PHYS301').
student('Michael Brown', 'CS101').

teacher('Dr. Roberts', 'CS101').
teacher('Dr. Adams', 'MATH201').
teacher('Dr. Lee', 'PHYS301').

find_students(SubjectCode, StudentName) :-
    student(StudentName, SubjectCode).

find_teacher(SubjectCode, TeacherName) :-
    teacher(TeacherName, SubjectCode).

find_subject(StudentName, SubjectCode) :-
    student(StudentName, SubjectCode).

find_subject_by_teacher(TeacherName, SubjectCode) :-
    teacher(TeacherName, SubjectCode).

find_teacher_of_student(StudentName, TeacherName) :-
    student(StudentName, SubjectCode),
    teacher(TeacherName, SubjectCode).
