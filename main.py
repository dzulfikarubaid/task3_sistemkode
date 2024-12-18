'''
1. Update alamat mahasiswa dengan NIM "123456" menjadi "Jl. Raya No.5".
2. Tampilkan NIM, nama, dan jurusan dari mahasiswa yang memiliki jurusan "Teknik Informatika", serta tampilkan juga nama dosen pembimbingnya.
3. Tampilkan 5 nama mahasiswa dengan umur tertua.
4. Tampilkan nama mahasiswa, mata kuliah yang diambil, dan nilai yang diperoleh untuk setiap mata kuliah. Hanya tampilkan data mahasiswa yang memiliki nilai lebih bagus dari 70.
'''
import pandas as pd
import json
data_mahasiswa = json.load(open('data_mahasiswa.json'))
data_mata_kuliah = json.load(open('data_mata_kuliah.json'))
df_mahasiswa = pd.DataFrame(data_mahasiswa['mahasiswa'])
df_mata_kuliah = pd.DataFrame(data_mata_kuliah['mata_kuliah'])

# 1. Update alamat mahasiswa dengan NIM "123456" menjadi "Jl. Raya No.5".
df_mahasiswa.loc[df_mahasiswa['nim'] == 123456, 'alamat'] = 'Jl. Raya No.5'
print('1. Update alamat mahasiswa dengan NIM "123456" menjadi "Jl. Raya No.5":')
print(df_mahasiswa)
print('\n')


# 2. Tampilkan NIM, nama, dan jurusan dari mahasiswa yang memiliki jurusan "Teknik Informatika", serta tampilkan juga nama dosen pembimbingnya.
df_mahasiswa_teknik_informatika = df_mahasiswa[df_mahasiswa['jurusan'] == 'Teknik Informatika']
df_mahasiswa_teknik_informatika = df_mahasiswa_teknik_informatika.merge(df_mata_kuliah, left_on='nim', right_on='nim')
print("2. Tampilkan NIM, nama, dan jurusan dari mahasiswa yang memiliki jurusan 'Teknik Informatika', serta tampilkan juga nama dosen pembimbingnya:")
df_mahasiswa_teknik_informatika.drop_duplicates(subset='nim', keep='first', inplace=True)
print(df_mahasiswa_teknik_informatika.reset_index(drop=True)[['nim', 'nama', 'jurusan', 'dosen_pengajar']])
print('\n')


# 3. Tampilkan 5 nama mahasiswa dengan umur tertua.
print("3. Tampilkan 5 nama mahasiswa dengan umur tertua:")
print(df_mahasiswa.sort_values(by='umur', ascending=False).nlargest(5, 'umur').reset_index(drop=True)[['nama', 'umur']])
print('\n')

# 4. Tampilkan nama mahasiswa, mata kuliah yang diambil, dan nilai yang diperoleh untuk setiap mata kuliah. Hanya tampilkan data mahasiswa yang memiliki nilai lebih bagus dari 70.
df_mahasiswa = df_mahasiswa.merge(df_mata_kuliah, left_on='nim', right_on='nim')
df_mahasiswa = df_mahasiswa[df_mahasiswa['nilai'] > 70]
print("4. Tampilkan nama mahasiswa, mata kuliah yang diambil, dan nilai yang diperoleh untuk setiap mata kuliah. Hanya tampilkan data mahasiswa yang memiliki nilai lebih bagus dari 70:")
print(df_mahasiswa[['nama', 'matkul', 'nilai']])
print('\n')