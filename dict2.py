import json

# 读取 JSON 文件
with open('students.json', 'r') as file:
    data = json.load(file)

# 获得数据
students = data['students']

# 打印数据
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"MATH GRADE: {student['grades']['math']}")
    print(f"SCIENCE GRADE: {student['grades']['science']}")
    print()
                                   