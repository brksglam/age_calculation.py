# Giriş verilerini al
isim = input("Adınız nedir? ")
yas = int(input("Yaşınız kaç? "))

# Hesaplamalari yap
dogum_yili = 2023 - yas
gelecek_yili = dogum_yili + 100

# Sonuçları yazdır
print("Adınız:", isim)
print("Yaşınız:", yas)
print("Doğum yılınız:", dogum_yili)
print("100 yıl sonra:", gelecek_yili)