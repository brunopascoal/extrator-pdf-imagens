# Importa a função convert_from_path do módulo pdf2image
from pdf2image import convert_from_path
# Importa a função teste do módulo extracao_dados_sankhya
from extracao_dados import teste

# Função para converter um arquivo PDF em imagens
def converter_pdf_para_imagem(caminho_pdf, caminho_imagem, formato="png"):
    # Converte o arquivo PDF em uma lista de imagens
    imagens = convert_from_path(caminho_pdf)
    i = 0
    # Salva cada página do PDF como uma imagem
    for i, imagem in enumerate(imagens):
        imagem.save(f"{caminho_imagem}/pagina_{i + 1}.{formato}", formato)
        i += 1
    print(f"Foram geradas {i} imagens...")

# Se o script for executado diretamente
if __name__ == "__main__":
    # Solicita ao usuário o caminho completo do arquivo PDF
    caminho_pdf = input("Digite o caminho completo do PDF")
    print(caminho_pdf[1:-1])
    # Solicita ao usuário o caminho completo de onde as imagens serão geradas
    caminho_imagem = input("Digite o caminho completo de onde as imagens serão geradas")
    # Converte o PDF em imagens e salva-as no caminho especificado
    converter_pdf_para_imagem(caminho_pdf[1:-1], caminho_imagem)
    # Chama a função teste do módulo extracao_dados_sankhya, passando o caminho das imagens
    teste(caminho_imagem)
