class DocParser:
    def __init__(self, document:str):
        self.text = document

    def get_sentences(self) -> str:
        prev = ""
        for letter in self.text:
            if (letter != '\n'):
                prev += letter

            if (letter == '.'):
                temp = prev
                prev = ""
                yield temp 

    def search_sentences(self, search_key:str, case_sensitive=True) -> list:
        results = []
        for sentence in self.get_sentences():
            present = False
            
            if not case_sensitive:
                present = (search_key.lower() in sentence.lower())
            else:
                present = (search_key in sentence)

            if (present):
                results.append(sentence)

        return results 