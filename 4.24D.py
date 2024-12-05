print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
def count_upper_lower(sentence):
    upper_case = sum(1 for c in sentence if c.isupper())
    lower_case = sum(1 for c in sentence if c.islower())
    return upper_case, lower_case
sentence = input("Nhập câu của bạn: ")
upper_case, lower_case = count_upper_lower(sentence)
print(f"Chữ hoa: {upper_case}")
print(f"Chữ thường: {lower_case}")
