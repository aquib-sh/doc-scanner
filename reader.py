import json

class InputReader:

    def __init__(self, filename:str):
        self.input_file = filename
        self.__fp = open(self.input_file)
        self.data = {} 

    def read(self):
        self.data = json.load(self.__fp)

    def get_row(self) -> tuple:
        """Returns input one value at a time

        Returns
        -------
        row: tuple
            returns a tuple in the form of (link:str, keywords:tuple, case_sensitive:bool) 
        """
        for item in self.data:
            link = self.data[item]['link']
            keywords = tuple(self.data[item]['keywords'])
            case = self.data[item]['case_sensitive']
            row = (link, keywords, case)
            yield row


    

    
    
        
    