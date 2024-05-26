print('UTS ARSITEKTUR DAN ORGANISASI KOMPUTER TI.23.C7')
print('Python Program : Inverted right-angled triangle pattern of number ')
print('=================================================================')
print('Nama : Nabhan Labib')
print('NIM  : 312310783')
print('Kelas: TI.23.C.7') #Bagian data diri dan Judul
print()
  
n = int(input('Input Angka: '))  #Masukan angka sebagai acuan Looping
print()

print('Hasil Tampilan: ')
print('=================================================================')
for i in range(n,0,-1):       #Looping mengacu pada Masukan angka (n)
  for j in range(i,0,-1):
    print(j,' ',end='',sep='') #Diberikan spasi (' ') agar membentuk segitiga yang proper
  print()

print('=================================================================')