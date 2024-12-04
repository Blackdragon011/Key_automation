import requests
import time

# Função para obter a chave do link fornecido
def obter_chave(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            chave = resposta.text.strip()
            return chave
        else:
            print("Erro ao acessar o link.")
            return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

# Função principal para rodar o script
def main():
    url = "https://link-do-delta-key"  # Substitua pelo link correto
    chave = obter_chave(url)
    
    if chave:
        # Salva a chave no arquivo delta_key.txt
        with open("delta_key.txt", "w") as f:
            f.write(chave)
        print("Chave obtida e salva com sucesso!")
    else:
        print("Não foi possível obter a chave.")

if __name__ == "__main__":
    main()
