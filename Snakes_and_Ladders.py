from time import sleep
from random import randint
from colorama import Fore, Back


casasEspeciais = {
    # escadas
    4: 14, 8: 31, 15: 44, 19: 39, 34: 54, 41: 61, 45: 56, 57: 74, 62: 81, 69: 88, 76: 95, 80: 99, 87: 94,
    # cobras
    97: 78, 91 : 72, 82: 63, 74: 53, 65: 51, 53: 33, 47: 26, 38: 20, 30: 11, 25: 5, 16: 7,
}


def coordenada_posicao(linha, coluna):
    #Converte coordenadas (linha, coluna) para uma posição no tabuleiro (1-100) para o tabuleiro serpentear
    # Para linha sim linha não, a ordem da coluna é invertida para criar o serpenteado
    if linha % 2 != 0:
        coluna = 9 - coluna
    return linha * 10 + coluna + 1


def imprime_tabuleiro(pos_jogador, pino_jogador, pos_computador):
    """Imprime dinamicamente o tabuleiro com as posições dos jogadores."""
    escadas = {4, 8, 15, 19, 34, 41, 45, 57, 62, 69, 76, 80, 84, 87}
    cobras = {97, 82, 74, 65, 53, 47, 38, 30, 25, 16}

    print()  # Linha extra para espaçamento
    for r in range(9, -1, -1):
        linha_casas = []
        
        # Determina a ordem da coluna para imprimir da esquerda para a direita ou da direita para a esquerda
        for c in range(10):
            pos = coordenada_posicao(r, c)
            
            # Determina qual caractere mostrar para os jogadores
            caractere_pino = " "
            if pos == pos_jogador and pos == pos_computador:
                caractere_pino = f"{Fore.GREEN}{Back.BLUE}{pino_jogador}{Back.RESET}{Fore.RED}{Back.YELLOW}M{Back.RESET}{Fore.WHITE}"
            elif pos == pos_jogador:
                caractere_pino = f"{Fore.GREEN}{Back.BLUE}{pino_jogador}{Back.RESET}{Fore.WHITE}"
            elif pos == pos_computador:
                caractere_pino = f"{Fore.RED}{Back.YELLOW}M{Back.RESET}{Fore.WHITE}"

            # Determina se é uma cobra ou escada
            caractere_especial = " "
            if pos in escadas:
                caractere_especial = f"{Fore.GREEN}H{Fore.WHITE}"
            elif pos in cobras:
                caractere_especial = f"{Fore.RED}S{Fore.WHITE}"

            # Formata a string da casa, preenchendo numero por numero e colocando zero a esquerda sempre que necessario
            pos_str = f"{pos:02d}" if pos < 100 else str(pos)
            casa = f"[{Fore.CYAN}{pos_str}{Fore.WHITE}({caractere_especial}{caractere_pino})]"
            linha_casas.append(casa)

        print("".join(linha_casas))
    print()


def regras():
    print("-=-= Bem Vindo ao Jogo Cobras e Escadas! =-=-")
    sleep(1)
    regras_input = str(input("\n|Quer ver algumas regras? (S/N) "))
    if regras_input in "Ss":
        while True:
            print("\n|O jogo consiste em uma corrida para ver quem chega primeiro no espaço 100 do tabuleiro!"
                  "\n|Na versão do jogo que você vai jogar agora, você e o computador (representado por um M) vão alternar turnos para rodar o dado de 1 até 6"
                  "\n|No tabuleiro, as Cobras são representadas por um 'S' e as Escadas são representadas pela letra 'H'"
                  "\n|As Cobras levam você para baixo no tabuleiro e as Escadas o levam para cima, mais perto da vitória!"
                  "\n|Boa sorte na sua jogatina!")
            de_novo = str(input("\n|Quer ver as regras de novo? (S/N) "))
            if de_novo in "Nn":
                print("\n|Então vamos para o jogo!")
                sleep(1)
                break
    else:
        print("\n|Então vamos para o jogo!")
        sleep(1)




def pino_Jogador():
    while True:
        pino = input("\n|Escolha um caractere para o seu personagem: ").strip() #strip pra precalção
        if pino and pino.upper() != 'M': 
            print("\n|Colocando o seu pino no tabuleiro...\n")
            sleep(2)
            return pino[0]
        elif pino == 'M': #checando se o jogador não escolhe M
            print("\n|'M' é reservado para o computador. Escolha outro caractere.")
        else:
            print("\n|Por favor, digite um caractere.")


def roda_dados():
    return randint(1, 6)


def turno_jogador():
    print(f"\n|É a sua vez!")

    forca = 0
    forca = int(input("|Digite a força que você quer jogar os dados em uma escala de 1 até 10: "))
    sleep(1)

    dado1 = roda_dados()
    dado2 = roda_dados()
    somadados = dado1 + dado2

    if forca <= 3:
        print("\n|Os dados quase não saem da sua mão!")
    elif forca <= 6:
        print("\n|Os dados caem perfeitamente na mesa!")
    else:
        print("\n|Os dados quase saem da mesa!")
    sleep(1)

    print(f"\n|Seus dados rodaram um {dado1} e um {dado2}! Você pode andar {somadados} casas!")
    sleep(1)

    return somadados


def turno_computador():
    print(f"\n|É a vez do computador (M)!")
    sleep(1)

    falaComputador = randint(1, 3)
    if falaComputador == 1:
        print("\n|O computador está rodando os seus dados!")
    elif falaComputador == 2:
        print("\n|O computador calcula qual a jogada perfeita!")
    else:
        print("\n|O computador atualizou os drivers!")
    sleep(1)

    dado1 = roda_dados()
    dado2 = roda_dados()
    somadados = dado1 + dado2

    print(f"\n|Os dados do computador rodaram um {dado1} e um {dado2}! Ele vai andar {somadados} casas!")
    sleep(1)

    return somadados


def main():
    regras()
    pino_jogador = pino_Jogador()

    pos_jogador = 1
    pos_computador = 1

    print("\n-=-=-=-= COMEÇANDO O JOGO =-=-=-=-")
    sleep(2)

    imprime_tabuleiro(pos_jogador, pino_jogador, pos_computador)
    
    print("\n|Boa sorte nos seus dados!")
    
    while True:
        # Turno do Jogador
        movimento = turno_jogador()
        pos_jogador += movimento
        if pos_jogador > 100:
            pos_jogador = 100

        print(f"|Você avançou para a casa {pos_jogador}.")
        sleep(1)

        if pos_jogador in casasEspeciais: #chamando o dicionario de casas especiais
            nova_pos = casasEspeciais[pos_jogador]
            if nova_pos > pos_jogador:
                print(f"|{Fore.GREEN}Que sorte!{Fore.WHITE} Você achou uma escada na casa {pos_jogador} e subiu para {nova_pos}!")
            else:
                print(f"|{Fore.RED}Oh não!{Fore.WHITE} Você caiu em uma cobra na casa {pos_jogador} e desceu para {nova_pos}!")
            pos_jogador = nova_pos
            sleep(2)

        imprime_tabuleiro(pos_jogador, pino_jogador, pos_computador)

        if pos_jogador == 100:
            print(f"\n-=-=-=-= {Fore.GREEN}PARABÉNS {Fore.GREEN}{Back.BLUE}{pino_jogador}{Back.RESET}{Fore.GREEN}! VOCÊ VENCEU!{Fore.WHITE} =-=-=-=-")
            break

        # Turno do Computador
        movimento = turno_computador()
        pos_computador += movimento
        if pos_computador > 100:
            pos_computador = 100

        print(f"|O computador avançou para a casa {pos_computador}.")
        sleep(1)

        if pos_computador in casasEspeciais:
            nova_pos = casasEspeciais[pos_computador]
            if nova_pos > pos_computador:
                print(f"|O computador achou uma escada na casa {pos_computador} e subiu para {nova_pos}!")
            else:
                print(f"|O computador caiu em uma cobra na casa {pos_computador} e desceu para {nova_pos}!")
            pos_computador = nova_pos
            sleep(2)

        imprime_tabuleiro(pos_jogador, pino_jogador, pos_computador)

        if pos_computador == 100:
            print(f"\n-=-=-=-= {Fore.RED}O COMPUTADOR VENCEU! TENTE NOVAMENTE!{Fore.WHITE} =-=-=-=-")
            break



main()
