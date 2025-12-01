import cv2
import numpy as np

video = 'assets/video_desafio_1.mp4'
video = cv2.VideoCapture(video)

# Estrutura: ("Nome", [min H,S,V], [max H,S,V])
lista_cores = [
    ("Circulo Azul", [100, 90, 180], [140, 180, 230]),
    # ("Pentagono Roxo", [124, 162, 42], [161, 255, 144]),
    # ("Cruz Rosa", [124, 212, 151], [155, 255, 212]),
    # ("Triangulo Azul", [107, 222, 113], [130, 255, 213]),
    # ("Castelo Laranja", [150, 0, 130], [179, 194, 255]),
    # ("Estrela Verde", [66, 220, 0], [104, 255, 215]),
    # ("Quadrado Azul", [101, 212, 56], [122, 255, 111]),
    # ("Hexagono Rosa", [147, 180, 104], [179, 255, 199])
]

def detectar_formas(imagem):
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    imagem_resultado = imagem.copy()
    
    for nome_cor, valor_min, valor_max in lista_cores:
        minimo = np.array(valor_min)
        maximo = np.array(valor_max)

        mascara = cv2.inRange(hsv, minimo, maximo)

        kernel = np.ones((5,5), np.uint8)
        mascara = cv2.erode(mascara, kernel, iterations=1)
        mascara = cv2.dilate(mascara, kernel, iterations=1)

        # Encontra contornos
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contornos:
            area = cv2.contourArea(cnt)
            if area > 1000:  # Área maior que 1000 pixels
                perimetro = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.015 * perimetro, True)
                num_vertices = len(approx)
                circularidade = 4 * np.pi * area / (perimetro * perimetro)
                
                forma = "Desconhecido"
                
                # Classificação das formas
                if "Circulo" in nome_cor and num_vertices == 6 and circularidade > 0.4:
                    forma = "Circulo"
                elif "Cruz" in nome_cor and num_vertices == 12 and circularidade < 0.25:
                    forma = "Cruz"
                elif "Estrela" in nome_cor and num_vertices == 11 and circularidade < 0.4:
                    forma = "Estrela"
                elif "Triangulo" in nome_cor and num_vertices == 3:
                    forma = "Triangulo"
                elif "Quadrado" in nome_cor and num_vertices == 4:
                    forma = "Quadrado"
                elif "Pentagono" in nome_cor and num_vertices == 5:
                    forma = "Pentagono"
                elif "Hexagono" in nome_cor and num_vertices == 6 and circularidade > 0.8:
                    forma = "Hexagono"
                elif "Castelo" in nome_cor and num_vertices == 10:
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
                cv2.drawContours(imagem_resultado, [cnt], -1, (0, 255, 0), 2)
                texto_final = f"{forma}"
                cv2.putText(imagem_resultado, texto_final, (cX - 20, cY), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    return imagem_resultado


while True:
    ret, frame = video.read() 

    frame_processado = detectar_formas(frame)
    
    cv2.imshow('Deteccao de Formas Geometricas - Video', frame_processado)
    
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("Programa encerrado.")