# Program Menambahkan Data ke dalam List
data_list = []

while True:
    # Input data
    nama = input("Masukkan nama: ")
    tugas = float(input("Masukkan nilai tugas (0-100): "))
    uts = float(input("Masukkan nilai UTS (0-100): "))
    uas = float(input("Masukkan nilai UAS (0-100): "))
    
    # Perhitungan nilai akhir
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
    
    # Menyimpan data ke list
    data_list.append({
        "Nama": nama,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })
    
    # Menanyakan apakah ingin menambah data lagi
    tambah = input("Apakah ingin menambah data lagi? (y/t): ").lower()
    if tambah == "t":
        break

# Menampilkan daftar data
print("\nDaftar Data:")
print("========================================================")
print("No | Nama         | Tugas | UTS   | UAS   | Nilai Akhir")
print("========================================================")
for i, data in enumerate(data_list, start=1):
    print(f"{i:2} | {data['Nama']:<12} | {data['Tugas']:5.1f} | {data['UTS']:5.1f} | {data['UAS']:5.1f} | {data['Nilai Akhir']:11.2f}")
print("========================================================")
