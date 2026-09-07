class Library:
    def __init__(self,name):
        self.name=name

    def issue_book(self):
        print(self.name," Issued\n")


class Book(Library):
    def issue_book(self):
        print("Book : ",self.name," issued\n")


class Magazine(Library):
    def issue_book(self):
        print("Magazine : ",self.name," issued\n")


class Journal(Library):
    def issue_book(self):
        print("Journal : ",self.name," issued\n")


items=[Book("Concept of Physics"),Magazine("Frobes"),Journal("Nature")]
for item in items:
    item.issue_book()