mth_gr=float(input("enter Math grade: "))
phy_gr=float(input("enter Physics grade: "))
py_gr=float(input("enter python grade: "))
subj=['Math', 'Physics', 'Python']
grades=[mth_gr,phy_gr,py_gr]

for i in range(3):
    subj_name=subj[i]
    score=grades[i]

    if score>=90:
        comment='Excellent'
    elif score>=75:
        comment='Good'
    elif score>=60:
        comment='Satisfactor'
    else:
        comment='Fail'

    print(f"{subj_name} : {score} : {comment}")
