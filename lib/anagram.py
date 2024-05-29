# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        list_of_individual_letters = [letter for letter in self.word]
        # print(list_of_individual_letters)
        possible_word = []
        for word in possible_anagrams:
                 possible_value = [x for x in word]
                 if sorted(possible_value) == sorted(list_of_individual_letters):
                     word = "".join(possible_value)
                     possible_word.append(word)
                     
        return possible_word          

            
        
                
                
        