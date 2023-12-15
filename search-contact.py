# при умові, що в контакти збережені як список словників

class AddressBook:

    def find(self, name):
        for info in self.data:          
            if info.get('name') == name:
                return info                #info - інформація про контакт за ім'ям 
        return None