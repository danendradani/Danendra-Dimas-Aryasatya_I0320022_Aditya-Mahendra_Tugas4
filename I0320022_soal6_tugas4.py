a = 4   # 4 = 0000 0100
b = 11  # 11 = 0000 1011

# jawaban soal a
c = a | b;
print("nilai : ", c, ", binary : ", format(c, "08b"))

# jawaban soal b
c = a >> 11;
print("nilai : ", c, ", binary : ", format(c, "08b"))

# jawaban soal c
c = a ^ b;
print("nilai : ", c, ", binary : ", format(c, "08b"))

# jawaban soal d
c = ~a;
print("nilai : ", c, ", binary : ", format(c, "08b"))

# jawaban soal e
c = a & b;
print("nilai : ", c, ", binary : ", format(c, "08b"))