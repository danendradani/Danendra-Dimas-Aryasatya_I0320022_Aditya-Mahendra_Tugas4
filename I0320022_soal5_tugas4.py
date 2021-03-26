# string awal
s = "Hey there! what should this string be?"
print(s)
print("")

# panjangnya harusnya 20
s = s[0:20]
print(s)
print("panjang dari s = %d" % len(s))
print("")

# huruf pertama 'a' harusnya di index no 8
s = s.replace("there", "media")
print(s)
print("Kemunculan pertama a = %d" % s.index("a"))
print("")

# jumlah huruf a harusnya 2
print(s)
print("a muncul sebanyak %d kali" % s.count("a"))
print("")

# memotong string berdasarkan index
print(s)
print("Lima karakter pertama adalah'%s'" % s[:5]) # Start to 5"
print("Lima karakter berikutnya adalah '%s'" % s[5:10]) # 5 to 10
print("Karakter ketiga belas adalah '%s'" % s[12]) # Just number 12
print("Karakter dengan indeks ganjil adalah '%s'" %s[1::2]) # (0-based indexing)
print("Lima karakter terakhir adalah '%s'" % s[-5:]) # 5th-from-last to end
print("")

# konversikan ke uppercase
print("String dalam huruf besar: %s" % s.upper())
print("")

# konversikan ke lowercase
print("String dalam huruf kecil: %s" % s.lower())
print("")

# cek bagaimana string itu dimulai
s = s.replace("Hey", "Str")
print(s)
if s.startswith("Str"):
    print("String dimulai dengan 'Str'. Good!")
print("")

# cek bagaimana string itu diakhiri
s = s.replace("shou", "ome!")
print(s)
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome!'. Good!")
print("")

# pisahkan string menjadi tiga string yang terpisah,
# masing-masing hanya berisi satu kata
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))