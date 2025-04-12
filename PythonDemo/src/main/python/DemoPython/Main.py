class Main:
    def __init__(self):
        pass
    def exponential(self, n):
        lista = [1, 2, 3, 4, 5, 6, 7, 8]
        list3 = []
        for i in lista:
            list3.append(i ** n)
        print(list3)

    def user_input(self, message):
        pass


demo_exponent = Main()
demo_exponent.exponential(2)