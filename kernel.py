import config
from services.google.token import TokenRetriever
from services.google.docs import GoogleDocs

class DocsKernel:

   def __init__(self):
        retriever = TokenRetriever() 
        self.__token = retriever.retrieve_google_api_token(
           config.google_api_token_path, 
           config.google_api_scope
        )
        self.docs = GoogleDocs(self.__token, config.google_api_scope)
        self.docs_service = self.docs.start_service()

   def fetch_document_text(self, link:str) -> str:
      raw_text = self.docs.get_text_from_document_using_link(link)
      return raw_text