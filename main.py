import os

sistema_operacional = os.name
dc_produtos = {}
chave_valor = 'Valor'
chave_tipo_embalagem = 'TipoEmbalagem'

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
    
    nome_produto = ''
    while nome_produto == '':
        numero_produto = len(dc_produtos)+1
        nome_produto = input(f'Digite a descrição do produto #{numero_produto} ')
        try:
            dc_produtos[nome_produto]           
        except KeyError:
            dc_produtos[nome_produto] = {}
            while True:
                banner()
                try:
                    valor_produto = float(input(f'Digite um valor válido para o produto "{nome_produto}": '))
                except ValueError:
                    continue
                else:
                    dc_produtos[nome_produto][chave_valor] = valor_produto
                    break
            tipo_embalagem = input(f'Digite o tipo de embalagem para o produto "{nome_produto}": ')
            dc_produtos[nome_produto][chave_tipo_embalagem] = tipo_embalagem
        else:
            print(f'Descrição já existente "{nome_produto}"')
            continue
            

def main():
    while True:
        banner()
        cadastrar_produto()
        if input("Deseja cadastrar mais um produto ? (S/N) ").upper() != 'S':
            break


if __name__ == '__main__':
    main()