print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
input_string = input("Nhập dãy các từ cách nhau bằng dấu cách:")
words = input_string.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Các từ dài nhất: ", ",".join(longest_words))

