import cv2
import numpy as np


class PreProcessamento:

    TAMANHO_DO_FILTRO_GAUSSIANO = (5, 5)
    LIMIAR = 90
    VALOR_MAXIMO = 255
    img_desfocada = []
    img_binaria = []
    img_escala_cinza = []

    def __init__(self):
        pass

    def extrair_valor(self, imagem_original):
        altura = imagem_original.shape[0]
        largura = imagem_original.shape[1]
        canais = imagem_original.shape[2]
        imagemHSV = np.zeros((altura, largura, 3), np.uint8)
        imagemHSV = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2HSV)
        imgMatiz, imgSaturacao, imgValor = cv2.split(imagemHSV)
        print(imgValor)
        return imgValor

    def melhorar_contraste(self, imagem_escala_cinza):
        altura, largura = imagem_escala_cinza.shape
        imgTopHat = np.zeros((altura, largura, 1), np.uint8)
        imgBlackHat = np.zeros((altura, largura, 1), np.uint8)
        estruturandoElemento = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        imgTopHat = cv2.morphologyEx(imagem_escala_cinza, cv2.MORPH_TOPHAT, estruturandoElemento)
        imgBlackHat = cv2.morphologyEx(imagem_escala_cinza, cv2.MORPH_BLACKHAT, estruturandoElemento)
        imagem_escala_cinza_top_hat = cv2.add(imagem_escala_cinza, imgTopHat)
        imagem_escala_cinza_top_hat_minus_black_hat = cv2.subtract(imagem_escala_cinza_top_hat, imgBlackHat)

        return imagem_escala_cinza_top_hat_minus_black_hat

    def simple_pre_process(self, imagem_original):
        cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)
        _, imagem_binaria = cv2.threshold(cinza, self.LIMIAR, self.VALOR_MAXIMO, cv2.THRESH_BINARY)
        imagem_desfocada = cv2.GaussianBlur(imagem_binaria, self.TAMANHO_DO_FILTRO_GAUSSIANO, 0)
        self.img_desfocada = imagem_desfocada
        self.img_binaria = imagem_binaria
        self.img_escala_cinza = cinza

        cv2.imwrite("/home/claudio/Documents/ProcessResult/EscalaDeCinza.jpg", cinza)
        return imagem_desfocada, imagem_binaria

