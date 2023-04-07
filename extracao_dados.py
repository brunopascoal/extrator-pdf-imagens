# Importa os módulos necessários
import pytesseract
from PIL import Image
import pandas as pd
import re
import os
import fnmatch


# Função para processar e extrair dados das imagens
def teste(caminho):
    caminho_da_pasta = caminho
    arquivos_na_pasta = os.listdir(caminho_da_pasta)
    arquivos_png = fnmatch.filter(arquivos_na_pasta, '*.png')
    caminho_imagens = []

    # Cria uma lista com o caminho completo das imagens
    for arquivo in arquivos_png:
        caminho_imagens.append(caminho + arquivo)

    # Chama a função de extração de imagens
    extracao_imagens(caminho_imagens, caminho_da_pasta)


# Função para extrair informações das imagens e salvar em um arquivo Excel
def extracao_imagens(caminho_imagens, caminho_da_pasta):
    # Define o caminho do executável Tesseract-OCR
    caminho = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Cria um DataFrame vazio para armazenar os dados extraídos
    df_geral = pd.DataFrame()

    # Processa cada imagem no caminho das imagens
    for imagens in caminho_imagens:
        # Abre a imagem
        imagem = Image.open(imagens)
        # Extrai o texto da imagem
        pytesseract.pytesseract.tesseract_cmd = caminho
        texto = pytesseract.image_to_string(imagem)

        linhas = texto.split("\n")
        parceiro = None
        i = 0

        # Processa cada linha de texto extraída da imagem
        for linha in linhas:
            i += 1
            if not linha.isspace() and len(linha) > 0:
                if linha.startswith('Parceiro'):
                    parceiro = linha[9:]
                if (linha[2] == "/"):
                    texto = linha
                    colunas = texto.split(" ")

                    # Tenta extrair os dados das colunas
                    try:
                        data_inicio = colunas[0]
                        hora_inicio = colunas[1]
                        data_fim = colunas[2]
                        hora_fim = colunas[3]
                        nome_usuario = colunas[4]

                        # Criando um DataFrame com os dados
                        dados = {'Data Início': data_inicio,
                                 'Hora Início': hora_inicio,
                                 'Data Fim': data_fim,
                                 'Hora Fim': hora_fim,
                                 'Nome de Usuário': nome_usuario,
                                 'Parceiro': parceiro}

                        # Adiciona os dados ao DataFrame geral
                        df_geral = df_geral.append(dados, ignore_index=True)

                    except:
                        pass

    # Salva o DataFrame em um arquivo Excel
    df_geral.to_excel(caminho_da_pasta + "\\Arquivos.xlsx")
