import sys

def complemento2(stringBinaria):
    # trocar todos os bits
    stringBinaria = stringBinaria.replace('1', '2')
    stringBinaria = stringBinaria.replace('0', '1')
    stringBinaria = stringBinaria.replace('2', '0')

    # fazendo a soma do 1 enquanto for necessario
    vaiUm = 1
    i = len(stringBinaria) - 1
    stringResultado = ""

    while (vaiUm):
        vaiUm = 0

        if i == -1:
            break

        if stringBinaria[i] == "0":
            stringResultado = "1" + stringResultado
        else:
            vaiUm = 1
            stringResultado = "0" + stringResultado
        i = i - 1

    # adicionando o restante dos caracteres(se houver) na string resultante
    for j in range(i, -1, -1):
        stringResultado = stringBinaria[j] + stringResultado

    return stringResultado


def function7(instrucao):
    function7conjunto1 = ["add", "sll", "xor", "srl", "or", "and"]
    function7conjunto2 = ["sub"]

    funct7 = ""

    if (instrucao in function7conjunto1):
        funct7 += "0000000"
    elif (instrucao in function7conjunto2):
        funct7 += "0100000"

    return funct7


def function3(instrucao):
    funct3 = ""

    if (instrucao == "add" or instrucao == "sub" or instrucao == "addi"):
        funct3 += "000"

    elif (instrucao == "or" or instrucao == "ori"):
        funct3 += "110"

    elif (instrucao == "xor"):
        funct3 += "100"

    elif (instrucao == "sll"):
        funct3 += "001"

    elif (instrucao == "srl"):
        funct3 += "101"

    elif (instrucao == "and" or instrucao == "andi"):
        funct3 += "111"

    return funct3


def opcode(instrucao):
    # INSTRUÇÃO DO OPCODE (0110011)
    opcode1 = ['add', 'sub', 'xor', 'srl', 'or', 'and', 'sll']
    # INSTRUÇÃO DO OPCODE (0010011)
    opcode2 = ['addi', 'andi', 'ori']

    opcode = ""

    if instrucao in opcode1:
        opcode += "0110011"

    elif instrucao in opcode2:
        opcode += "0010011"

    return opcode


def ConversaoBinaria(instrucao, rd, rs1, rs2):
    # Variavel que retornará a instrução completa
    resultado = ""

    instrucoesImediatas = ["addi", "andi", "ori"]  # aparentemente nao tem function 7

    # Adicionando function7 a string resultado
    resultado += function7(instrucao)

    # Removendo x das variaveis
    rd = rd.replace("x", "")
    rs1 = rs1.replace("x", "")
    rs2 = rs2.replace("x", "")

    # Inserindo o rs2 no resultado de acordo com cada caso (imediato ou nao)
    if (instrucao in instrucoesImediatas):

        if ((int)(rs2) > 0):
            resultado += format((int)(rs2), "b").zfill(12)

        else:
            rs2 = str((int)(rs2) * (-1))
            rs2 = format((int)(rs2), "b").zfill(12)

            rs2 = complemento2(rs2)

            resultado += rs2

    else:
        resultado += format((int)(rs2), "b").zfill(5)

    # Inserindo rs1 no resultado
    resultado += format((int)(rs1), "b").zfill(5)

    # Adicionando function3 a string resultado
    resultado += function3(instrucao)

    # Adicionando o registrador de destino
    resultado += format((int)(rd), "b").zfill(5)

    # Adicionando opcode ao resultado
    resultado += opcode(instrucao)

    if (len(sys.argv) > 2 and sys.argv[2]=="-o"):
        ArquivoSaida(resultado)
    else:
        print(resultado)

def ArquivoEntrada():
    arquivo = open("entrada/"+sys.argv[1], "r")
    for linha in arquivo:
        if (linha == '\n'):
            break
        linha = linha.split()
        instrucao = linha[0]
        rd = linha[1].replace(",", "")
        rs1 = linha[2].replace(",", "")
        rs2 = linha[3]
        ConversaoBinaria(instrucao, rd, rs1, rs2)
    arquivo.close()

def ArquivoSaida(resultado):
    arquivo = open("saida/"+sys.argv[3], 'r+')
    conteudo = arquivo.readlines()
    # inserindo o novo valor de saída, que se encontra na variavel resultado
    conteudo.append(resultado)
    conteudo.append("\n")
    arquivo = open("saida/"+sys.argv[3], "w")
    arquivo.writelines(conteudo)
    arquivo.close()


if("-o" in sys.argv):
    if(".txt" not in sys.argv[3]):
        sys.argv[3] = sys.argv[3] + ".txt"
    arquivo = open("saida/"+sys.argv[3], 'w')

ArquivoEntrada()
