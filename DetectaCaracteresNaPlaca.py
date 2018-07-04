import cv2

class DetectaCaracteres:
    TAMANHO_DO_FILTRO_GAUSSIANO = (5, 5)
    LIMIAR = 70
    VALOR_MAXIMO = 255

    def tratamento_da_placa(self, imagem):
        imagem = cv2.resize(imagem, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        imagem_placa = imagem
        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        ret, imagem = cv2.threshold(cinza, self.LIMIAR, 255, cv2.THRESH_BINARY)
        imagem_desfocada = cv2.GaussianBlur(imagem, self.TAMANHO_DO_FILTRO_GAUSSIANO, 0)
        return imagem_desfocada, imagem_placa

    def detectaCaracteres(self, imagem_desfocada, imagem_placa_original):

        _, contornos, hier = cv2.findContours(imagem_desfocada, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        regioes_retangulares = []

        for c in contornos:
            perimetro = cv2.arcLength(c, True)
            if perimetro > 250:
                aprox = cv2.approxPolyDP(c, 0.02 * perimetro, True)
                (x, y, alt, lar) = cv2.boundingRect(c)
                cv2.rectangle(imagem_placa_original, (x, y), (x + alt, y + lar), (0, 0, 255), 2)
                possivel_placa = imagem_placa_original[y:y + lar, x:x + alt]
                regioes_retangulares.append(possivel_placa)

        for i in regioes_retangulares:
            cv2.imshow("foto", i)
            cv2.waitKey(0)

        cv2.imshow('Possiveis Caracteres', imagem_placa_original)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return regioes_retangulares

