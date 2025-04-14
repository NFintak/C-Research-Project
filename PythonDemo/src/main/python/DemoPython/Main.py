class Main:
    def __init__(self):
        pass

    def exponential(self, n):
        # create your list of numbers
        lista = [1, 2, 3, 4, 5, 6, 7, 8]
        #empty list to hold results
        list3 = []
        #begin your loop
        for i in lista:
            list3.append(i ** n)
        #print the results
        print(list3)


    def remove_odds(self):
        #create your list of numbers
        lista = [1, 2, 3, 4, 5, 6, 7, 8]
        #setup your loop
        for item in lista:
            #remove items that are odd
            if item % 2 != 0:
                lista.remove(item)
            #print the results
            print(lista)


    def reverse(self, a):
        print (a[::-1])


    def palindrome(self, value ):
        #take value and clean it -- make all lowercase and remove spaces
        clean_input = value.lower().replace(" ", "")
        #reverse the clean string
        reversed_clean_input = reversed(clean_input)
        #place clean and reverse string into variables
        a = list(clean_input)
        b = list(reversed_clean_input)
        #print true if a == b
        print (a == b)





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
