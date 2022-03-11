class Market:
    def __init__(self):
        self.__amount= 200

    def viewvegetableamount(self):
        print(self.__amount)

    def hikeamount(self,amount):
        self.__amount=amount

Vegetableamount = Market()
Vegetableamount.viewvegetableamount()

Vegetableamount.__amount = 300
Vegetableamount.viewvegetableamount()

Vegetableamount.hikeamount(1000)
Vegetableamount.viewvegetableamount()