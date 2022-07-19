
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
    def Emp_Util(self):
        if self._hours == (self._employees - 2) * 20 + 80:
            print("\nGreat! Employee Utilization at 100%")
        elif self._hours / ((self._employees - 2) * 20 + 80) < 0.80:
            print("\nWARNING! Employee Utilization at " + ("%.2f" % ((self._hours / ((self._employees - 2) * 20 + 80))*100))+ "%! Continued under utilization may result in position reduction!")
        elif self._hours / ((self._employees - 2) * 20 + 80) > 1.10:
            print("\nWARNING! Employee Utilization at " + ("%.2f" % ((self._hours / ((self._employees - 2) * 20 + 80))*100)) + "%! Carefully manage overtime!")
        else:
            print("\nEmployee Utilization at an acceptable amount" + ("%.2f" % ((self._hours / ((self._employees - 2) * 20 + 80))*100)) + "%!")

    def Hours_Eff(self):
        if self._customers == (self._hours / 2):
            print("\nGreat! Work Effeciency at 100%")
        elif self._customers / (self._hours / 2) < 0.80:
            print("\nWARNING! Work Effeciency at " + ("%.2f" % ((self._customers / (self._hours / 2) )*100))+ "%! Make more sales or reduce hours!")
        elif self._customers / (self._hours / 2) > 1.10:
            print("\nFANTASTIC! Work Effeciency at " + ("%.2f" % ((self._customers / (self._hours / 2) )*100)) + "%! Continured over performance may result in position expansion!")
        else:
            print("\nEmployee Utilization at an acceptable amount" + ("%.2f" % ((self._customers / (self._hours / 2))*100)) + "%!")


class Repair(Location):
    def Emp_Util(self):
        if self._hours == (self._employees - 2) * 40 + 40:
            print("\nGreat! Employee Utilization at 100%")
        elif self._hours / ((self._employees - 2) * 40 + 40) < 0.80:
            print("\nWARNING! Employee Utilization at " + ("%.2f" % ((self._hours / ((self._employees - 2) * 40 + 40))*100))+ "%! Continued under utilization may result in position reduction!")
        elif self._hours / ((self._employees - 2) * 40 + 40) > 1.10:
            print("\nWARNING! Employee Utilization at " + ("%.2f" % ((self._hours / ((self._employees - 2) * 40 + 40))*100)) + "%! Carefully manage overtime!")
        else:
            print("\nEmployee Utilization at an acceptable amount" + ("%.2f" % ((self._hours / ((self._employees - 2) * 40 + 40))*100)) + "%!")
    def Hours_Eff(self):
        if self._customers == (self._hours / 10):
            print("\nGreat! Work Effeciency at 100%")
        elif self._customers / (self._hours / 10) < 0.80:
            print("\nWARNING! Work Effeciency at " + ("%.2f" % ((self._customers / (self._hours / 10) )*100))+ "%! Find more repairs or reduce hours!")
        elif self._customers / (self._hours / 10) > 1.10:
            print("\nFANTASTIC! Work Effeciency at " + ("%.2f" % ((self._customers / (self._hours / 10) )*100)) + "%! Continured over performance may result in position expansion!")
        else:
            print("\nWork Effeciency at an acceptable amount" + ("%.2f" % ((self._customers / (self._hours / 10))*100)) + "%!")

class Admin(Location):
    def Emp_Util(self):
        if self._hours / self._employees == 40:
            print("\nGreat! Employee Utilization at 100%")
        else:
            print("\nWARNING! Employee Utilization at " + ("%.2f" % (((self._hours / self._employees)/40)*100)) + "%! Please ensure employees are working their specified number of hours!")
    def Hours_Eff(self):
        print("\nNo effciency rating for Admin Locations...")
