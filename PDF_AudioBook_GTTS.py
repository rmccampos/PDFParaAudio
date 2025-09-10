from gtts import gTTS
import PyPDF2
import os

def pdf_para_audio():
    #Caminho do PDF
    pdf = 'C:/Users/RAFAEL-PC/Desktop/Python GUI/AudioBookProj/PDF_Audio/PDFParaAudio/PDF/O ladrão de raios - Ricky Riordan.pdf'
    pasta_saida = 'audiobook_capitulos_gtts'
    os.makedirs(pasta_saida, exist_ok=True)

    #Lê o PDF
    with open(pdf, "rb") as arq_pdf:
        leitor = PyPDF2.PdfReader(arq_pdf)
        texto = ""
        for pagina in leitor.pages:
            if pagina.extract_text():
                texto += pagina.extract_text() + "\n"

    #Converte para áudio em português do Brasil
    tts = gTTS(texto, lang="pt", slow=False)
    tts.save(os.path.join(pasta_saida, "audiobook.mp3"))

    print("✅ Audiobook com gTTS!")
