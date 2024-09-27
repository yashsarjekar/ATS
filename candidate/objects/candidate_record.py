
class CandidateRecord:

    def __init__(self, id, name, age, gender, email, phone_number) -> None:
        self.__id = id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__email = email
        self.__phone_number = phone_number

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_gender(self):
        return self.__gender
    
    def get_email(self):
        return self.__email
    
    def get_phone_number(self):
        return self.__phone_number