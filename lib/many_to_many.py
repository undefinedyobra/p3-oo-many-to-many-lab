
# many_to_many.py

class Author:
    pass
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class.")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    pass
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    pass
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author class.")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class.")
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add this contract to the author's and book's contract lists
        author._contracts.append(self)
        book._contracts.append(self)

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]