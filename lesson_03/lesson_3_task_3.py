from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Тверская", "10", "25")
from_addr = Address("654321", "Санкт-Петербург", "Невский", "5", "12")

mail = Mailing(to_addr, from_addr, 350, "TRK123456789")

from_str = (
    f"{mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - "
    f"{mail.from_address.apartment}"
)

to_str = (
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}"
)

print(
    f"Отправление {mail.track} из {from_str} "
    f"в {to_str}. Стоимость {mail.cost} рублей."
)
