print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")

input_str = input("Nhập các số, phân tách bởi dấu phẩy: ")
numbers = list(map(int, input_str.split(',')))
odd_numbers = [str(num) for num in numbers if num % 2 != 0]
output_str = ','.join(odd_numbers)
print("Các số lẻ là: " + output_str)

