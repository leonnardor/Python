#Script que move o mouse em uma trajetória circular para ajudar a entender conceitos de pyaytogui para automação de processos como o de captura de tela, testes de software, etc.

import pyautogui
import time
import math


# Define o número de vezes que o mouse será movido
num_movements = 10000

# Define a velocidade do movimento do mouse (em segundos)
speed = 1

# Obtém a posição atual do mouse
current_x, current_y = pyautogui.position()

# Define o raio da trajetória circular
radius = 200

# Define o ângulo inicial
angle = 0

while num_movements > 0:
    # Calcula a nova posição x e y do mouse baseado no raio e no ângulo
    new_x = current_x + radius * math.cos(angle)
    new_y = current_y + radius * math.sin(angle)

    # Mova o mouse para a nova posição
    pyautogui.moveTo(new_x, new_y)

    # Atualiza o ângulo para o próximo movimento
    angle += 0.1

    # Decrementa o número de movimentos restantes
    num_movements -= 1

    # Pausa por um período de tempo antes do próximo movimento
    time.sleep(speed)