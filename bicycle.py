class Bicycle(object):
    def __init__(self):
        self.weight = 100
        self.speed = 30
        self.color = "red"
        self.cost = 50
              
class Bikeshop(object):
    def __init__(self):
        self.name = "River City Cycle"
        self.models = ["BMX", "Mountain", "Fixed gear", "Road"]
      
class Customer(object):
    def __init__(person):
        person.name = ["Tom", "Dick", "Harry"]

Tom = Customer()
Dick = Customer()
Harry = Customer()

Tom.funds = 70
Dick.funds = 75
Harry.funds = 80