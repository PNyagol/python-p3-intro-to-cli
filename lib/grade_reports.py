#!/usr/bin/env python3
import os

def create_grade_report(student_grades):
    if not os.path.exists('reports'):
        os.makedirs('reports')

    file_path = os.path.join('reports', 'grade_reports.txt')
    with open(file_path, 'w') as gr:
        for grade in student_grades:
            gr.write(grade + '\n')

if __name__ == '__main__':
    student_grades = []

    grade = input("Student Name, Grade: ")
    while grade:
        student_grades.append(grade)
        grade = input("Student Name, Grade: ")

    create_grade_report(student_grades)
