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

# Menetapkan nilai secara otomatis
nilai = 90

# Menghitung dan mencetak grade
grade = hitung_nilai(nilai)
print(f"Nilai untuk nilai {nilai} adalah {grade}")

