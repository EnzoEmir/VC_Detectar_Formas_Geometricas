import cv2
import numpy as np

imagem = cv2.imread('assets/13_frame_000001_t1.50s.jpg')

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Estrutura: ("Nome", [min H,S,V], [max H,S,V])
lista_cores = [
    ("Circulo Azul", [112, 229, 212], [150, 255, 255]),
    ("Pentagono Roxo", [124, 162, 42], [161, 255, 144]),
    ("Cruz Rosa", [124, 212, 151], [155, 255, 212]),
    ("Triangulo Azul", [107, 222, 113], [130, 255, 213]),
    ("Castelo Laranja", [166, 90, 124], [179, 255, 255]),
    ("Estrela Verde", [66, 220, 0], [104, 255, 215]),
    ("Quadrado Azul", [101, 212, 56], [122, 255, 111])


]

for nome_cor, valor_min, valor_max in lista_cores:

    minimo = np.array(valor_min)
    maximo = np.array(valor_max)

    mascara = cv2.inRange(hsv, minimo, maximo)

    # Limpeza Morfologia
    # Cria um "pincel" 5x5 pixels
    kernel = np.ones((5,5), np.uint8)

    # Erode: suaviza as bordas 
    mascara = cv2.erode(mascara, kernel, iterations=1)
    # Dilate: "Incha" a forma para tapar buracos dentro dela
    mascara = cv2.dilate(mascara, kernel, iterations=1)

    # RETR_EXTERNAL: Pega apenas o contorno de fora 
    # CHAIN_APPROX_SIMPLE: guarda apenas os pontos essenciais da linha
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 3)

    if len(contornos) > 0:
            print(f"Processando {nome_cor}: Encontrei {len(contornos)} contornos.")

cv2.imshow('Contorno Detectado', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()