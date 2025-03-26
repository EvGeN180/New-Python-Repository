class Ticket:
    def __init__(self, fromTo, price):
        self.__fromTo = fromTo
        self.__price = price
        self.__is_available = True

    def get_ticket(self):
        return self.__fromTo, self.__price, self.__is_available
    
    def book(self):
        if self.__is_available:
            self.__is_available = False
            return "Квиток заброньовано."
        return "Квиток недоступний."
    
    def is_available(self):
        return self.__is_available
    
    def get_fromTo(self):
        return self.__fromTo


class TransportSystem:
    def __init__(self):
        self.__tickets = []  
    
    def add_ticket(self, fromTo, price):
        self.__tickets.append(Ticket(fromTo, price))

    def find_tickets(self, fromTo):
        return [t for t in self.__tickets if fromTo in t.get_ticket() and t.is_available()]
    
    def book_ticket(self, fromTo):
        for ticket in self.__tickets:
            if fromTo in ticket.get_ticket() and ticket.is_available():
                return ticket.book()
        return "Немає доступних квитків на цей маршрут."
    
ticket1 = Ticket("Київ-ІФ", 1500)
print(ticket1.get_ticket())
print(ticket1.is_available())

system = TransportSystem()
system.add_ticket("Київ-ІФ", 1500)

print(system.book_ticket("Київ-ІФ")) 
print(system.book_ticket("Київ-ІФ"))
