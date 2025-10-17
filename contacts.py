class contact_system():
    print(choose the option
                1.add contact
                2.update contact
                3.list of contacts
                4.exit)
    
    option=int(input("enter the number u want to select"))
    if option==1:
            def add_contact(self):
            
                name=input()
                mailid=input()
                mobileno=int(input())
                print(self.name,self.mailid,self.mobileno)

a=contact_system()
a.add_contact()
class contact:
    def __init__(self,name,phone_number,email):
        self.name=name
        self.phone_number=phone_number
        self.email=email
    def __str__(self):
        return f"Name: {self.name},phone