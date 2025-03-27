# class Investment:
#     def __init__(self, amount, procent, years):
#         self._amount = amount
#         self._procent = procent / 100
#         self._years = years
    
#     def getInvestment(self):
#         return self._amount * (1 + self._procent * self._years)
    
#     def __str__(self):
#         return f"Investment: Amount={self._amount}, Procents={self._procent * 100}%, Years={self._years}, Sum={self.getInvestment()}"
    
#     def __lt__(self, other):
#         return self.getInvestment() < other.getInvestment()

#     def __gt__(self, other):
#         return self.getInvestment() > other.getInvestment()


# class CompoundInvestment(Investment):
#     def __init__(self, amount, procent, years, narax):
#         super().__init__(amount, procent, years)
#         self._narax = narax
    
#     def getInvestment(self):
#         return self._amount * (1 + self._procent / self._narax) ** (self._narax * self._years)
    
#     def __str__(self):
#         return (f"Compound Investment: Amount={self._amount}, Procent={self._procent * 100}%, Years={self._years}, Narax={self._narax} times, Sum={self.getInvestment()}")

# # Example usage
# investment1 = Investment(1000, 5, 3)  
# investment2 = Investment(15000, 4, 2)  

# print("investment1 < investment2",investment1 < investment2)  
# print("investment1 > investment2",investment1 > investment2)  
# print(investment1,investment2)

# compound_investment1 = CompoundInvestment(10000, 5, 3, 12) 
# compound_investment2 = CompoundInvestment(15000, 4, 2, 4) 
# print("compound_investment1 < compound_investment2",compound_investment1 < compound_investment2)
# print("compound_investment1 > compound_investment2",compound_investment1 > compound_investment2)
# print(compound_investment1,compound_investment2)


class TransportCompany:
    countOfvehicles = 0
    
    def __init__(self, name):
        self.name = name
        self.vehicles = {}

    @classmethod
    def change_name(cls, instance, new_name):
        instance.name = new_name
    
    @classmethod
    def count_vehicles(cls):
        return cls.countOfvehicles
    
    def add_vehicle(self, number, specs):
        self.vehicles[number] = specs
        TransportCompany.countOfvehicles += 1
    
    def get_vehicle(self, number):
        return self.vehicles.get(number, "Not found")
    
    def update(self, number, new_specs):
        if number in self.vehicles:
            self.vehicles[number] = new_specs
            return "Updated"
        return "Not found"


company = TransportCompany("Auto")
TransportCompany.change_name(company, "AutoNew")
print(company.name) 
company.add_vehicle("AAA1234", {"type": "Auto", "capacity": "2 tons"})
print(company.get_vehicle("AAA1234"))
company.update("AAA1234", {"type": "Auto", "capacity": "3 tons"})
print(company.get_vehicle("AAA1234"))
