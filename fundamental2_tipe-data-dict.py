""" Tipe data dictionary sekadar menghubungkan KEY dan VALUE
KVP = Key Value Pair """

kamus_INA_ENG = {'anak': 'child', 'ayah': 'father', 'ibu': 'mother'}
print(kamus_INA_ENG)
print(kamus_INA_ENG['ayah'])
print(kamus_INA_ENG['ibu'])  # cuma satu arah. jadi kalo print(kamus_INA_ENG['mother']) ga bakal keluar

print('\nData ini dikirimkan oleh server Gojek untuk memberikan informasi driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-11-26',
    'driver_list': [
        {'Nama': 'a', 'jarak': 10},
        {'Nama': 'b', 'jarak': 11},
        {'Nama': 'c', 'jarak': 13},
        {'Nama': 'd', 'jarak': 16}
    ]
}
print(data_dari_server_gojek)
print(f"Driver di sekitar sini : {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 : {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']}m")
