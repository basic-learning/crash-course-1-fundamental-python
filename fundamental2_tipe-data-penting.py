# Tipe data skalar => tipe data sederhana
print('-----Tipe data skalar-----')
anak1 = 'a'
anak2 = 'b'
anak3 = 'c'
anak4 = 'd'
print(anak1)
...
# Tipe data list/array/daftar
print('\n-----Tipe data list-----')
anak = ['a', 'b', 'c', 'd']
print(anak)
anak.append('e') #buat nambahin data ke list
print(anak)
print('*Menyapa anak ke-2*')
print(f'Hai {anak[1]}!')
print('*Menyapa semua anak*')
for a in anak:
    print(f'Hai {a}!')
print('*Menyapa semua anak (cara ribet)*')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}!')