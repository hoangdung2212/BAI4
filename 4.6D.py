print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
full_name = input("Nhập tên người: ")
name_parts = full_name.split()
last_name = name_parts[0]
first_name = ' '.join(name_parts[1:])
print("Họ:", last_name)
print("Tên riêng:", first_name)
