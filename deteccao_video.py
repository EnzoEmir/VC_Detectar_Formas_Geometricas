import cv2
import numpy as np
from config import *

video = cv2.VideoCapture(VIDEO_PATH)

def detectar_formas(imagem):
    # Aplica blur para reduzir ruído
    imagem_blur = cv2.medianBlur(imagem, MEDIAN_BLUR_KERNEL)
    
    hsv = cv2.cvtColor(imagem_blur, cv2.COLOR_BGR2HSV)
    imagem_resultado = imagem.copy()
    
    for nome_cor, valor_min, valor_max in LISTA_CORES:
        minimo = np.array(valor_min)
        maximo = np.array(valor_max)

        mascara = cv2.inRange(hsv, minimo, maximo)

        kernel = np.ones(MORPHOLOGY_KERNEL_SIZE, np.uint8)
        # Melhor que o Erode e Dilate pq "limpa" dentro da figura
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
        
        mascara = cv2.medianBlur(mascara, MEDIAN_BLUR_KERNEL)

        # Encontra contornos
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contornos:
            area = cv2.contourArea(cnt)
            if area > AREA_MINIMA:
                perimetro = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, APPROX_POLY_FACTOR * perimetro, True)
                num_vertices = len(approx)
                circularidade = 4 * np.pi * area / (perimetro * perimetro)
                
                forma = "Desconhecido"
                
                # Classificação das formas baseada em vértices e circularidade
                if "Circulo" in nome_cor and VERTICES_CIRCULO[0] <= num_vertices <= VERTICES_CIRCULO[1] and circularidade > CIRCULARIDADE_MINIMA_CIRCULO:
                    forma = "Circulo"
                elif "Cruz" in nome_cor and VERTICES_CRUZ[0] <= num_vertices <= VERTICES_CRUZ[1]:
                    forma = "Cruz"
                elif "Estrela" in nome_cor and VERTICES_ESTRELA[0] <= num_vertices <= VERTICES_ESTRELA[1]:
                    forma = "Estrela"
                elif "Triangulo" in nome_cor and VERTICES_TRIANGULO[0] <= num_vertices <= VERTICES_TRIANGULO[1]:
                    forma = "Triangulo"
                elif "Quadrado" in nome_cor and VERTICES_QUADRADO[0] <= num_vertices <= VERTICES_QUADRADO[1]:
                    forma = "Quadrado"
                elif "Pentagono" in nome_cor and VERTICES_PENTAGONO[0] <= num_vertices <= VERTICES_PENTAGONO[1]:
                    forma = "Pentagono"
                elif "Hexagono" in nome_cor and VERTICES_HEXAGONO[0] <= num_vertices <= VERTICES_HEXAGONO[1]:
                    forma = "Hexagono"
                elif "Castelo" in nome_cor and VERTICES_CASTELO[0] <= num_vertices <= VERTICES_CASTELO[1]:
                    forma = "Castelo"
                # Fallback para detecção por cor
                elif "Circulo" in nome_cor:
                    forma = "Circulo"
                elif "Triangulo" in nome_cor:
                    forma = "Triangulo"
                elif "Quadrado" in nome_cor:
                    forma = "Quadrado"
                elif "Pentagono" in nome_cor:
                    forma = "Pentagono"
                elif "Hexagono" in nome_cor:
                    forma = "Hexagono"
                elif "Cruz" in nome_cor:
                    forma = "Cruz"
                elif "Estrela" in nome_cor:
                    forma = "Estrela"
                elif "Castelo" in nome_cor:
                    forma = "Castelo"
                else:
                    forma = f"Forma ({num_vertices} vertices)"

                # Encontra o centro
                M = cv2.moments(cnt)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    cX, cY = 0, 0
                
                # Desenha o contorno e o texto
                cv2.drawContours(imagem_resultado, [cnt], -1, COR_CONTORNO, ESPESSURA_CONTORNO)
                texto_final = f"{forma}"
                cv2.putText(imagem_resultado, texto_final, (cX + OFFSET_TEXTO_X, cY + OFFSET_TEXTO_Y), 
                           cv2.FONT_HERSHEY_SIMPLEX, TAMANHO_FONTE, COR_TEXTO, ESPESSURA_TEXTO)
    
    return imagem_resultado


while True:
    ret, frame = video.read() 
    
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    frame_processado = detectar_formas(frame)
    
    cv2.imshow('Deteccao de Formas Geometricas - Video', frame_processado)
    
    if cv2.waitKey(FRAME_DELAY) & 0xFF == ord(TECLA_SAIR):
        break

video.release()
cv2.destroyAllWindows()