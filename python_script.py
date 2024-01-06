def hitung_nilai(nilai):
    if 90 <= nilai <= 100:
        return 'A'
    elif 80 <= nilai < 90:
        return 'B'
    elif 70 <= nilai < 80:
        return 'C'
    elif 60 <= nilai < 70:
        return 'D'
    elif 0 <= nilai < 60:
        return 'F'
    else:
        return 'Nilai Tidak Valid'

# Contoh: Meminta input dari pengguna
try:
    nilai = float(input("Masukkan nilai: "))
    if 0 <= nilai <= 100:
        grade = hitung_nilai(nilai)
        print(f"Nilai untuk nilai {nilai} adalah {grade}")
    else:
        print("Input tidak valid. Nilai harus berada di antara 0 dan 100.")
except ValueError:
    print("Input tidak valid. Harap masukkan nilai numerik.")

