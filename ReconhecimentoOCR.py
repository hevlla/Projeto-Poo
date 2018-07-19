import cv2
import tkinter
import pytesseract
from PIL import Image

class ReconhecerNumeros():
    placa = ''

    def reconhecimentoOCR(self, path_img):
        entrada = cv2.imread(path_img + ".jpg")

        img = cv2.resize(entrada, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, img = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)

        img = cv2.GaussianBlur(img, (5, 5), 0)

        img.save("-ocr.jpg", img)
        img.show()
        print(img)

        imagem = Image.open(path_img + "-ocr.jpg", "r")

        saida = pytesseract.image_to_string(imagem, lang='eng')
        print(saida)
        texto = self.removerChars(saida)
        janela = tkinter.Tk()
        tkinter.Label(janela, text=texto, font=("Helvetica", 50)).pack()
        janela.mainloop()

        cv2.destroyAllWindows()

    def removerChars(self, text):
        str = "!@#%¨&*()_+:;><^^}{`?|~¬\/=,.'ºª»‘"
        for x in str:
            text = text.replace(x, '')
        return text