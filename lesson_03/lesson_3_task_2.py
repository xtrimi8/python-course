from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S23", "+79161234567"),
    Smartphone("Apple", "iPhone 15", "+79261234568"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79361234569"),
    Smartphone("Nokia", "G21", "+79461234570"),
    Smartphone("Huawei", "P60 Pro", "+79561234571")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
