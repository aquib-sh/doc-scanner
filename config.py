import os

data_dir = os.path.join(os.getcwd(), "internal")
# ======================= CACHE FILE  =============================
cache_file = "cache.json"
cache_path = os.path.join(data_dir, cache_file)
# ======================= INPUT FILE  =============================
input_file = "input.json"
# ======================= GOOGLE APIs =============================
google_token_file  = 'token.json'
client_secret_file = 'client_secret.json'

client_secret_path    = os.path.join(data_dir, client_secret_file)
google_api_token_path = os.path.join(data_dir, google_token_file)

google_api_scope = ['https://www.googleapis.com/auth/gmail.readonly',
                    'https://www.googleapis.com/auth/documents']
