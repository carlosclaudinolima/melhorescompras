import os
import json

chave_valor = 'valor'
chave_tipo_embalagem = 'tipo_embalagem'
chave_icms = 'valor_icms'
minimo_produtos = 5

dc_produtos = {}

sistema_operacional = os.name

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
        banner()
        numero_produto = len(dc_produtos)+1
        nome_produto = input(f'Digite a descrição do {numero_produto}º produto: ')
        if nome_produto.lstrip().rstrip() == '':
            input('O nome do produto deve ser preenchido.\nPressione uma tecla pra continuar...')
            nome_produto = ''
            continue
        try:
            dc_produtos[nome_produto]           
        except KeyError:
            dc_produtos[nome_produto] = {}
            while True:
                banner()
                try:
                    valor_produto = float(input(f'Digite o valor do produto "{nome_produto}": '))                    
                    if valor_produto <= 0:
                        raise ValueError
                except ValueError:
                    input('Valor inválido. O valor deve ser numérico e maior que zero.\nPressione uma tecla pra continuar...')
                    continue
                else:
                    dc_produtos[nome_produto][chave_valor] = valor_produto
                    dc_produtos[nome_produto][chave_icms] = (lambda  x: x * 18/100)(valor_produto)
                    break
            tipo_embalagem = input(f'Digite o tipo de embalagem para o produto "{nome_produto}": ')
            dc_produtos[nome_produto][chave_tipo_embalagem] = tipo_embalagem
        else:
            input(f'Descrição já existente "{nome_produto}"\nPressione uma tecla pra continuar...')
            nome_produto = ''
            continue
        
def salvar_json():
    produtos = json.dumps(dc_produtos, indent=4) 
    arquivo_json = '1_5_arquivo_produto.json'
    with open(arquivo_json, '+w') as f:
        f.write(produtos)

def main():
    while True:        
        cadastrar_produto()
        if input("\nDeseja cadastrar mais um produto ? (S/N) ").upper() != 'S':
            break
    if len(dc_produtos) >= minimo_produtos:
        salvar_json()

if __name__ == '__main__':
    main()