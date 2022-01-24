from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
import time
import unittest


browser= webdriver.Chrome()
url ="https://localhost:44378"
browser.get(url) #the site link
time.sleep(5)

#--------------------------------Ekran 1--------------------------------------
#------Tutar1-----
#Tutar1 Kucuk hatasi
tutar1 = browser.find_element_by_id("MainContent_txtTutarBir")
tutar1.send_keys("475")
time.sleep(2)

basvur1 = browser.find_element_by_id("MainContent_btnBasvurBir")
basvur1.click()

time.sleep(2)
tutar1 = browser.find_element_by_id("MainContent_txtTutarBir")
tutar1.clear()

#Tutar1 Buyuk Hatasi
tutar1 = browser.find_element_by_id("MainContent_txtTutarBir")
tutar1.send_keys("1000001")
time.sleep(2)

basvur1 = browser.find_element_by_id("MainContent_btnBasvurBir")
basvur1.click()

time.sleep(2) 
tutar1 = browser.find_element_by_id("MainContent_txtTutarBir")
tutar1.clear()

# #Tutar1 Harf Hatasi
# tutar1 = browser.find_element_by_id("MainContent_txtTutarBir")
# tutar1.send_keys("M3rha6a")
# time.sleep(2)

# basvur1 = browser.find_element_by_id("MainContent_btnBasvurBir")
# basvur1.click()

# time.sleep(2) 
# tutar1 = browser.find_element_by_id("MainContent_txtTutarBir")
# tutar1.clear()

# -----Tutar 2-----
#Tutar2 Kucuk hatasi
tutar2 = browser.find_element_by_id("MainContent_txtTutarIki")
tutar2.send_keys("475")
time.sleep(2)

basvur2 = browser.find_element_by_id("MainContent_btnBasvurIki")
basvur2.click()

time.sleep(2) 
tutar2 = browser.find_element_by_id("MainContent_txtTutarIki")
tutar2.clear()

#Tutar2 Buyuk hatasi
tutar2 = browser.find_element_by_id("MainContent_txtTutarIki")
tutar2.send_keys("1000001")
time.sleep(2)

basvur2 = browser.find_element_by_id("MainContent_btnBasvurIki")
basvur2.click()

time.sleep(2) 
tutar2 = browser.find_element_by_id("MainContent_txtTutarIki")
tutar2.clear()

# #Tutar2 Harf Hatasi
# tutar2 = browser.find_element_by_id("MainContent_txtTutarIki")
# tutar2.send_keys("M3rha6a")
# time.sleep(2)

# basvur2 = browser.find_element_by_id("MainContent_btnBasvurIki")
# basvur2.click()

# time.sleep(2) 
# tutar2 = browser.find_element_by_id("MainContent_txtTutarIki")
# tutar2.clear()


#-----Tutar 3-----
#Tutar3 Kucuk hatasi
tutar3 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar3.send_keys("475")
time.sleep(2)

basvur3 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur3.click()

time.sleep(2) 
tutar3 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar3.clear()

#Tutar3 Buyuk hatasi
tutar3 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar3.send_keys("1000001")
time.sleep(2)

basvur3 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur3.click()

time.sleep(2) 
tutar3 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar3.clear()

# #Tutar3 Harf Hatasi
# tutar3 = browser.find_element_by_id("MainContent_txtTutarUc")
# tutar3.send_keys("M3rha6a")
# time.sleep(2)

# basvur3 = browser.find_element_by_id("MainContent_btnBasvurUc")
# basvur3.click()

# time.sleep(2) 
# tutar3 = browser.find_element_by_id("MainContent_txtTutarUc")
# tutar3.clear()


#Hatasiz Devam
tutar3 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar3.send_keys("1200")
time.sleep(2)

basvur3 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur3.click()
time.sleep(2)

basvur3 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur3.click()

#--------------------------------Ekran 2--------------------------------------
#clear method

#Hatasiz Devam (File upload oluyor ama kaydet deyince kabul etmiyor)
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
gelirb.send_keys("101")

time.sleep(2)
foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")                                   


kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
kvkk.click()

time.sleep(2)
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()


#Temizlik
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.clear()

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.clear()

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.clear()

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.clear()

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.clear()

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.clear()

gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
gelirb.clear()

time.sleep(2)


#Tc eksik hane
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("9876543210")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
gelirb.send_keys("100")

foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg")
                  
secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")  


# kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
# kvkk.click()

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()

time.sleep(2)


tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.clear()

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.clear()

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.clear()

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.clear()

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.clear()

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.clear()

#gelirb = browser.find_element_by_id("MainContent_ txtGelir") #*
#gelirb.clear()

#secim =browser.find_element_by_id("MainContent_ddlMeslekler")  
#secim.clear()                

time.sleep(2)


#eposta hatasi
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

# eposta = browser.find_element_by_id("MainContent_txtEmail") #*
# eposta.send_keys("akhaciogmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

#gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
#gelirb.send_keys("100")

foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg")
                  
secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")  


#kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
#kvkk.click()

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()

time.sleep(5)


tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.clear()

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.clear()

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.clear()

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.clear()

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.clear()

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.clear()

#gelirb = browser.find_element_by_id("MainContent_ txtGelir") #*
#gelirb.clear()

#secim =browser.find_element_by_id("MainContent_ddlMeslekler")  
#secim.clear()                

time.sleep(2)


#tel basa 0 hatasi
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("0557252612")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

#gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
#gelirb.send_keys("100")

foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg")
                  
secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")  


#kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
#kvkk.click()

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()

time.sleep(5)


tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.clear()

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.clear()

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.clear()

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.clear()

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.clear()

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.clear()

#gelirb = browser.find_element_by_id("MainContent_ txtGelir") #*
#gelirb.clear()

#secim =browser.find_element_by_id("MainContent_ddlMeslekler")  
#secim.clear()                

time.sleep(2)


#tel hane hatasi
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("25273785150")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

#gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
#gelirb.send_keys("100")

foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg")
                  
secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")  


#kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
#kvkk.click()

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()

time.sleep(5)


tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.clear()

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.clear()

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.clear()

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.clear()

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.clear()

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.clear()

#gelirb = browser.find_element_by_id("MainContent_ txtGelir") #*
#gelirb.clear()
             

time.sleep(2)


#dg hatasi
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05012010")

#gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
#gelirb.send_keys("100")

foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg")
                  
secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")  


# kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
# kvkk.click()

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()

time.sleep(5)


tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.clear()

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.clear()

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.clear()

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.clear()

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.clear()

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.clear()

#gelirb = browser.find_element_by_id("MainContent_ txtGelir") #*
#gelirb.clear()

#secim =browser.find_element_by_id("MainContent_ddlMeslekler")  
#secim.clear()                

time.sleep(2)


#foto hatasi
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

#gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
#gelirb.send_keys("100")
                  
secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")  


#kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
#kvkk.click()

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()

time.sleep(5)


tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.clear()

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.clear()

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.clear()

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.clear()

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.clear()

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.clear()

#gelirb = browser.find_element_by_id("MainContent_ txtGelir") #*
#gelirb.clear()

#secim =browser.find_element_by_id("MainContent_ddlMeslekler")  
#secim.clear()                

time.sleep(2)


#Kvkk kabul hatasi
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

#gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
#gelirb.send_keys("100")

time.sleep(2)
foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")                                  


kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
kvkk.click()

time.sleep(2)
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()

time.sleep(5)


tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.clear()

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.clear()

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.clear()

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.clear()

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.clear()

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.clear()

#gelirb = browser.find_element_by_id("MainContent_ txtGelir") #*
#gelirb.clear()

#secim =browser.find_element_by_id("MainContent_ddlMeslekler")  
#secim.clear()                

time.sleep(2)


#gelir hatasi
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Arthur")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Pendragon")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
gelirb.clear()
time.sleep(2)
gelirb.send_keys("0")

foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg")
                  
secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")  


kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
kvkk.click()

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()

time.sleep(5)


# tcno = browser.find_element_by_id("MainContent_txtTc") #*
# tcno.clear()

# ad = browser.find_element_by_id("MainContent_txtAd") # !
# ad.clear()

# soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
# soyad.clear()

# eposta = browser.find_element_by_id("MainContent_txtEmail") #*
# eposta.clear()

# telno = browser.find_element_by_id("MainContent_txtTelefon") #*
# telno.clear()

# dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
# dg.clear()

# #gelirb = browser.find_element_by_id("MainContent_ txtGelir") #*
# #gelirb.clear()

# #secim =browser.find_element_by_id("MainContent_ddlMeslekler")  
# #secim.clear()                

#time.sleep(2)


# #Hatasiz Devam (File upload oluyor ama kaydet deyince kabul etmiyor)
# tcno = browser.find_element_by_id("MainContent_txtTc") #*
# tcno.send_keys("98765432141")

# ad = browser.find_element_by_id("MainContent_txtAd") # !
# ad.send_keys("Arthur")

# soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
# soyad.send_keys("Pendragon")

# eposta = browser.find_element_by_id("MainContent_txtEmail") #*
# eposta.send_keys("akhaciog@gmail.com")

# telno = browser.find_element_by_id("MainContent_txtTelefon") #*
# telno.send_keys("5572526128")

# dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
# dg.send_keys("05011994")

# gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
# gelirb.clear()
# time.sleep(2)
# gelirb.send_keys("191")

# time.sleep(2)
# foto = browser.find_element_by_id("MainContent_fuResim") #*
# foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

# secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
# meslek =Select(secim)   #DROPDOWN LIST
# meslek.select_by_visible_text("Memur")                                  


# # kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
# # kvkk.click()

# time.sleep(2)
# kaydet = browser.find_element_by_id("MainContent_btnKaydet")
# kaydet.click()


#--------------------------------Ekran 3--------------------------------------

url ="https://localhost:44378/Pages/Basvurularim"
browser.get(url) #the site link
time.sleep(3)

belge_yukle = browser.find_element_by_id("MainContent_rptBasvurular_btnBelgeYukle_2")
belge_yukle.click()
time.sleep(3)



#--------------------------------Ekran 4--------------------------------------

#Belge yok hatasi
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)

#Belgenizi yukleyiniz
belge_ekle = browser.find_element_by_id("MainContent_btnSatirEkle")
belge_ekle.click()
time.sleep(3)

time.sleep(2)
belge = browser.find_element_by_id("MainContent_fuBelge") #*
belge.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

belge = browser.find_element_by_id("MainContent_ddlBelgeler") #*
belge.send_keys("Faiz Geliri Belgesi") 

belge_ekle = browser.find_element_by_id("MainContent_btnSatirEkle")
belge_ekle.click()
time.sleep(3)

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)


#--------------------------------Ekran 5--------------------------------------
url ="https://localhost:44378/Pages/BasvuruOnaylama"
browser.get(url) #the site link
time.sleep(3)
 
 
#1100-1499 (1200)
onayla = browser.find_element_by_id("MainContent_rptBasvurular_btnOnayla_2")
onayla.click()
time.sleep(3)

onaylama = browser.find_element_by_id("MainContent_rptBasvurular_btnOnaylama_2")
onaylama.click()
time.sleep(3)

#-----------------------For 5th Screen, Repeat other Scenarios-------------------------

#Iskender basvuru denemesi
url ="https://localhost:44378"
browser.get(url) #the site link
time.sleep(5)

#Hatasiz Devam
tutar2 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar2.send_keys("1010")
time.sleep(2)

basvur2 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur2.click()
time.sleep(2)

basvur2 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur2.click()

#Hatasiz Devam (File upload oluyor ama kaydet deyince kabul etmiyor)
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Alexander")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Great")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
gelirb.send_keys("1000")

time.sleep(2)
foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")                                   

kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
kvkk.click()

time.sleep(2)
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()


url ="https://localhost:44378/Pages/Basvurularim"
browser.get(url) #the site link
time.sleep(3)

belge_yukle = browser.find_element_by_id("MainContent_rptBasvurular_btnBelgeYukle_3")
belge_yukle.click()
time.sleep(3)


#Belge yok hatasi
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)

#Belgenizi yukleyiniz
belge_ekle = browser.find_element_by_id("MainContent_btnSatirEkle")
belge_ekle.click()
time.sleep(3)

time.sleep(2)
belge = browser.find_element_by_id("MainContent_fuBelge") #*
belge.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

belge = browser.find_element_by_id("MainContent_ddlBelgeler") #*
belge.send_keys("Faiz Geliri Belgesi") 

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)


#<1100 hatasi (1010)
onayla = browser.find_element_by_id("MainContent_rptBasvurular_btnOnayla_3")
onayla.click()
time.sleep(3)

onaylama = browser.find_element_by_id("MainContent_rptBasvurular_btnOnaylama_3")
onaylama.click()
time.sleep(3)


#Richy 1.basvuru
url ="https://localhost:44378"
browser.get(url) #the site link
time.sleep(5)

#Hatasiz Devam
tutar1 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar1.send_keys("1800")
time.sleep(2)

basvur1 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur1.click()
time.sleep(2)

basvur1 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur1.click()

#Hatasiz Devam (File upload oluyor ama kaydet deyince kabul etmiyor)
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Richie")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Rich")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
gelirb.send_keys("10000")

time.sleep(2)
foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")                                   

kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
kvkk.click()

time.sleep(2)
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()


url ="https://localhost:44378/Pages/Basvurularim"
browser.get(url) #the site link
time.sleep(3)

belge_yukle = browser.find_element_by_id("MainContent_rptBasvurular_btnBelgeYukle_4")
belge_yukle.click()
time.sleep(3)


#Belge yok hatasi
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)

#Belgenizi yukleyiniz
belge_ekle = browser.find_element_by_id("MainContent_btnSatirEkle")
belge_ekle.click()
time.sleep(3)

time.sleep(2)
belge = browser.find_element_by_id("MainContent_fuBelge") #*
belge.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

belge = browser.find_element_by_id("MainContent_ddlBelgeler") #*
belge.send_keys("Faiz Geliri Belgesi") 

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)


#1500-1900 (1800)
onayla = browser.find_element_by_id("MainContent_rptBasvurular_btnOnayla_4")
onayla.click()
time.sleep(3)


#Richy 2. basvuru
url ="https://localhost:44378"
browser.get(url) #the site link
time.sleep(5)

#Hatasiz Devam
tutar1 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar1.send_keys("2000")
time.sleep(2)

basvur1 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur1.click()
time.sleep(2)

basvur1 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur1.click()

#Hatasiz Devam (File upload oluyor ama kaydet deyince kabul etmiyor)
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Richie")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Rich")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
gelirb.send_keys("10000")

time.sleep(2)
foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")                                   

kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
kvkk.click()

time.sleep(2)
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()


url ="https://localhost:44378/Pages/Basvurularim"
browser.get(url) #the site link
time.sleep(3)

belge_yukle = browser.find_element_by_id("MainContent_rptBasvurular_btnBelgeYukle_5")
belge_yukle.click()
time.sleep(3)


#Belge yok hatasi
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)

#Belgenizi yukleyiniz
belge_ekle = browser.find_element_by_id("MainContent_btnSatirEkle")
belge_ekle.click()
time.sleep(3)

time.sleep(2)
belge = browser.find_element_by_id("MainContent_fuBelge") #*
belge.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

belge = browser.find_element_by_id("MainContent_ddlBelgeler") #*
belge.send_keys("Faiz Geliri Belgesi") 

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)


#2000
onayla = browser.find_element_by_id("MainContent_rptBasvurular_btnOnayla_5")
onayla.click()
time.sleep(3)


#3. basvuru Richy
url ="https://localhost:44378"
browser.get(url) #the site link
time.sleep(5)

#Hatasiz Devam
tutar1 = browser.find_element_by_id("MainContent_txtTutarUc")
tutar1.send_keys("2500")
time.sleep(2)

basvur1 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur1.click()
time.sleep(2)

basvur1 = browser.find_element_by_id("MainContent_btnBasvurUc")
basvur1.click()

#Hatasiz Devam (File upload oluyor ama kaydet deyince kabul etmiyor)
tcno = browser.find_element_by_id("MainContent_txtTc") #*
tcno.send_keys("98765432141")

ad = browser.find_element_by_id("MainContent_txtAd") # !
ad.send_keys("Richie")

soyad = browser.find_element_by_id("MainContent_txtSoyad") # !
soyad.send_keys("Rich")

eposta = browser.find_element_by_id("MainContent_txtEmail") #*
eposta.send_keys("akhaciog@gmail.com")

telno = browser.find_element_by_id("MainContent_txtTelefon") #*
telno.send_keys("5572526128")

dg = browser.find_element_by_id("MainContent_txtDgTarihi")  #* 
dg.send_keys("05011994")

gelirb = browser.find_element_by_id("MainContent_txtGelir") #*
gelirb.send_keys("10000")

time.sleep(2)
foto = browser.find_element_by_id("MainContent_fuResim") #*
foto.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

secim =browser.find_element_by_id("MainContent_ddlMeslekler")                  
#meslek =Select(secim)   #DROPDOWN LIST
#meslek.select_by_visible_text("Memur") 
secim.send_keys("Memur")                                   

kvkk = browser.find_element_by_id("MainContent_chckbxOnay")
kvkk.click()

time.sleep(2)
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()


url ="https://localhost:44378/Pages/Basvurularim"
browser.get(url) #the site link
time.sleep(3)

belge_yukle = browser.find_element_by_id("MainContent_rptBasvurular_btnBelgeYukle_6")
belge_yukle.click()
time.sleep(3)


#Belge yok hatasi
kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)

#Belgenizi yukleyiniz
belge_ekle = browser.find_element_by_id("MainContent_btnSatirEkle")
belge_ekle.click()
time.sleep(3)

time.sleep(2)
belge = browser.find_element_by_id("MainContent_fuBelge") #*
belge.send_keys("C://Users/Lenovo/Desktop/Vault/papyrus.jpg") #FILE UPLOAD

belge = browser.find_element_by_id("MainContent_ddlBelgeler") #*
belge.send_keys("Faiz Geliri Belgesi") 

kaydet = browser.find_element_by_id("MainContent_btnKaydet")
kaydet.click()
time.sleep(3)


#2500
onayla = browser.find_element_by_id("MainContent_rptBasvurular_btnOnayla_6")
onayla.click()
time.sleep(5)


browser.close()
