# Listelerde okuma
liste = ["Ahmet", "Mehmet", 23, 65, 3.2]
print(liste)
print('1 ile 3.index arası: ', liste[1:3])

# sondan başa sıralama **0 pozitif tamsayıdır
print('En SON VERİ: ', liste[-1])  # listenin son elemanını verir
print('-1 ile -3.index arası: ', liste[-3:-1])

print("Liste uzunluğu :", len(liste))  # liste uzunluğunu verir

# LİSTE DEĞİŞTİRME - SİLME

liste[0] = 111
print(liste)  # listenin ilk elemanını 111 ile değiştirmiş olduk

# ELEMENT SİLME

son_element = liste.pop()
print(liste)  # en sondaki eleman listeden atılıp son_element içine yazılır
print(son_element)  # 3.2 çıktısı verir

# KOLEKSİYONU TEMİZLE
liste.clear()
print('Listenin son hali :', liste)

# TUPLE(DEMET) --> Bir veya daha fazla veriyi topla ve kullandırır. 0 bazlı dizin eklenir.
# Bir kez oluşturulduktan sonra içeriği değiştirilemez READ ONLY olarak

bos_demet1 = ()
bos_demet2 = tuple()

demet1 = (1, 2, 3)

print(dir(tuple))