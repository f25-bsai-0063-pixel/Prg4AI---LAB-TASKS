#Lab Task 3

class cash_payment:
    def pay():
        print("cash payment")


class card_payment(cash_payment):
    def pay():
        print("Card payment")


Cash = cash_payment
Card = card_payment
l = [Cash, Card]

for i in l:
    i.pay()
