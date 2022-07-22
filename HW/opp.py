from ctypes import addressof
from datetime import datetime as dt
class User():

    def __init__(self,first_name,last_name,email, id):  
       self.first_name = first_name
       self.last_name=last_name
       self.email=email
       self.id = id

class Employee(User):    

    def __init__(self, first_name, last_name, email,home_address, security_level, department, id):
        super().__init__(first_name, last_name, email, id,)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department
        self.created_on= dt.now().strftime("%c")   
        self.id = id
        


    def id(self):
        return self.full_name + self.department

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def new_first_name(self):
        return self.new_first_name
    @property
    def new_last_name(self):
        return self.new_last_name    
    @property
    def switch_departments(self):   
        return self.new_department

    def __str__(self):
        return f'<Employee | {self.full_name}>'
        
    def __hash__(self):
        return hash(self.last_name+self.created_on)


    def __reper__(self):
        return f'<Employee | {self.last_name} {self.created_on}>'

    def __hash__(self):
        return hash(self.full_name+ self.security_level)

class Customer(User):

    def __init__(self, first_name, last_name, email, shipping_address, billing_address, purchase_history,):
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_address=purchase_history
        self.created_on= dt.now().strftime("%c") 
        self.id = email + billing_address
        self.full_name=first_name + last_name
        
    @property
    def new_first_name(self):
        return self.new_first_name

    @property
    def new_last_name(self):
        return self.new_last_name  

    @property
    def new_shipping_address(self):
        return self.new_shipping_address   

    def __str__(self):
        return f'<Customer | {self.full_name}>'               

    def __reper__(self):
        return f'<Employee | {self.last_name} {self.crteated_on.strfttime("%c")}>'

    def __hash__(self):
        return hash(self.full_name+ self.shipping_address)
    

Amy_Morgan=Employee('Amy', 'Morgan', 'amy@gmail.com','444 Prinvceton rd', None,'Maintenance','Wed Jul 20 17:01:27 2022')
Joe_Secora=Employee('Joe','Secora','Joe@gmail.com','1090 Abbey Rd', None,'Sales','Tues Jul 20 15:01:25 2022')        
Frank_G=Employee('Frank','G','g@gmail.com', '543 Data Rd', None, 'Procurement','Tues Jul 20 13Tues:01:37 2022')
Olga_Smith=Customer('Olga','Smith', 'olga@gmial.com', '555 ave b', '555 ave b', 'Tues Jul 20 13Tues:09:27 2022')
Jack_Law=Customer('Jack', 'Law', 'jack@gmail', '111 Pelcian D','111 Pelcian D','Tues Jul 20 13Tues:11:00 2022')
Juan_Clavo=Customer('Juan', 'Clavo','clavo@gmail.com','123 Contera Rd','123 Contera Rd', 'Wed Jul 20 17:01:27 2022')

test=[Amy_Morgan.created_on,Joe_Secora.created_on,Frank_G.created_on,Olga_Smith.created_on,Jack_Law.created_on,Juan_Clavo.created_on]
print(sorted(test))
