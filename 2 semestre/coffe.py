class Coffee:
    def __init__(self, name, price):
        self.name= name
        self.price = float(price)
    
    def check_budget(self, budget):
        if not isinstance(budget(int, float)):
            print("enter float or int")
            exit()
        if budget < 0:
            print ("sorry you don\' have money")
            exit()

    def get_chance(self, budget):
        return budget -self.price
    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f'you can buy the {self.name} coffee')
            if budget == self.price:
                print('it\'s complete')
            else:
                print(f'here is your change {self.get_chance(budget)}$')

small= Coffee('small',2)
regular=Coffee('regular',5)
big=Coffee('big',6)

try:
    user_budget= float(input('what is your budget? '))
except ValueError:
    exit ('please enter a number ')

for coffee in [big, regular, small]:
    coffee.sell (user_budget )