from PIL import Image
import tkinter
import pytesseract
import cv2
import os

class TesseractOCR():
    def __init__(self):
        pass

    def leituraImg(self, path_img):
        entrada = cv2.imread(path_img + ".JPEG")
        cv2.imshow("kk", entrada)
        cv2.waitKey(0)

        img = cv2.resize(entrada, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        cv2.imshow("ENTRADA", img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, img = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
        img2 = img
        cv2.imshow("Limiar", img)
        cv2.waitKey(0)

        img = cv2.GaussianBlur(img, (5, 5), 0)
        cv2.imwrite(path_img + "-ocr.JPEG", img)
        #imagem = Image.open(path_img + "-ocr.JPEG")
        #imagem = cv2.imread(path_img + ".JPEG")
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, img)
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        print(text)
        texto = self.removerChars(text)
        #janela = tkinter.Tk()
        #tkinter.Label(janela, text=texto, font=("Helvetica", 50)).pack()
        #janela.mainloop()

        cv2.destroyAllWindows()

    def removerChars(self, text):
        str = "!@#%¨&*()_+:;><^^}{`?|~¬\/=,.'ºª»‘"
        for x in str:
            text = text.replace(x, '')
        return text

path = "C:/roi1"
x = TesseractOCR()
x.leituraImg(path)
