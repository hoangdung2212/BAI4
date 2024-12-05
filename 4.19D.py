print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
t= tuple()
for i in range (1, 1000):
    dem=0
    for j in range (1, i+1):
        if (i%j==0):
            dem=dem+1
    if (dem==2):
            t=t+(i,)
print(t)
