"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #7 - Anagram Validator (anagram.py)


Author: Paul Thai

Difficulty Level: 4/10

Background: Just like Paul, Chris doesn't have enough RAM in his brain to store information. 
As result he tends to forget some things just like his anagram password. 
Help Chris recover his anagram password by solving the puzzle. 

Prompt: An anagram is a word/phrase that is formed by rearranging the letters of a different work of phrase. 
Typically, these words consist of the original letters and are used once. Using two strings, 
find out if these are anagrams or not! Return True if it is an anagram and False if it is not!

Test Cases:
a = "anagram" ; b = "maranag" ; output = True
a = "tar" ; b = "car" ; output = False
a = "sad" ; b = "dsa" ; output = True
"""

class Solution:
    def anagram(self,a,b):
        # type a: string
        # type b: string
        # return type: bool
        for i in a:
            if i not in b:
                return False
        return True
        # TODO: Write code below to return a bool with the solution to the prompt
        pass

def main():
    string1 = input().strip()
    string2 = input().strip()

    tc1 = Solution()
    ans = tc1.anagram(string1, string2)
    print(ans)

if __name__ == "__main__":
    main()