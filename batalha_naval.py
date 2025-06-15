
def criar_tabuleiro():
    n_linha = 20
    tabuleiro = []
    for linha in range (n_linha):
        linha_tab = ['~'] * 20
        tabuleiro.append(linha_tab)
               
    return tabuleiro

def exibir_tabuleiro(tabuleiro):
    cabecalho = "  "
    for i in range(20):
        if i + 1 < 10:
            cabecalho += f" {i + 1} "
        else:
            cabecalho += f"{i + 1} "
    print(cabecalho)
    for linha_index in range(20):
        letra = chr(65 + linha_index)
        conteudo = ""
        for coluna_index in range(20):
            conteudo += tabuleiro[linha_index][coluna_index].rjust(2) + " "
        print(f"{letra} {conteudo}")

def simbolo_indice(simbolo):
    if simbolo == "P":
        return 0
    elif simbolo == "C":
        return 1
    elif simbolo == "F":
        return 2
    return -1

def navios_vivos(partes_restantes):
    for restante in partes_restantes:
        if restante > 0:
            return True
    return False 

def verificar_afundados(partes_restantes):
    for restante in partes_restantes:
        if restante != 0:
            return False
    return True
def informacoes(nome,quantidade,tamanho, pontuacoes_navios):
    tabela = []
    for navio in range(len(nome)):
        linha = [nome[navio],quantidade[navio],tamanho[navio],pontuacoes_navios[navio]]
        tabela.append(linha)
    return tabela


def posicionar_navio(tabuleiro, nome_navio,quantidade,tamanho,simbolo):
    for numero_navio in range(quantidade):
        for posicoes_validas in range(100):
            exibir_tabuleiro(tabuleiro)
            posicao_navio = input(f"\n ==Em qual posição você deseja posiconar o(a) {nome_navio} #{numero_navio + 1} (EX: A10)==")
                
            linha = ord(posicao_navio[0]) - 65
            coluna = int(posicao_navio[1:]) - 1
            
            if coluna + tamanho > 20:
                print("O Navio não cabe nesta linha, tente novamente")
                continue
            
            sobreposicao = False
            for deslocamento in range(tamanho):
                if tabuleiro[linha][coluna + deslocamento] != "~" :
                    sobreposicao = True
                    break
            
            if sobreposicao:
                print('Ja existe um navio nesta posição, tente novamente!')
                continue

            for posicionamento_auto in range(tamanho):
                tabuleiro[linha][coluna + posicionamento_auto] = simbolo
            break

def atacar(tabuleiro_real,tabuleiro_ataque,pontuacao,partes_restantes,tamanhos_navios,nomes_navios,pontuacoes_navios):
    while navios_vivos(partes_restantes):
        print("\n +-+-+-+-+-+-+-+-+-+ ATAQUE +-+-+-+-+-+-+-+-+-+")
        exibir_tabuleiro(tabuleiro_ataque)
        coordenada = input("Escolha onde você irá atacar (EX: C11): ")
        letra = coordenada[0]
        numero = coordenada[1:]
        linha = ord(coordenada[0]) - 65
        coluna = int(coordenada[1:]) - 1
        
        if not (0 <= linha < 20 and 0 <= coluna <20):
            print('Coordenada fora do tabuleiro!')
            continue
        if tabuleiro_ataque[linha][coluna] in ["X","O"]:
            print("Coordenada já sofreu ataque, tente outra!")
            continue
        
        alvo = tabuleiro_real[linha][coluna]
        indice = simbolo_indice(alvo)
        
        if indice != -1:
            tabuleiro_real[linha][coluna] = "X"
            tabuleiro_ataque[linha][coluna] = "X"
            print("ACERTOU!!!")
            partes_restantes[indice] -= 1
            
            
            if partes_restantes[indice] % tamanhos_navios[indice] == 0:
                pontuacao[0] += pontuacoes_navios[indice]
                print(f"Você afundou um {nomes_navios[indice]}! (+{pontuacoes_navios[indice]} pontos)")
                
        else:
            tabuleiro_ataque[linha][coluna] = "O"
            print("Errou...Tente novamente!")
        
        if verificar_afundados(partes_restantes):
            print("\n Todos os navios afundaram!!")
            print(f"Pontuação Final: {pontuacao[0]} pontos")
            break
       
        continuar = input("Deseja continuar jogando ? (S/N) ")
        while continuar not in ("S", "N"):
            print("Para continuar você deve digitar S ou N, tente novamente!")
            continuar = input("Deseja continuar jogando ? (S/N) ")

        if continuar == "N":
            print(f"\n Jogo Encerrado pelo jogador")
            print(f"Pontuação Final: {pontuacao[0]} pontos")
            return False
            
        

def gerar_tabuleiro_teste():
    tabuleiro = criar_tabuleiro()

    # Porta-Aviões (3 unidades de 4 células)
    tabuleiro[0][0:4] = ["P"] * 4
    tabuleiro[2][5:9] = ["P"] * 4
    tabuleiro[4][10:14] = ["P"] * 4

    # Cruzadores (4 unidades de 3 células)
    tabuleiro[6][0:3] = ["C"] * 3
    tabuleiro[7][5:8] = ["C"] * 3
    tabuleiro[8][10:13] = ["C"] * 3
    tabuleiro[9][15:18] = ["C"] * 3

    # Fragatas (5 unidades de 2 células)
    tabuleiro[11][0:2] = ["F"] * 2
    tabuleiro[12][3:5] = ["F"] * 2
    tabuleiro[13][6:8] = ["F"] * 2
    tabuleiro[14][9:11] = ["F"] * 2
    tabuleiro[15][12:14] = ["F"] * 2

    return tabuleiro        

    
        
print("Bem vindo ao Batalha Naval!!! \n") 
         
tamanhos_navios = [4, 3, 2]
quantidades_navios = [3, 4, 5]
simbolos_navios = ["P", "C", "F"]
nomes_navios = ["Porta-Aviões", "Cruzador", "Fragata"]
pontuacoes_navios = [30, 20, 10]

partes_restantes = [
    quantidades_navios[0] * tamanhos_navios[0],
    quantidades_navios[1] * tamanhos_navios[1],
    quantidades_navios[2] * tamanhos_navios[2] 
]
pontuacao = [0]
escolha = ""

print('Informações do Jogo:\n')
informacoes_tabela = informacoes(nomes_navios,quantidades_navios,tamanhos_navios,pontuacoes_navios)
print("Navios          | Quantidades | Tamanhos | Pontos")
print("-" * 50)
for linha in informacoes_tabela:
    print(f"{linha[0]:15} | {linha[1]:^11} | {linha[2]:^8} | {linha[3]:^6}\n")     
while escolha !="0":
    print("=-=-=-=Escolha o modo de jogo:=-=-=-= \n")
    print("1 - Posicionar manualmente os navios")
    print("2 - Usar tabuleiro pronto para teste")
    print("0 - Sair do jogo")
    escolha = input("Sua escolha é: ")
    
    tabuleiro_ataque = criar_tabuleiro()
    tabuleiro_real = ""
    if escolha == "0":
        print("Saindo do Jogo")
        break
    elif escolha == "1":
        tabuleiro_real = criar_tabuleiro()
        for indice_navio in range(3):
            posicionar_navio(
                tabuleiro_real,
                nomes_navios[indice_navio],
                quantidades_navios[indice_navio],
                tamanhos_navios[indice_navio],
                simbolos_navios[indice_navio]
            )
        break  
    elif escolha == "2":
        tabuleiro_real = gerar_tabuleiro_teste()
        print("\n Tabuleiro para testes gerado automaticamente!")
        exibir_tabuleiro(tabuleiro_real)
        break
    else:
        print("Opção Invalida, Escolha somente 1, 2 ou 0!")

while escolha == "1" or escolha == "2":
    atacar(tabuleiro_real,tabuleiro_ataque,pontuacao,partes_restantes,tamanhos_navios,nomes_navios,pontuacoes_navios)
    break