def unique_sum(list):
# ubah dalam bentuk Set
    data_set = set(list)
# hitung jumlah seluruh anggota data_set
    total = 0
    for data in data_set:
        total = total + data
# return hasil akhir
    return total
# contoh penggunaan fungsi unique_sum()
contoh1 = [2, 4, 3, 2, 7, 8, 6, 4, 5, 5]
hasil1 = unique_sum(contoh1)
print(hasil1)