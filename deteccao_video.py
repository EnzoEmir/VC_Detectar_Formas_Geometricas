import cv2
import numpy as np

video = 'assets/video_desafio_1.mp4'
video = cv2.VideoCapture(video)

# Estrutura: ("Nome", [min H,S,V], [max H,S,V])
lista_cores = [
    ("Circulo Azul", [100, 90, 180], [140, 180, 230]),
    ("Quadrado Marrom", [115, 25, 85], [145, 90, 150]), 
    ("Pentagono Roxo", [158, 92, 150], [179, 255, 225]),
    ("Cruz Rosa", [140, 70, 160], [158, 180, 255]),
    ("Triangulo Azul", [100, 30, 130], [120, 110, 190]),
    ("Castelo Laranja", [165, 30, 130], [179, 200, 255]), # Esta instavel, mas nâo consegui melhorar
    ("Estrela Verde", [45, 25, 150], [90, 90, 215]),
   ("Hexagono Vermelho", [0, 120, 160], [10, 255, 255]) # Como não tem no vídeo, somente uma estimativa
]

def detectar_formas(imagem):
    # Aplica blur para reduzir ruído(se estiver pesado pode trocar pro GaussianBlur)
    imagem_blur = cv2.medianBlur(imagem, 5)
    
    hsv = cv2.cvtColor(imagem_blur, cv2.COLOR_BGR2HSV)
    imagem_resultado = imagem.copy()
    
    for nome_cor, valor_min, valor_max in lista_cores:
        minimo = np.array(valor_min)
        maximo = np.array(valor_max)

        mascara = cv2.inRange(hsv, minimo, maximo)

        kernel = np.ones((5, 5), np.uint8)
        # Melhor que o Erode e Dilate pq "limpa" dentro da figura
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
        
        mascara = cv2.medianBlur(mascara, 5)

        # Encontra contornos
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contornos:
            area = cv2.contourArea(cnt)
            if area > 800:  # Diminui a área pra conseguir pegar a Estrela em alguns casos(Caso diminuir mais pode acabar pegando ruido)
                perimetro = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.015 * perimetro, True)
                num_vertices = len(approx)
                circularidade = 4 * np.pi * area / (perimetro * perimetro)
                
                forma = "Desconhecido"
                
                # Classificação das formas
                if "Circulo" in nome_cor and 5 <= num_vertices <= 10 and circularidade > 0.4:
                    forma = "Circulo"
                elif "Cruz" in nome_cor and 10 <= num_vertices <= 14 :
                    forma = "Cruz"
                elif "Estrela" in nome_cor and 9 <= num_vertices <= 13:
                    forma = "Estrela"
                elif "Triangulo" in nome_cor and num_vertices == 3:
                    forma = "Triangulo"
                elif "Quadrado" in nome_cor and num_vertices == 4:
                    forma = "Quadrado"
                elif "Pentagono" in nome_cor and num_vertices == 5:
                    forma = "Pentagono"
                elif "Hexagono" in nome_cor and 5 <= num_vertices <= 7:
                    forma = "Hexagono"
                elif "Castelo" in nome_cor and 8 <= num_vertices <= 12:
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
    
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    frame_processado = detectar_formas(frame)
    
    cv2.imshow('Deteccao de Formas Geometricas - Video', frame_processado)
    
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()