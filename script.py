import requests
from bs4 import BeautifulSoup

# Função para pegar o link da página que gera o Delta Key
def obter_link_gerado(url):
    try:
        # Faz uma requisição GET à página que gera o link
        resposta = requests.get(url)
        
        # Se a resposta foi bem-sucedida
        if resposta.status_code == 200:
            # Parse da página com BeautifulSoup
            soup = BeautifulSoup(resposta.text, 'html.parser')
            
            # Aqui você precisa identificar qual é o elemento HTML que contém o link
            # Vamos supor que o link esteja dentro de uma tag <a> com a classe 'key-link'
            link = soup.find('a', class_='key-link')
            
            if link:
                return link['href']  # Retorna o atributo href (URL)
            else:
                print("Link não encontrado na página.")
                return None
        else:
            print("Erro ao acessar a página.")
            return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

# Função principal para rodar o script
def main():
    # Pede o link gerado para o usuário
    url_pagina = input("Digite o link gerado pelo Delta: ")  # Solicita o link no terminal
    
    # Tenta obter o link gerado
    link_gerado = obter_link_gerado(url_pagina)
    
    if link_gerado:
        print(f"Link gerado: {link_gerado}")
        chave = obter_chave(link_gerado)
        
        if chave:
            # Salva a chave no arquivo delta_key.txt
            with open("delta_key.txt", "w") as f:
                f.write(chave)
            print("Chave obtida e salva com sucesso!")
        else:
            print("Não foi possível obter a chave.")
    else:
        print("Não foi possível obter o link gerado.")

if __name__ == "__main__":
    main()
