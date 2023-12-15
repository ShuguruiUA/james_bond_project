# список контактів з ДН за наступні day днів.
# належить до класу class AddressBook
 
from datetime import datetime, timedelta



def find_birthday(self, day = 7):
    list_date = []
    today = datetime.now().date()
    end_birthday = today + timedelta(days=day)
    for record in self.data.values():
        next_birthday = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
        next_birthday = next_birthday.replace(year=today.year)
        if today > next_birthday:
            next_birthday = next_birthday.replace(year=today.year + 1)
        if today <= next_birthday and next_birthday <= end_birthday:
            list_date.append(record)
    return list_date

