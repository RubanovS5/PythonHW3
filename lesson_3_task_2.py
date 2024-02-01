from smartphone import Smartphone


Phone1 = Smartphone ("Iphone", "15pro", "+7899-422-45-33")
Phone2= Smartphone ("Xiaomi", "12X", "+7299-467-05-13")
Phone3 = Smartphone ("Iphone", "XR", "+7899-666-12-33")
Phone4 = Smartphone ("Samsung", "S24+", "+7333-002-45-00")
Phone5 = Smartphone ("Iphone", "12", "+7849-143-43-03")




catalog = [Phone1,Phone2,Phone3,Phone4,Phone5]

for phone in catalog:
    print(f"{phone.brandPhone} - {phone.modelPhone} - {phone.numberPhone}")

