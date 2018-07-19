import cv2
from Projeto.PreProcessamento import PreProcessamento
from Projeto.DetectarPlacasnaCena import DetectarPlacasnaCena
from Projeto.DetectarCaracteresNaPlaca import DetectaCaracteres
from Projeto.ReconhecimentoOCR import ReconhecerNumeros
from PIL import Image
imagem_original = cv2.imread("placa4.JPG")

altura, largura, canais = imagem_original.shape
metade = int(altura / 2)
imagem_original = imagem_original[int(altura / 2): altura, 0: largura]
cv2.imshow("copia", imagem_original)
cv2.waitKey(0)

possiveis_placas = DetectarPlacasnaCena()
tratar_imagem = PreProcessamento()
imagem_desfocada, imagem_binaria = tratar_imagem.pre_process(imagem_original)
cv2.imshow("kk", imagem_desfocada)
cv2.waitKey(0)

possiveis_placas = possiveis_placas.possiveisPlacasNaCena(imagem_desfocada, imagem_original)
placa_final = []
detectar = DetectaCaracteres()
for placa in possiveis_placas:
    imagem_desfocada2, imagemplaca = detectar.tratamento_da_placa(placa)
    quan_de_carac = detectar.detectaCaracteres(imagem_desfocada2, imagemplaca)
    if(len(quan_de_carac) > 7):
        placa_final = placa



desfocada, placaFi = detectar.tratamento_da_placa(placa_final)
cv2.imshow("PlacaFi", placaFi)
cv2.waitKey(0)
cv2.destroyAllWindows()

reconhecer = ReconhecerNumeros()


reconhecer.reconhecimentoOCR("C:/placa3")
