import os

sistema_operacional = os.name
dc_produtos = {}

def limpa_tela():
    if sistema_operacional == 'nt':
        os.system('cls')
    elif sistema_operacional == 'posix':
        os.system('clear')


def banner():
    limpa_tela()
    melhores_compras = """
    ░█▀▄▀█ █▀▀ █── █──█ █▀▀█ █▀▀█ █▀▀ █▀▀ 　 ░█▀▀█ █▀▀█ █▀▄▀█ █▀▀█ █▀▀█ █▀▀█ █▀▀ 
    ░█░█░█ █▀▀ █── █▀▀█ █──█ █▄▄▀ █▀▀ ▀▀█ 　 ░█─── █──█ █─▀─█ █──█ █▄▄▀ █▄▄█ ▀▀█ 
    ░█──░█ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ 　 ░█▄▄█ ▀▀▀▀ ▀───▀ █▀▀▀ ▀─▀▀ ▀──▀ ▀▀▀"""
    print(melhores_compras)
    print('\n\n')
    


def cadastrar_produto():
    numero_produto = len(dc_produtos)+1
    nome_produto = ''
    while nome_produto == '':
        nome_produto = input(f'Digite o nome do produto #{numero_produto} ')
        print(nome_produto)

def main():
    banner()
    while True:
        cadastrar_produto()
        if input("Deseja cadastrar mais um produto ? (S/N) ").upper() != 'S':
            break


if __name__ == '__main__':
    main()