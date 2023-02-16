def create_student(name,korean,math,english,science):
    return{
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student["korean"]+student["math"]+\
        student["english"]+student["science"]

def student_get_average(student):
    return student_get_sum(student)/4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )

students = [
    {"name":"윤인성", "korean":87,"math":98, "english":88, "science":95},
    {"name":"연하진", "korean":92,"math":98, "english":96, "science":98},
    {"name":"구지연", "korean":76,"math":96, "english":94, "science":90},
    {"name":"나선주", "korean":98,"math":92, "english":96, "science":92},
    {"name":"윤아린", "korean":95,"math":98, "english":98, "science":98},
    {"name":"윤명월", "korean":64,"math":88, "english":92, "science":92},
]

print("이름","총점","평균",sep="\t")
for student in students:
    print(student_to_string(student))