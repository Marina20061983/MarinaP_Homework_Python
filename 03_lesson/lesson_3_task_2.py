from smartphone import Smartphone

catalog = []

catalog.append(Smartphone(
    brand="Apple", model="iPhone 15", phone_number="+79123456789"
))
catalog.append(Smartphone(
    brand="Samsung", model="Galaxy S24", phone_number="234567890"
))
catalog.append(Smartphone(
    brand="Xiaom", model="Mi 13", phone_number="+79345678901"
))
catalog.append(Smartphone(
    brand="Google", model="Pixel 8", phone_number="+79456789012"
))
catalog.append(Smartphone(
    brand="OnePlusl", model="11", phone_number="+79567890123"
))

for smartphone in catalog:
    print(
        f"{smartphone.brand} - {smartphone.model} "
        f"{smartphone.phone_number}"
    )
