#ถ้าเงื่อนไข้เป็นจริงให้หยุด
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
#-----------------------------------------------------------
# #ถ้าเงื่อนไข้เป็นจริงให้ไปต่อ
y = 1
while y < 6:
    y += 1
    if y == 3:
        continue
    print(y)
#----------------------------------------------------------
# ถ้าเงื่อนไข้เป็นเท็จให้ขึ้นข้อความ
f = 1
while f < 6:
    print(f)
    f += 1
else:
    print("F is no logner less than")