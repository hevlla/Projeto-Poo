import cv2
import shutil
import os

class DetectaCaracteres:
    TAMANHO_DO_FILTRO_GAUSSIANO = (5, 5)
    LIMIAR = 70
    VALOR_MAXIMO = 255
    CORTE = 8

    def __init__(self):
        pass

    def tratamento_da_placa(self, imagem):
        imagem = cv2.resize(imagem, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        imagem_placa = imagem
        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("/home/claudio/Documents/ProcessResult/Placa_Cinza.jpg", cinza)

        ret, imagem = cv2.threshold(cinza, self.LIMIAR, 255, cv2.THRESH_BINARY)
        cv2.imwrite("/home/claudio/Documents/ProcessResult/PlacaPosPro.jpg", imagem)
        imagem_desfocada = cv2.GaussianBlur(imagem, self.TAMANHO_DO_FILTRO_GAUSSIANO, 0)

        return imagem_desfocada, imagem_placa

    def detectaCaracteres(self, imagem_desfocada, imagem_placa_original):

        _, contornos, hier = cv2.findContours(imagem_desfocada, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        lista_de_possiveis_caracteres = []
        cont = 0
        shutil.rmtree("/home/claudio/Documents/ProcessResult/CaracteresDaPlaca/")
        caminho = R'/home/claudio/Documents/ProcessResult/CaracteresDaPlaca'
        os.mkdir(caminho)

        for c in contornos:
            perimetro = cv2.arcLength(c, True)

            if perimetro > 150:
                (x, y, alt, lar) = cv2.boundingRect(c)
                possivel_caracter = imagem_placa_original[y - self.CORTE: y + lar + self.CORTE,
                                    x - self.CORTE: x + alt + self.CORTE]
                altura, largura, canal = possivel_caracter.shape
                cinza = cv2.cvtColor(possivel_caracter, cv2.COLOR_BGR2GRAY)
                ret, imagem = cv2.threshold(cinza, self.LIMIAR, 255, cv2.THRESH_BINARY)
                copia = imagem_placa_original.copy()
                cv2.rectangle(copia, (x - 8, y - 8), (8 + x + alt, 8 + y + lar), (0, 0, 255), 2)
                if(altura >= largura):
                    cv2.imwrite("/home/claudio/Documents/ProcessResult/CaracteresDaPlaca/Caracter" + str(cont) + ".jpg", imagem)
                    lista_de_possiveis_caracteres.append(possivel_caracter)
                    cv2.rectangle(imagem_placa_original, (x - 8, y - 8), (8 + x + alt, 8 + y + lar), (0, 0, 255), 2)
                    cont += 1

        cv2.imshow('Possiveis Caracteres', imagem_placa_original)
        cv2.imwrite("/home/claudio/Documents/ProcessResult/Caracteres.jpg", imagem_placa_original)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return lista_de_possiveis_caracteres


