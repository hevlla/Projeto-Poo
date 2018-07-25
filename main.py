import argparse
from POO.Classes.PreProcessamento import PreProcessamento
from POO.Classes.DetectarPlacasnaCena import DetectarPlacasnaCena
from POO.Classes.DetectaCaracteresNaPlaca import DetectaCaracteres
import cv2

class Segmentacao:

    def __init__(self):
        pass

    def Segment(self, imagem_original):
        altura, largura, canais = imagem_original.shape
        imagem_original = imagem_original[int(altura / 2): altura, 0: largura]

        possiveis_placas = DetectarPlacasnaCena()
        tratar_imagem = PreProcessamento()
        imagem_desfocada, imagem_binaria = tratar_imagem.simple_pre_process(imagem_original)

        cv2.imwrite("/home/claudio/Documents/ProcessResult/ImagemDesfocada.jpg", imagem_desfocada)

        possiveis_placas = possiveis_placas.possiveisPlacasNaCena(imagem_desfocada, imagem_original)

        placa_final = []
        detectar = DetectaCaracteres()

        for placa in possiveis_placas:
            placa_desfocada, possivel_placa = detectar.tratamento_da_placa(placa)
            quan_de_carac = detectar.detectaCaracteres(placa_desfocada, possivel_placa)
            altura, largura, canais = placa.shape

            if(altura < largura and len(quan_de_carac) > 6):
                placa_final = placa

        placa_desfocada, possivel_placa = detectar.tratamento_da_placa(placa_final)
        detectar.detectaCaracteres(placa_desfocada, possivel_placa)

        desfocada, placaFi = detectar.tratamento_da_placa(placa_final)
        cv2.imwrite("/home/claudio/Documents/ProcessResult/PlacaFinal.png", placaFi)


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
args = vars(ap.parse_args())
imagem_original = cv2.imread(args["image"])


seg = Segmentacao()
seg.Segment(imagem_original)
