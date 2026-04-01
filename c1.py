student_name=input("Enter student name: ")
mth_gr=float(input("enter Math grade: "))
phy_gr=float(input("enter Physics grade: "))
py_gr=float(input("enter python grade: "))

total_grade=mth_gr+phy_gr+py_gr
aver_grade=total_grade/3
if aver_grade>=90:
    letter_grade="A"
elif aver_grade>=75:
    letter_grade="B"
elif aver_grade>=60:
    letter_grade="C"
elif aver_grade>=50:
    letter_grade="D"
else:
    letter_grade="F"
scholarship=aver_grade>=90 and mth_gr>=70 and phy_gr>=70 and py_gr>=70

print("=" *30)
print(f"Student: {student_name}")
print(f"Math: {mth_gr}")
print(f"Physics: {phy_gr}")
print(f"Python: {py_gr}")
print("-" * 30)
print(f"Average: {aver_grade}")
print(f"Letter grade: {letter_grade}")
print(f"Scholarship: {scholarship}")