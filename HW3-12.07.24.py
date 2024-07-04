class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def set_dollars(self, dollars):
        self.dollars = dollars

    def set_cents(self, cents):
        self.cents = cents

    def get_total(self):
        return self.dollars + self.cents / 100

    def __str__(self):
        return f"${self.dollars}.{self.cents:02d}"

money = Money(100, 50)
print(money)

money.set_dollars(200)
money.set_cents(75)
print(money)

total_amount = money.get_total()
print(f"Общая сумма: {total_amount}") 
