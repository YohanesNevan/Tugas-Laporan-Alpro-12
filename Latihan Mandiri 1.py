n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    
    data_aplikasi[nama_kategori] = aplikasi

print("Data aplikasi per kategori:")
print(data_aplikasi)

daftar_aplikasi_list = [set(aplikasi) for aplikasi in data_aplikasi.values()]

all_apps = set().union(*daftar_aplikasi_list)

app_count = {}
for app_set in daftar_aplikasi_list:
    for app in app_set:
        if app in app_count:
            app_count[app] += 1
        else:
            app_count[app] = 1

unique_apps = [app for app, count in app_count.items() if count == 1]
print("Aplikasi yang hanya muncul di satu kategori:")
print(unique_apps)

if n > 2:
    double_category_apps = [app for app, count in app_count.items() if count == 2]
    print("Aplikasi yang muncul tepat di dua kategori sekaligus:")
    print(double_category_apps)
else:
    print("Jumlah kategori tidak lebih dari 2, tidak ada aplikasi yang muncul tepat di dua kategori sekaligus.")

if daftar_aplikasi_list:
    hasil = daftar_aplikasi_list[0]
    for i in range(1, len(daftar_aplikasi_list)):
        hasil = hasil.intersection(daftar_aplikasi_list[i])
    print("Aplikasi yang muncul di semua kategori:")
    print(hasil)
else:
    print("Tidak ada data aplikasi untuk dihitung.")
