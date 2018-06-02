import cv2
import imutils
import argparse
import numpy as np


class Detector_de_Formas:
    def __init__(self):
        pass

    def detect(self, contorno):
        shape = "Indefinido"
        peri = cv2.arcLength(contorno, True)
        aprox = cv2.approxPolyDP(contorno, 0.04 * peri, True)
        print(aprox)
        print(peri)

        if(len(aprox) == 3):
            shape = "Triangulo"

        elif (len(aprox) == 4):
            (x, y, w, h) = cv2.boundingRect(aprox)
            area = w / float(h)
            shape = "Quadrado" if area >= 0.95 and area <= 1.05 else "Retangulo"

        elif(len(aprox) == 5):
            shape = "Pentagono"

        else:
            shape = "Circulo"


        return shape


"""Nas próximas três linhas, diz respeito a como será a entrada do nosso programa,
pois será rodado no terminal para poder testar várias imagens na mesma execução do programa,
então os parametros serão passados na seguinte ordem: python3 DetectordeFormas.py --image nome_da_imagem.formato_da_imagem(png, jpg, JPG, jpeg)"""

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
args = vars(ap.parse_args())

"""Nas próximas três linhas, será lida a imagem atraves da função 'cv2.imread',
na próxima linha a imagem será redimensionada atraves da função 'imutils.resize'"""

image = cv2.imread(args["image"])
redimensiona = imutils.resize(image, width=300)
ratio = image.shape[0]/float(redimensiona.shape[0])

"""Transforma a imagem em escala de cinza"""
img_cinza = cv2.cvtColor(redimensiona, cv2.COLOR_BGR2GRAY)
"""Faz um balanceamento das cores atraves da função 'cv2.equalizehist', esse balanceamento melhora o contraste,
isto permite melhor definição dos objetos presentes na imagem"""
hist_img_equa = cv2.equalizeHist(img_cinza)

"""na proxima linha, usamos a função 'np.stack' pra juntar a imagem antes de aplicar a equalização e a imagem 
depois de aplicar a equalização, e nas linhas seguintes essa será mostrado as duas juntas"""
res = np.hstack((img_cinza, hist_img_equa))
cv2.imwrite('res.png', res)
cv2.imshow("sdsd", res)
cv2.waitKey(0)

""" Nas proximas três linhas a imagem equalizada será passado no filtro gaussiano atravas da função 'cv2.GaussianBlur'
 e mostrada logo em seguida"""
blurred = cv2.GaussianBlur(hist_img_equa, (5, 5), 0)
cv2.imshow("kkk", blurred)
cv2.waitKey(0)
"""A imagem apos aplicado o filtro gaussiano, vai ser binarizada"""
binarizar = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("gfh", binarizar)
cv2.waitKey(0)


cnts = cv2.findContours(binarizar.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if imutils.is_cv2() else cnts[1]

sd = Detector_de_Formas()

for c in cnts:

    """ Nesse laco, são mostradas todos os formatos encontrados na imagem, não é o foco do nosso programa"""
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = sd.detect(c)

    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)

    cv2.imshow("Image", image)
    cv2.waitKey(0)