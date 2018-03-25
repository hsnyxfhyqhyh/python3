import datetime

class User: 
    def __init__(self, full_name, dob):
        '''blah, blah'''

        self.name = full_name
        self.dob = dob  #yyyymmdd

        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self): 
        ''' to return the age of the user in integer of years'''
        today = datetime.date(2018, 3, 12)
        yyyy = int(self.dob[0:4])
        mm = int(self.dob[4:6])
        dd = int(self.dob[6:8])
        
        print (yyyy, mm, dd) 

        d = datetime.date(yyyy, mm, dd)

        age_in_days = (today - d).days
        age_in_years = age_in_days / 365

        return int(age_in_years)

    def doSomething(self): 
        return "do something"


user1 = User('Yinghui hu', '19751001')


print (user1.age())

print (user1.doSomething())