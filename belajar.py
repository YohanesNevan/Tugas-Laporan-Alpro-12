bilangan_genap = {2, 4, 6, 8, 10, 12}
bilangan_ganjil = {1, 3, 5, 7, 9, 11}

pernah_ke_bulan = set('Neil Armstrong', 'Buzz Aldrin')

nim = {'71200120', '71200195', '71200214'}
jumlah_nim = len(nim)
print(jumlah_nim) # akan menghasilkan output 3
# tampilkan isi set satu-persatu
for n in nim:
    print(n)

# definisikan sebuah set kosong
plat_nomor = set()
# tambahkan plat nomor 'AB 1890 XA'
plat_nomor.add('AB 1890 XA')
# tambahkan plat nomor 'AD 6810 MT'
plat_nomor.add('AD 6810 MT')
# jumlah anggota di dalam Set
print(len(plat_nomor))
# tambahkan plat yang sama sekali lagi
plat_nomor.add('AB 1890 XA')
# tampilkan semua plat nomor
for plat in plat_nomor:
    print(plat)

bilangan_prima = {13, 23, 7, 29, 11, 5}
# hapus 5 dari set tersebut
bilangan_prima.remove(5)
print(bilangan_prima)

# hapus 97 (tidak ada)
bilangan_prima.discard(97)
print(bilangan_prima)

# ambil dan hapus salah satu
bilangan = bilangan_prima.pop()
print(bilangan)
print(bilangan_prima)

# kosongkan set
bilangan_prima.clear()
print(bilangan_prima)

# Buat Set dari List
ikan = set(['koi', 'koki', 'kembung', 'salmon'])
print(ikan)
# ganti koi menjadi teri
ikan.remove('koi')
ikan.add('teri')
print(ikan)

renang = {'siti', 'mail', 'ikhsan', 'upin', 'ipin'}
tenis = {'joko', 'mail', 'ipin', 'upin', 'tejo'}
# suka renang dan tenis
renang_tenis = renang & tenis
print(renang_tenis)

merek_hp = {'Samsung', 'Apple', 'Xiaomi', 'Sony'}
merek_ac = {'LG', 'Samsung', 'Panasonic', 'Daikin', 'Sony'}
# union dari merek_hp dan merek_ac
gabungan = merek_hp | merek_ac
print(gabungan)

english = {'desi', 'tono', 'evan', 'miko', 'takashi', 'chaewon'}
korean = {'chaewon', 'yeona', 'erika', 'miko'}
# hanya bisa bicara satu bahasa saja
one_language = english ^ korean
print(one_language)

one_languange = english.union(korean) - english.intersection(korean)

a=["a","b","c"]
b=a
print(b)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)


english = {'desi', 'tono', 'evan', 'miko', 'takashi', 'chaewon'}
# bisa berbahasa korea
korean = {'chaewon', 'yeona', 'erika', 'miko'}
# siapa yang hanya bisa bahasa korea?
only_korean = korean - english
print(only_korean)
# siapa yang hanya bisa bahasa english?
only_english = english
print(only_english)




