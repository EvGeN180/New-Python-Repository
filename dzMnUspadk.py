# class Item:
#     def __init__(self, id, title, created_at):
#         self.__id = id
#         self.__title = title
#         self.__created_at = created_at

#     def get_title(self):
#         return self.__title
    
#     def get_id(self):
#         return self.__id
    
#     def get_created_at(self):
#         return self.__created_at

# class Searchable(Item):
#     def __init__(self, id, title, created_at):
#         super().__init__(id, title, created_at)
    
#     def search(self, query):
#         return query in self.get_title()

# class Printable:
#     def print_info(self):
#         print(self.get_title(), self.get_id(), self.get_created_at())

# class Book(Searchable, Printable):
#     def __init__(self, id, title, created_at, author, isbn):
#         super().__init__(id, title, created_at)
#         self.__author = author
#         self.__isbn = isbn

#     def get_author(self):
#         return self.__author
    
#     def get_isbn(self):
#         return self.__isbn
    
#     def print_info(self):
#         super().print_info()
#         print(self.get_author(),self.get_isbn())

       
# class Magazine(Searchable, Printable):
#     def __init__(self, id, title, created_at, issue_number, publisher):
#         super().__init__(id, title, created_at)
#         self.__issue_number = issue_number
#         self.__publisher = publisher

#     def get_issue_number(self):
#         return self.__issue_number
    
#     def get_publisher(self):
#         return self.__publisher
#     def print_info(self):
#         super().print_info()
#         print(self.get_issue_number(),self.get_publisher())


# class Library:
#     def __init__(self):
#         self.__items = []

#     def add_item(self, item):
#         self.__items.append(item)
    
#     def remove_item(self, item_id):
#         for item in self.__items:
#             if item.get_id() == item_id:
#                 self.__items.remove(item)

#     def searchItems(self, query):
#         search = []
#         for item in self.__items:
#             if item.search(query):
#                 search.append(item)
#         if search:
#             for item in search:
#                 item.print_info()
#         else:
#             print("Dont found items")

#     def list_all(self):
#         for item in self.__items:
#             Printable.print_info(item)

# class AudioBook(Book):
#     def __init__(self, id, title, created_at, author, isbn, duration):
#         super().__init__(id, title, created_at, author, isbn)
#         self.__duration = duration

#     def get_duration(self):
#         return self.__duration
    
#     def print_info(self):
#         super().print_info()
#         print(self.get_duration())



# book = Book(1, "Book", "2024", "unknown", "12")
# # book.print_info()
# magazine = Magazine(2, "Magazine", "2000", 12, "jj")
# # magazine.print_info()
# audiobook = AudioBook(3, "Audio", "2011", "Author", "11", 60)
# # audiobook.print_info()


# library = Library()
# library.add_item(book)
# library.add_item(magazine)
# library.add_item(audiobook)
# library.remove_item(1)
# # library.list_all()
# library.searchItems("Au")





# Створіть три класи:
# 1. Клас "Тварина" з методом "голос"
# 2. Клас "Домашня" з методом "ім'я"
# 3. Клас "Кіт", який наслідується від обох класів

# Вимоги до завдання:
# - Клас "Тварина" повинен мати метод "голос", який повертає рядок "Невідомий звук"
# - Клас "Домашня" повинен мати метод "ім'я", який приймає ім'я тварини і зберігає його
# - Клас "Кіт" повинен наслідуватися від обох класів та перевизначати метод "голос", 
#   щоб він повертав "Мяу"
# - Створіть об'єкт класу "Кіт", задайте йому ім'я і викличте обидва методи

# Приклад очікуваного результату:
# кіт = Кіт("Мурчик")
# print(кіт.ім'я()) # Виведе: "Мурчик"
# print(кіт.голос()) # Виведе: "Мяу"


class Animal:
    def sound(self):
        return "Невідомий звук"

class Pet:
    def __init__(self, name):
        self._name = name
    
    def name(self):
        return self._name

class Cat(Animal, Pet):
    def __init__(self, name):
        Pet.__init__(self, name)
    
    def sound(self):
        return "Мяууууу"

cat = Cat("Муркотик")
print(cat.name())
print(cat.sound()) 