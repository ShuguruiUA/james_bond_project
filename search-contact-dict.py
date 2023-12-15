from collections import UserDict

class AddressBook(UserDict):
   

    def find(self, name):
        return self.data.get(name)