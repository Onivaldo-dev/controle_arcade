import serial
import time
import pyautogui

# Abra a porta serial com a mesma taxa de baud definida no Arduino (9600)
arduino = serial.Serial('COM6', 9600)  # Troque 'COM6' pela porta correta
time.sleep(2)  # Aguarde a conexão ser estabelecida

# Estados anteriores para detectar mudança
estado_anterior_botoes = ['1', '1']  # Supondo que '1' é não pressionado

# Mapeamento: botão físico → tecla
mapa_botoes_teclas = {
    0: 'a',  # botão 4 → tecla 'a'
    1: 'b'   # botão 5 → tecla 'b'
}

def ler_botoes():
    """Função para ler os estados dos botões do Arduino"""
    arduino.write(b'R')  # Envia comando para ler
    data = arduino.readline().decode('utf-8').strip()
    return data.split(',')

def acionar_led(led_id, acionar=True):
    """Função para acionar ou desligar um LED no Arduino"""
    if acionar:
        arduino.write(f'S{led_id}1'.encode())
    else:
        arduino.write(f'S{led_id}0'.encode())

def main():
    global estado_anterior_botoes

    try:
        while True:
            botoes_estado = ler_botoes()

            print(f"Estados dos botões: {botoes_estado}")

            for i in range(len(botoes_estado)):
                # Se botão foi pressionado agora e estava solto antes
                if botoes_estado[i] == '0' and estado_anterior_botoes[i] == '1':
                    tecla = mapa_botoes_teclas.get(i)
                    if tecla:
                        pyautogui.press(tecla)  # Simula a tecla
                        print(f"Tecla '{tecla}' pressionada por botão {i + 4}")
                    acionar_led(i + 7, True)

                elif botoes_estado[i] == '1' and estado_anterior_botoes[i] == '0':
                    acionar_led(i + 7, False)

            estado_anterior_botoes = botoes_estado.copy()
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Programa interrompido.")
        arduino.close()

if __name__ == '__main__':
    main()
