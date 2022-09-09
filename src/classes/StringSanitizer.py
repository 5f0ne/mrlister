class StringSanitizer():
    
    def __init__(self):
        self.__punctuation = [".", ",", "!", "?", ":", ";"]
        self.__brackets = ["{", "}", "[", "]", "(", ")"]
    
    def sanitize(self, string):
        string = self.removePunctuation(string)
        string = self.removeBrackets(string)
        return string
    
    def removePunctuation(self, string):
        return self.__remove(string, self.__punctuation)
    
    def removeBrackets(self, string):
        return self.__remove(string, self.__brackets)
        
    def __remove(self, string, list):
        for l in list:
            string = string.replace(l, "")
        return string