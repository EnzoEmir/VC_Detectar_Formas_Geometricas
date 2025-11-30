import cv2
import numpy as np

imagem = cv2.imread('assets/13_frame_000001_t1.50s.jpg')
#imagem = cv2.imread('assets/13_frame_000004_t6.00s.jpg')

bbox = cv2.selectROI("Selecione a Cor", imagem, showCrosshair=True)
cv2.destroyWindow("Selecione a Cor")

# Verificar se algo foi selecionado
if bbox[2] > 0 and bbox[3] > 0:
    x, y, w, h = bbox
    

    recorte = imagem[y:y+h, x:x+w]
    
    recorte_hsv = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
    
    min_hsv = np.min(recorte_hsv, axis=(0,1))
    max_hsv = np.max(recorte_hsv, axis=(0,1))
    

    print(f"Minimo: np.array([{min_hsv[0]}, {min_hsv[1]}, {min_hsv[2]}])")
    print(f"Maximo: np.array([{max_hsv[0]}, {max_hsv[1]}, {max_hsv[2]}])")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
