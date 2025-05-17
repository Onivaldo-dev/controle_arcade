import keyboard
import time

# Função para acionar ou desligar um LED (aqui simulando no PC)
def acionar_led(led_id, acionar=True):
    """Função para simular a ativação de LEDs no computador com a biblioteca keyboard."""
    if acionar:
        print(f"LED {led_id} acionado.")  # Simula o acionamento do LED
    else:
        print(f"LED {led_id} desligado.")  # Simula o desligamento do LED

def main():
    try:
        # Mapeamento das teclas para os botões
        botoes = {
            'a': 1,  # Tecla 'a' mapeada para o botão 1
            's': 2,  # Tecla 's' mapeada para o botão 2
            'd': 3,  # Tecla 'd' mapeada para o botão 3
            'f': 4,  # Tecla 'f' mapeada para o botão 4
            'g': 5,  # Tecla 'g' mapeada para o botão 5
            'h': 6,  # Tecla 'h' mapeada para o botão 6
            'j': 7,  # Tecla 'j' mapeada para o botão 7
            'k': 8,  # Tecla 'k' mapeada para o botão 8
        }

        while True:
            for tecla, led_id in botoes.items():
                if keyboard.is_pressed(tecla):  # Verifica se a tecla foi pressionada
                    acionar_led(led_id, True)  # Aciona o LED (simulado)
                else:
                    acionar_led(led_id, False)  # Desliga o LED (simulado)

            # Atraso para não sobrecarregar o loop
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Programa interrompido.")

if __name__ == '__main__':
    main()
