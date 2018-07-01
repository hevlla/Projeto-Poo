import cv2
import numpy as np
from matplotlib import pyplot as plt
from Projeto.PreProcessamento import PreProcessamento


imagem_original = cv2.imread("placa5.jpeg")

class DetectarPlacasnaCena():
    LARGURA_PADRAO_DA_PLACA = 1.3
    ALTURA_PADRAO_DA_PLACA = 1.5

    def possiveisPlacasNaCena(self, imagem_desfocada):
        """ Neste metodo, é recebida a imagem desfocada, após ser aplicado o filtro gaussiano, e
            através do método 'cv2.findCountorns' buscamos todos os contornos, retornando um Array
            com todos os contornos presentes na imagem. Em seguida percorremos este array, de forma
            a selecionar aquele que são fechados, fazemos isso atraves do metodo 'cv2.arcLenght',
            logo em seguida transformamos o contorno para algo parecido com aquilo que procuramos,
            atraves do metodo 'cv2.approxPoly', logo verificamos se a forma é um quadrado ou um retangulo
            se for, será pego as coordenadas desse contorno atraves do metodo 'cv2.boundingRect', e apos
            será desenhado a forma da regiao encontrada e salva como uma nova imagem.
            """
        _, contornos, hier = cv2.findContours(imagem_desfocada, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        regioes_retangulares = []

        for c in contornos:
            perimetro = cv2.arcLength(c, True)
            if perimetro > 120:
                aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)
                if len(aprox) == 4:
                    (x, y, alt, lar) = cv2.boundingRect(c)
                    cv2.rectangle(imagem_original, (x, y), (x+alt, y+lar), (0, 255, 0), 2)
                    possivel_placa = imagem_original[y:y + lar, x:x + alt]
                    regioes_retangulares.append(possivel_placa)

        cv2.imshow('draw', imagem_original)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return regioes_retangulares

