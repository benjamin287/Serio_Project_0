
from abc import ABC, abstractmethod

class Location(ABC):
    def __init__(self, name, manager, employees, hours, customers):
        self._name = str(name)
        self._manager = str(manager)
        self._employees = int(employees)
        self._hours = int(hours)
        self._customers = int(customers)

    def __str__(self):
        return "Name: " + self._name + ", Manager: " + self._manager

class Retail(Location):
    pass

class Repair(Location):
    pass

class Admin(Location):
    pass
