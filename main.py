from collections import UserDict
from datetime import datetime

class Field:
    
    def __init__(self, value):
        self.__value = value
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.__value = value
    
    def is_valid(self, value):
        return True

    def __str__(self):
        return str(self.value)

class Name(Field):

    def __init__(self, value):
        super().__init__(value)
        pass


class Phone(Field):
    
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Wrong phone number format")
        if True:
            super().__init__(value)
    

    def is_valid(self, value):    
        return isinstance(value, str) and len(value) == 10 and value.isdigit()

    

class Birthday(Field):

    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Wrong date format")
        if True:
            super().__init__(value)
        

    def is_valid(self, value):
        return datetime.strptime(value,'%Y-%m-%d')

            



class Record:
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for elem in self.phones:
            if elem.value == phone:
                self.phones.remove(elem)
                return phone
        raise ValueError(f'this phone is not exist in {self.name.value}')

    def edit_phone(self, old_phone, new_phone ):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for elem in self.phones:
            if elem.value == phone:
                return elem
            
    def days_to_birthday(self):
        if self.birthday.value is None:
            return "No birthaday entered"
        else:
            current_datetime = datetime.now()
            year, month, day = [int(i) for i in self.birthday.value.split('-')]
            contact_birthday = datetime(year=current_datetime.year, month=month, day=day)
            if contact_birthday > current_datetime:
                result = contact_birthday - current_datetime
            else:
                contact_birthday = datetime(year=current_datetime.year + 1, month=month, day=day)
                result = contact_birthday - current_datetime
            return f'{result.days} days left'
        


    def __repr__(self):
        if self.birthday.value == None:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"


class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
                raise KeyError("Already exists")
        self.data[record.name.value] = record

    def find(self, record):
        for key, value in self.data.items():
            if key == record:
                return value

    def delete(self, record):
        if record in self.data:
            self.data.pop(record)

    
    def iterator(self,N):
        current_index = 0
        my_list = []
        for elem in self.data.values():
            my_list.append(elem)
        while current_index < len(my_list):
            yield my_list[current_index:current_index + N]
            current_index += N




            

