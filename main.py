import getpass
import PDF_AudioBook
import PDF_AudioBook_GTTS
import os

def print_hi(nome):
    print(f'Olá, {nome}!\n')

def limpar_terminal():
    #Limpa o terminal usando cls ou clear dependendo do SO
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    nome = getpass.getuser()
    print_hi(nome)
    tipo = input('Digite 1 para usar |pyttsx3| ou 2 para usar |GTTS|: ')

    # Caminho PDF que vai virar áudio
    pdf = 'PDF/O ladrão de raios - Ricky Riordan.pdf'

    #Definição e/ou criação da Pasta de saída
    pasta_saida = 'C:/Users/RAFAEL-PC/Desktop/Audio Books/PercyLivro01'
    os.makedirs(pasta_saida, exist_ok=True)

    #Verificação das opções de execução
    while not(tipo == '1' or tipo == '2'):
        print('Por favor, digite uma das opções diponíveis.')
        tipo = input('Digite 1 para usar |pyttsx3| ou 2 para usar |GTTS|: ')

    #Execução dos scripts
    limpar_terminal()
    print('-'*50)
    try:
        if tipo == '1':
            PDF_AudioBook.pdf_para_audio(pdf,pasta_saida)
        elif tipo == '2':
            PDF_AudioBook_GTTS.pdf_para_audio(pdf,pasta_saida)
        else:
            print('Tipo não encontrado ou não disponível.')
    except ValueError as e:
        print(f'Erro: {e}')