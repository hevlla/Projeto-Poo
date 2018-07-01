import cv2
import numpy as np
import math

imagem_original = cv2.imread("placa5.jpeg")

class PreProcessamento():

    GAUSSIAN_SMOOTH_FILTER_SIZE = (5, 5)
    ADAPTIVE_THRESH_BLOCK_SIZE = 19
    ADAPTIVE_THRESH_WEIGHT = 9

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

    def pre_process(self, imagem_original):

        """imagem_escala_cinza = self.extrair_valor(imagem_original)
        imagem_contraste_max_cinza = self.melhorar_contraste(imagem_escala_cinza)
        altura, largura = imagem_escala_cinza.shape
        imagem_Blurred = np.zeros((altura, largura, 1), np.uint8)
        imagem_Blurred = cv2.GaussianBlur(imagem_contraste_max_cinza, self.GAUSSIAN_SMOOTH_FILTER_SIZE, 0)
        #imagem_binaria = cv2.adaptiveThreshold(imagem_Blurred, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, self.ADAPTIVE_THRESH_BLOCK_SIZE, self.ADAPTIVE_THRESH_WEIGHT)"""

        cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)
        _, imagem_binaria = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
        imagem_desfocada = cv2.GaussianBlur(imagem_binaria, self.GAUSSIAN_SMOOTH_FILTER_SIZE, 0)
        return imagem_desfocada

