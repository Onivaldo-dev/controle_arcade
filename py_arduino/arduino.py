import serial
import time

# Abra a porta serial com a mesma taxa de baud definida no Arduino (9600)
arduino = serial.Serial('COM6', 9600)  # Troque 'COM3' pela porta correta do seu Arduino
time.sleep(2)  # Aguarde a conexão ser estabelecida

def ler_botoes():
    """Função para ler os estados dos botões do Arduino"""
    arduino.write(b'R')  # Envia um comando para o Arduino ler os botões (R = Read)
    data = arduino.readline().decode('utf-8').strip()  # Lê a resposta do Arduino
    return data.split(',')

def acionar_led(led_id, acionar=True):
    """Função para acionar ou desligar um LED no Arduino"""
    if acionar:
        arduino.write(f'S{led_id}1'.encode())  # Envia comando para acionar o LED
    else:
        arduino.write(f'S{led_id}0'.encode())  # Envia comando para desligar o LED

def main():
    try:
        while True:
            # Lê o estado dos botões
            botoes_estado = ler_botoes()

            # Exibe o estado dos botões (em formato binário)
            print(f"Estados dos botões: {botoes_estado}")

            # Aqui você pode implementar a lógica para controlar os LEDs com base no estado dos botões
            # Por exemplo, acionar LEDs se determinados botões forem pressionados
            if botoes_estado[0] == '0':  # Se o botão 4 for pressionado
                acionar_led(7, True)
            else:
                acionar_led(7, False)

            if botoes_estado[1] == '0':  # Se o botão 5 for pressionado
                acionar_led(8, True)
            else:
                acionar_led(8, False)

            # Atraso para não enviar dados em excesso
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Programa interrompido.")
        arduino.close()

if __name__ == '__main__':
    main()
