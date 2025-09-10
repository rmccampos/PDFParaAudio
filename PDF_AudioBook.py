import pyttsx3
import PyPDF2
import os

def pdf_para_audio():
    #Caminho do PDF
    pdf = 'C:/Users/RAFAEL-PC/Desktop/Python GUI/AudioBookProj/PDF_Audio/PDFParaAudio/PDF/O ladrão de raios - Ricky Riordan.pdf'

    #Pasta de saída
    pasta_saida = 'Audio Books'
    os.makedirs(pasta_saida, exist_ok=True)

    #Abre o PDF
    with open(pdf,'rb') as arq_pdf:
        leitor = PyPDF2.PdfReader(arq_pdf)

        #Inicia o narrador
        engine = pyttsx3.init()
        voz = engine.getProperty('voices')
        engine.setProperty('voice', voz[1].id)
        engine.setProperty('rate', 160)

        #Lê página por página
        for i, pagina in enumerate(leitor.pages, start=1):
            texto = pagina.extract_text()

            if texto:
                nome_arq = os.path.join(pasta_saida,f'pagina_{i}.mp3')
                engine.save_to_file(texto, nome_arq)
                engine.runAndWait()
                print(f'✅ Página {i} salva como {nome_arq}')

    print(f'\n 🎧 Audiobook completo gerado na pasta: {pasta_saida}')