# input usia peserta
x = 21
print("Berapa usia anda?")
usia = int(input("Usia saya adalah : "))

# input jawaban peserta
if usia >= x:
    print("Apakah anda sudah lulus ujian kualifikasi? (Y / T)")
    jawaban = input("")
    if jawaban == "Y" or "y":
        print("Anda dapat mendaftar di kursus")
    else:
        print("Anda tidak dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")