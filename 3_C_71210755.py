alas = int(input("masukan alas atap :"))
tinggi = int(input("masukan tinggi atap :"))
sisi = int(input("masukan tinggi tembok :"))

#proses
hasil = (alas * tinggi * 0.5) + (sisi * sisi)
semen = hasil/5

print("rumah tersebut membutuhkan", semen, "sak semen")
