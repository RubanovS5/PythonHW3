from adress import Adress
from mailing import Mailing

to_address = Adress("033456", "Москва", "Улица Газопровод", "11", "56")
from_address = Adress("678902", "Мурманск", "Улица Стадионная", "10", "90")


mailing = Mailing (to_address, from_address, "SD06542", 678)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.flat}.Стоимость {mailing.cost} рублей.")