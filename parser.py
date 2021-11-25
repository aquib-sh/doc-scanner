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

    def search_sentences(self, search_key:str) -> list:
        results = []
        for sentence in self.get_sentences():
            if search_key in sentence:
                results.append(sentence)
        return results 