def hitung_rata2 ( daftar_nilai ):
  total=0
  for nilai in daftar_nilai:total+=nilai
  return total/len(daftar_nilai)
def cetak_hasil (nama,daftar_nilai):
 hasil=hitung_rata2( daftar_nilai )
 print("Mahasiswa: "+nama+", Rata-rata nilai:"+str( hasil ))
 daftar_nilai.sort() ;print ("Nilai Terendah:",daftar_nilai[0],"| Nilai Tertinggi:",daftar_nilai[-1] )
  
nilai_siswa=[80, 75, 90, 85,100,60]
cetak_hasil ("Andi" , nilai_siswa)
