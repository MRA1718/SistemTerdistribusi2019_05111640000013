-------------------------------

name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777
gunakan URI untuk referensi name server yang akan digunakan
untuk mengetahui instance apa saja yang aktif gunakan pyro4-nsc -n localhost -p 7777 list

untuk instance yang berbeda, namailah fileserver dengan angka
ns.register("fileserver2", uri_fileserver)
ns.register("fileserver3", uri_fileserver)

