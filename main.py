"""
Sistema de Gerenciamento Acadêmico (SGA-Python)

Este script consolida a estrutura de dados, o motor de lógica e a interface
de terminal para gerenciamento de notas de estudantes.
"""

# ==============================================================================
# 1. INICIALIZAÇÃO DA ESTRUTURA DE DADOS
# ==============================================================================
# Lista global que armazenará os dicionários de cada estudante na memória
cadastro_estudantes = []


# ==============================================================================
# 2. MOTOR DE LÓGICA E PROCESSAMENTO (PEP 8 & DOCSTRINGS)
# ==============================================================================
def calcular_media(lista_notas):
    """
    Calcula a média aritmética simples de uma lista de notas flutuantes.

    Esta função soma todas as notas fornecidas e divide pelo número total de 
    elementos. Possui um mecanismo de segurança para tratar coleções vazias e 
    prevenir falhas de execução por divisão por zero.

    Args:
        lista_notas (list of float): Uma lista contendo as notas do estudante.

    Returns:
        float: A média resultante das notas. Retorna 0.0 se a lista estiver vazia.
    """
    if not lista_notas:
        return 0.0
    
    return sum(lista_notas) / len(lista_notas)


def verificar_aprovacao(media_final, nota_corte=7.0):
    """
    Avalia se a média final atinge o critério mínimo para aprovação.

    Compara a média obtida pelo estudante com a nota de corte institucional 
    para determinar seu status acadêmico.

    Args:
        media_final (float): A média de notas processada do estudante.
        nota_corte (float, optional): A nota mínima exigida para ser aprovado. 
            O valor padrão é 7.0.

    Returns:
        str: 'Aprovado' se a média for maior ou igual à nota_corte, 
            caso contrário, 'Reprovado'.
    """
    if media_final >= nota_corte:
        return 'Aprovado'
    else:
        return 'Reprovado'


# ==============================================================================
# 3. RELATÓRIOS E EXIBIÇÃO DE DADOS
# ==============================================================================
def generar_relatorio(lista_estudantes):
    """
    Consolida e exibe em bloco o rendimento acadêmico de todos os estudantes.

    Itera sobre a estrutura de dados dos estudantes cadastrados, aciona as 
    funções de lógica para calcular as médias e processar as aprovações, 
    imprimindo uma tabela formatada diretamente no terminal.

    Args:
        lista_estudantes (list of dict): Uma lista onde cada dicionário representa 
            um estudante e deve conter obrigatoriamente as chaves 'nome' (str) 
            e 'notas' (list of float).

    Returns:
        None: A função realiza apenas a exibição de dados (print) e não possui 
            valor de retorno.
    """
    if not lista_estudantes:
        print("\n--- NENHUM ESTUDANTE CADASTRADO NO SISTEMA ---")
        return

    print("\n" + "="*50)
    print(f"{'RELATÓRIO DE RENDIMENTO ACADÊMICO':^50}")
    print("="*50)
    print(f"{'Nome do Estudante':<25} | {'Média':<6} | {'Situação':<10}")
    print("-"*50)

    for estudante in lista_estudantes:
        nome_estudante = estudante["nome"]
        notas_estudante = estudante["notas"]
        
        media_calculada = calcular_media(notas_estudante)
        situacao_final = verificar_aprovacao(media_calculada)
        
        print(f"{nome_estudante:<25} | {media_calculada:<6.1f} | {situacao_final:<10}")
        
    print("="*50 + "\n")


# ==============================================================================
# 4. INTERFACE DO USUÁRIO (MENU INTERATIVO CLI)
# ==============================================================================
def menu_principal():
    """
    Gerencia o fluxo de execução do programa no terminal, oferecendo opções
    de cadastro, visualização de relatórios e encerramento.
    """
    while True:
        print("=== MENU GERENCIAL ACADÊMICO ===")
        print("1. Cadastrar Novo Estudante")
        print("2. Gerar Relatório de Rendimento")
        print("3. Sair do Sistema")
        
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            nome = input("\nDigite o nome do estudante: ").strip()
            if not nome:
                print("Erro: O nome do estudante não pode ser vazio.\n")
                continue
                
            notas = []
            print("Digite as notas do estudante (ou pressione Enter sem digitar nada para finalizar):")
            while True:
                entrada_nota = input(f"Digite a nota {len(notas) + 1}: ").strip()
                if entrada_nota == "":
                    break
                try:
                    nota = float(entrada_nota)
                    notas.append(nota)
                except ValueError:
                    print("Por favor, insira um número válido (ex: 7.5).")
            
            # Adiciona o novo dicionário estruturado à nossa lista na memória
            novo_estudante = {"nome": nome, "notas": notas}
            cadastro_estudantes.append(novo_estudante)
            print(f"✔ {nome} cadastrado com sucesso!\n")
            
        elif opcao == "2":
            generar_relatorio(cadastro_estudantes)
            
        elif opcao == "3":
            print("\nEncerrando o sistema acadêmico. Até logo!")
            break
        else:
            print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.\n")


if __name__ == "__main__":
    # Inicia o programa apenas se ele for executado diretamente
    menu_principal()