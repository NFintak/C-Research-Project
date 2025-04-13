class Main:
    def __init__(self):
        pass

    def exponential(self, n):
        lista = [1, 2, 3, 4, 5, 6, 7, 8]
        list3 = []
        for i in lista:
            list3.append(i ** n)
        print(list3)


    def remove_odds(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8]
        for item in lista:
            if item % 2 != 0:
                lista.remove(item)
            print(lista)


    def reverse(self, a):
        print (a[::-1])


    def palindrome(self, value ):
        clean_input = value.lower().replace(" ", "")
        reversed_clean_input = reversed(clean_input)

        a = list(clean_input)
        b = list(reversed_clean_input)

        print (a == b)

    def greet(self, name):
        """
        This function receives a name parameter and utilizes it to print a greeting.
        """
        print("Hello, "+ name)

    def name_input(self):
        """
        This function prompts the user for their name and returns the value provided by the user.
        """
        return input("What is your name?\n")





#exponential
#demo_one = Main()
#demo_one.exponential(2)

#removeodds
#demo_two = Main()
#demo_two.remove_odds()

#reverse
#demo_three = Main()
#demo_three.reverse('applesauce')

#palnindrome
#demo_four = Main()
#demo_four.palindrome('Dog')
#demo_four.palindrome('Racecar')

#greet
#demo_five = Main()
#name = demo_five.name_input()
#demo_five.greet(name)