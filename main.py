import getpass
import PDF_AudioBook
import PDF_AudioBook_GTTS


def print_hi(nome):
    print(f'Olá, {nome}')

nome = getpass.getuser()

if __name__ == '__main__':
    print_hi(nome)
    PDF_AudioBook_GTTS.pdf_para_audio()