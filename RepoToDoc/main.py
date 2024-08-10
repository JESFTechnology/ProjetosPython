import requests
import time
import re
from bs4 import BeautifulSoup

# Faz a requisição para o link
periodo = None
url = input("Insira o GIT: ")
nome = input("Insira o nome do arquivo (Obrigatório): ")
nomePessoal = input("Insira o nome: ")
email = input("Insira o email: ")
faculdade = input("Insira a escola: ")
if faculdade:
    periodo = input("Insira o periodo ou ano: ")

text_document = ""

response = requests.get(url)


def texto_para_arquivo(texto, nome_arquivo):
    with open(nome_arquivo + ".txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)


nome_arquivo = f"{nome}"

try:

    def replace_tree_with_blob(url2):
        url2 = re.sub(
            r"https://github.com/",
            "https://raw.githubusercontent.com/",
            url2,
        )

        url2 = re.sub(
            r"tree/main",
            "main",
            url2,
        )

        return url2

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parseia o HTML com BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Encontra todos os elementos td com a classe "react-directory-row-name-cell-small-screen"
        elements = soup.find_all(
            "td", class_="react-directory-row-name-cell-small-screen"
        )

        if elements == None or elements == []:
            print("Não foi possível encontrar o conteúdo do arquivo")
            print("---- Operação cancelada ----")
            print(response.content)
        else:
            print("Iniciando produção...")
            # Encontra os links dentro desses elementos
            if nomePessoal:
                text_document = "Nome: " + nomePessoal + "\n"
            if email:
                text_document += "Email: " + email + "\n"
            if faculdade:
                text_document += "Escola/Faculdade: " + faculdade + "\n"
            if periodo:
                text_document += "Ano/Período: " + periodo + "\n"
            for element in elements:
                link = element.find("a", class_="Link--primary")
                nome_atividade = str(link.get_text())

                new_url = replace_tree_with_blob(url)
                new_url2 = new_url + "/" + nome_atividade

                print("Atividade: ", nome_atividade, " sendo feita...")

                time.sleep(3)

                text_document += "\n\n" + nome_atividade + "\n"
                response2 = requests.get(new_url2)

                if response2.status_code == 200:
                    soup2 = BeautifulSoup(response2.content, "html.parser")
                    text_document += str(soup2.get_text())
                    print("Obtendo texto da atividade...")
                    time.sleep(2)
            texto_para_arquivo(text_document, nome_arquivo)
            print("Arquivo salvo com sucesso!")
    else:
        print("Erro ao fazer a requisição 2: ", str(response.status_code))
except Exception as e:
    print("Erro ao fazer a requisição: ", str(e))
