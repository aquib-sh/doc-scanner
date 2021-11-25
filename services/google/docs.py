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
        super().start_service("docs", version)

