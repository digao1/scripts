import os
from cryptography.fernet import Fernet

# Função para gerar e salvar uma chave
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Função para carregar a chave
def load_key():
    return open("secret.key", "rb").read()

# Função para criptografar arquivos
def encrypt_file(file_path, fernet):
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Diretório alvo
target_directory = "caminho/para/seu/diretorio"

# Gera uma nova chave e carrega a chave
# key = generate_key()  # Descomente se quiser gerar uma nova chave
key = load_key()
fernet = Fernet(key)

# Criptografa arquivos em todas as pastas do diretório
for foldername, subfolders, filenames in os.walk(target_directory):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        encrypt_file(file_path, fernet)
        print(f'Arquivo criptografado: {file_path}')

print("Todos os arquivos foram criptografados.")
