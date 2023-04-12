# Microondas
# Considerar: apenas um botão giratório (o qual pode ser puxado e pressionado) e que
# controla toda a funcionalidade do microondas (tempo de cozimento, start/stop, etc)
# Possui timer/relógio integrado e também possui possibilidade de ajustar a potência
# Tempo de cozimento será acionado ao girar o botão giratório, start/stop serão
# acionados ao pressionar/puxar o botão
# Timer será acionado assim que o cozimento iniciar, o relógio irá aparecer após um
# tempo de inatividade de 5 minutos
# Para alterar a potência, será empurra o botão giratório para cima e então selecionar a potência desejada

import time
import threading
import pygame
import os
import keyboard
import msvcrt
import datetime

# função que reproduz o "beep"
def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()

def microondas(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()

def clean():
    os.system('cls')

# objeto "microondas"
class microondas:
    # Método construtor
    def __init__(self, tempoCozimento):
        #self.startStop = True #startStop
        self.tempoCozimento = tempoCozimento

    # Temporizador que irá fazer a contagem regressiva e iniciar o funcionamento do microondas
    def temporizador(self):
        if True:
            tempo = self.tempoCozimento
            play_sound('C:\\Users\\guiga\\Desktop\\Pasta\\Beep.mp3')
            for i in range(tempo, -1, -1):
                mins, secs = divmod(i, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                clean()
                pass
                # para a operação caso a tecla "enter" seja pressionada
                if msvcrt.kbhit() and msvcrt.getch() == b"\r":
                    cozimento = False
                    break
                while tempo > 0:
                    cozimento = True

                    break
            mins, secs = divmod(i, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)

            # Após o contador chegar a zero, dispara o alarme e printa a mensagem na tela
            cozimento = False
            for ii in range(6, 0, -1):
                clean()
                if ii % 2 == 0:
                    # limpa a tela e coloca a mensagem indicando que o cozimento acabou
                    print('--:--')  # lembrar da limitação de 10 caracteres, será necessário fazer a mensagem rolar na tela
                    play_sound('C:\\Users\\guiga\\Desktop\\Pasta\\Beep.mp3')
                elif ii % 2 != 0:
                    clean()
                time.sleep(1)

def tempoSelecionado():
    # Define os valores mínimo e máximo
    min_value = 0
    max_value = 20

    # Define o valor inicial
    value = 0

    # Loop principal
    while True:
        # Exibe o valor atual
        minutos, segundos = divmod(value, 60)
        print(f"{minutos:02d}:{segundos:02d}", end="\r")

        # Espera por uma tecla
        key = msvcrt.getch()

        # Processa a tecla
        if key == b"\xe0":
            key = msvcrt.getch()
            if key == b"K":
                # Diminui o valor em 1 minuto
                value = max(value - 60, min_value)
            elif key == b"M":
                # Aumenta o valor em 1 minuto
                value = max(value + 60, min_value)
        elif key == b"\r":
            # Seleciona o valor atual
            break

    # Limpa a tela após a seleção
    clean()
    # Retorna o valor para a função, que será passado para o objeto
    return int(value)

def potencia():
    # Define os valores mínimo e máximo
    min_value = 00
    max_value = 10

    # Define o valor inicial
    value = 0

    # Loop principal
    while True:
        # Exibe o valor atual
        print(f"PO{value:01d}", end="\r")

        # Espera por uma tecla
        key = msvcrt.getch()

        # Processa a tecla
        if key == b"\xe0":
            key = msvcrt.getch()
            if key == b"K":
                # Diminui o valor
                value = max(value - 1, min_value)
                clean()
            elif key == b"M":
                # Aumenta o valor
                value = min(value + 1, max_value)
                clean()
        elif key == b"\r":
            # Seleciona o valor atual
            clean()
            break

    # Exibe uma mensagem de confirmação
    print(f"PO{value}")
    time.sleep(3)
    clean()

def clock():
    # printa a hora do sistema na tela
    while True:
        if keyboard.is_pressed('left') or keyboard.is_pressed('right') or keyboard.is_pressed('up') or keyboard.is_pressed('down'):
            break
        else:
            hora = datetime.datetime.now()
            clean()
            print(hora.strftime("%H:%M"), end='\r')
            time.sleep(0.5)
        #return hora

def main():
    while True:
        clock()
        if keyboard.is_pressed('up') or keyboard.is_pressed('down'):
            clean()
            potencia()
            pass
        print('--:--')
        clean()
        time.sleep(0.3)
        start = microondas(tempoSelecionado()).temporizador()
        pass

if __name__ == "__main__":
    main()



