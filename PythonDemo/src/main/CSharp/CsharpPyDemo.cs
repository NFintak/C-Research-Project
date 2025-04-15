//using classes from System
using System;
using System.Collections.Generic;

class Utility
{
    
        static void Main(string[] args)
    {
        Utility utility = new Utility();

        // Testing Exponentiator
        List<double> doubleNumbers = new List<double> { 2, 3, 4, 5 };
        double exponent = 2;
        utility.Exponentiator(doubleNumbers, exponent);

        // Testing RemoveOdds
        List<int> intNumbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        utility.RemoveOdds(intNumbers);

        // Testing Palindrome
        string str1 = "madam";
        utility.Palindrome(str1);

        // Testing Reverse
        string original = "Hello, World!";
        utility.Reverse(original);
    }
    
    public void Exponentiator(List<double> numbers, double exponent)
    {   //create a new list called results
        List<double> results = new List<double>();
        //foreach loop
        foreach (double number in numbers)
        {
            //add numbers after being raised by exponent
            results.Add(Math.Pow(number, exponent));
        }
        Console.WriteLine(string.Join(", ", results));
    }

    public void RemoveOdds(List<int> numbers)
    {   // a new list called even numbers where 
        List<int> evenNumbers = numbers.Where(n => n % 2 == 0).ToList();
        
        Console.WriteLine(string.Join(", ", evenNumbers));
    }

    public void Palindrome(string str)
    {
        char[] cArray = str.ToCharArray();
        Array.Reverse(cArray);
        string reversedStr = new string(cArray);
        bool isPalindrome = str.Equals(reversedStr, StringComparison.OrdinalIgnoreCase);
        Console.WriteLine(isPalindrome);
    }

    public void Reverse(string s)
    {   // the input string is turned into an array of chars and placed in charArray
        char[] charArray = s.ToCharArray();
        // reverse method is done on charArray
        Array.Reverse(charArray);
        // creates a new string  out of the reversed array of chars
        string reversed = new string(charArray);
        Console.WriteLine(reversed);
    }


    
    
}
