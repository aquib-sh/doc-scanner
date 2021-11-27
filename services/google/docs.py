import re
from services.google.service_builder import GoogleServices

class GoogleDocs(GoogleServices):
    """Handles Google Docs API events and methods.
    
    Inherited Parameters from GoogleServices
    -----------------------------------------
    token
        Token of the current session.

    scope: list
        Scope of the current token.
    """
    def __init__(self, token, scope: list):
       super().__init__(token, scope)

    def start_service(self, version='v1'):
        """Builds Google Docs Service."""
        return super().start_service("docs", version)

    def create_document(self, body:dict) -> str:
        """Creates a Google Document.
        
        Parameters
        ----------
        body: dict
            contains the details and body of the document
            contains {'title'}

        Returns
        --------
        document_id: str
            ID of the document just created by this method.
        """
        doc = self.service.documents().create(
            body=body
        ).execute()
        return doc['documentId']

    def __get_document_body(self, document_id:str):
        """Returns document body."""
        doc = self.service.documents().get(
            documentId=document_id).execute()
        return doc.get('body')

    def get_text_from_document(self, document_id:str) -> str:
        """Extracts text from the document

        Parameters
        ----------
        document_id: str
            id of Google Docs document.  
        """
        document = ""
        doc_content = self.__get_document_body(document_id)
        for content in doc_content['content']:
            if 'paragraph' in content:
                para = content['paragraph']
                elems = para['elements']
                for elem in elems:
                    document += elem['textRun']['content']
        return document

    def __get_id_from_link(self, link:str) -> str:
        """Extracts ID from link."""
        pattern = r"[https:\/\/]?docs\.google\.com\/document\/d\/(.*)\/edit"
        match = re.search(pattern, link)
        return match.group(1)

    def get_text_from_document_using_link(self, link:str) -> str:
        """Extracts text from the document using link as parameter

        Parameters
        ----------
        link: str
            link of Google Docs document.  
        """
        doc_id = self.__get_id_from_link(link)
        content =  self.get_text_from_document(doc_id)
        return content