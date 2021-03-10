import json

from car import Car
from client import Client
from rental import Rental
from management import CarManagement


def quick_client_status(cl):
    print(f"{cl.name} has rented {len(cl.cars)} cars.")
    print(f"{cl.name} balance: {cl.money}\n")


with open('cars.json') as json_cars:
    cars = json.load(json_cars)

management = CarManagement([Car.from_dict(car) for car in cars])
management.list_available_cars()

# client 1
ivo = Client('Ivo', 5000)
ivo_rental1 = Rental('EB8735AP', hours=4, days=1)
management.rent(ivo_rental1, ivo)
quick_client_status(ivo)

# client 2
eli = Client('Eli', 1790)
eli_rental1 = Rental('EB8735AP', hours=10)
eli_rental2 = Rental('PB3274TH', days=1)
eli_rental3 = Rental('PB5778TA', hours=1)
eli_rental4 = Rental('EB6783AP', weeks=1)
management.rent(
    [eli_rental1, eli_rental2, eli_rental3, eli_rental4],
    eli
)
quick_client_status(eli)
