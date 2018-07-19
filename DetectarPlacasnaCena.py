import cv2

class DetectarPlacasnaCena():
    LARGURA_PADRAO_DA_PLACA = 1.3
    ALTURA_PADRAO_DA_PLACA = 1.5

    TAMANHO_DO_PERIMETRO = 120
    COR_DO_TRACO = (0, 255, 0)

    def possiveisPlacasNaCena(self, imagem_desfocada, imagem_original):
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
        imagem_copia = imagem_original

        for contorno in contornos:
            perimetro = cv2.arcLength(contorno, True)
            if perimetro > self.TAMANHO_DO_PERIMETRO:
                aprox = cv2.approxPolyDP(contorno, 0.03 * perimetro, True)

                if len(aprox) == 4:
                    (x, y, alt, lar) = cv2.boundingRect(contorno)
                    cv2.rectangle(imagem_copia, (x, y), (x+alt, y+lar), self.COR_DO_TRACO, 2)
                    possivel_placa = imagem_copia[y:y + lar, x:x + alt]
                    regioes_retangulares.append(possivel_placa)

        cv2.imshow('Possiveis Placas', imagem_copia)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return regioes_retangulares

