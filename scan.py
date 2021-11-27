import datetime
import config
from kernel import DocsKernel
from parser import DocParser
from reader import InputReader

class Main:
    def __init__(self):
        self.intro = """
         _____________________________
        |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
        |$$$| GOOGLE DOCS SCANNER |$$$|
        |$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
        \n\n
        """
        self.kernel = DocsKernel()
        self.reader = InputReader(config.input_file)
        self.reader.read()

    def make_result(self, link:str, keyword:str, results:list) -> str:
        LINE_WIDTH = 100
        today = str(datetime.datetime.now()).split(".")[0]
        text = f"SCANNED FROM: {link}\nKEYWORD: {keyword}\nSCAN DATETIME: {today}\n\n"

        for result in results:
            text += result
            text += "\n"
            text += "====="*10
            text += "\n\n"
        return text
        
    def run(self):
        print(self.intro)
        LINE_SEPERATOR = "==="*10
        for row in self.reader.get_row():
            link, keywords, sensitive = row

            response = self.kernel.fetch_document_text(link)
            parser = DocParser(response)

            for keyword in keywords:
                print(f"Document: {link}\nKeyword: {keyword}\nCase Sensitive: {sensitive}")
                now = str(datetime.datetime.now().date())  #current date&time
                results = parser.search_sentences(keyword, sensitive)  
                out_text = self.make_result(link, keyword, results)

                # Add current datetime to title to distinguish it incase of duplication
                title = f"{keyword}_{now}"
                # Create document on Google Docs using the title and text
                self.kernel.create_document(title, out_text)
                print(f"Document {title} sucessfully created!\n{LINE_SEPERATOR}")

if __name__ == "__main__":
    program = Main()
    program.run()