class Bill:
    """
    data about the bill, the amount and the billing period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    name and number of days lived as fields and pay method
    """

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def pay(self, bill, other_flatmate):
        return bill.amount * (self.days / (self.days + other_flatmate.days))
