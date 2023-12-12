# your code goes here!

class Anagram:
    pass
    def __init__(self, word):
        self.word = word

    def match(self, words):
        result=[]
        pass
        for item in words:
            if sorted([letter for letter in self.word]) == sorted([letter for letter in item]):
                result.append(item)
                print(result)
            
        return result

test = Anagram("tab")
test.match(["meat","atb","bat"])
