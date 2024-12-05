print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")

input_string = input("Nhập Chuỗi: ")
new_string = ''.join(char for char in input_string if not char.isdigit())
print("Chuỗi sau khi loại bỏ chữ số:", new_string)
