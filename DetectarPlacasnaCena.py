import cv2
import numpy as np
from Projeto.PreProcessamento import PreProcessamento

imagem_original = cv2.imread("placa5.jpeg")

class DetectarPlacasnaCena():
    LARGURA_PADRAO_DA_PLACA = 1.3
    ALTURA_PADRAO_DA_PLACA = 1.5

    def detectando_placas(self, imagem_original):
        lista_de_possiveis_placas = []
        altura, largura, canais = imagem_original.shape

        imagem_cinza = np.zeros((altura, largura, 1), np.uint8)
        imagem_binaria = np.zeros((altura, largura, 1), np.uint8)
        imagem_contornos = np.zeros((altura, largura, 3), np.uint8)
        #cv2.imshow("asd", imagem_cinza)

        cv2.destroyAllWindows()
        x = PreProcessamento()

        imagem_cinza, imagem_binaria = x.pre_process(imagem_original)
        cv2.imshow("1a", imagem_cinza)
        cv2.imshow("1b", imagem_binaria)
        cv2.waitKey(0)

    def encontrar_possiveis_carac(self, imagem_binaria):
        lista_possiveis_carac = []
        contar_possiveis_caracteres = 0

        imagem_binaria_copia = imagem_binaria.copy()
        imagem_contornos, contornos, npahierarchy = cv2.findContours(imagem_binaria_copia, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        altura, largura = imagem_binaria.shape
        imagem_contornos = np.zeros((altura, largura, 3), np.uint8)




x = DetectarPlacasnaCena()
x.detectando_placas(imagem_original)



