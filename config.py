# Parâmetros do vídeo

VIDEO_PATH = 'assets/video_desafio_1.mp4'

# Velocidade de reprodução
FRAME_DELAY = 30

TECLA_SAIR = 'q'

# ----------------------------------------------------------------------

# Parâmetros de Pré-processamento

# Tamanho do kernel para filtro medianBlur (redução de ruído, maior mais suave)
MEDIAN_BLUR_KERNEL = 5

# Tamanho do kernel para operações morfológicas 
MORPHOLOGY_KERNEL_SIZE = (5, 5)

# ----------------------------------------------------------------------

# Limites do HSV para segmentação por cor

# Estrutura: ("Nome", [min H,S,V], [max H,S,V])
LISTA_CORES = [
    ("Circulo Azul", [100, 90, 180], [140, 180, 230]),
    ("Quadrado Marrom", [115, 25, 85], [145, 90, 150]), 
    ("Pentagono Roxo", [158, 92, 150], [179, 255, 225]),
    ("Cruz Rosa", [140, 70, 160], [158, 180, 255]),
    ("Triangulo Azul", [100, 30, 130], [120, 110, 190]),
    ("Castelo Laranja", [165, 30, 130], [179, 200, 255]),
    ("Estrela Verde", [45, 25, 150], [90, 90, 215]),
    ("Hexagono Vermelho", [0, 120, 160], [10, 255, 255])
]

# ----------------------------------------------------------------------

# Parâmetros de detecção de contornos

# Valores menores detectam objetos pequenos (estrela em alguns casos), mas podem capturar ruído
AREA_MINIMA = 800

# Maior valor = menos precisão
APPROX_POLY_FACTOR = 0.015

# ----------------------------------------------------------------------

# Parâmetros de classificação de formas

# Estrutura: (min_vertices, max_vertices)
VERTICES_CIRCULO = (5, 10)
VERTICES_CRUZ = (10, 14)
VERTICES_ESTRELA = (9, 13)
VERTICES_TRIANGULO = (3, 3)
VERTICES_QUADRADO = (4, 4)
VERTICES_PENTAGONO = (5, 5)
VERTICES_HEXAGONO = (5, 7)
VERTICES_CASTELO = (8, 12)

# Mais perto de 1 = mais circular
CIRCULARIDADE_MINIMA_CIRCULO = 0.4

# ----------------------------------------------------------------------

# PARÂMETROS DE VISUALIZAÇÃO

COR_CONTORNO = (0, 255, 0)  

ESPESSURA_CONTORNO = 2

COR_TEXTO = (255, 255, 255)  

TAMANHO_FONTE = 0.5

ESPESSURA_TEXTO = 2

OFFSET_TEXTO_X = -20
OFFSET_TEXTO_Y = 0