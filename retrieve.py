import config
from services.google.token import TokenRetriever

retriever = TokenRetriever()

token = retriever.retrieve_google_api_token(
    config.google_api_token_path, 
    config.google_api_scope
)

print(token)
