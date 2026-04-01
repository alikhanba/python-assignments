from c1 import student_name

print(f"Name uppercase:{student_name.upper()}")
print(f"Name lowercase:{student_name.lower()}")

name_lengt=len(student_name)
print(f"Name length:{name_length}")
masked_name=student_name.replace(student_name[0],'*',1)
print(f"Masked name:{masked_name}")