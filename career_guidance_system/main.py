from models import Perfil
from data import COMPETENCIAS, PERFIS_CADASTRADOS
from logic import gerar_recomendacao, formatar_recomendacao

def exibir_menu():
    """Exibe o menu principal da aplicação."""
    print("\n" + "="*50)
    print("SISTEMA DE ORIENTAÇÃO DE CARREIRAS - FUTURE AT WORK")
    print("="*50)
    print("1. Cadastrar Novo Perfil")
    print("2. Analisar Perfil Existente")
    print("3. Listar Perfis Cadastrados")
    print("4. Sair")
    print("="*50)

def cadastrar_perfil():
    """Permite ao usuário cadastrar um novo perfil e avaliar suas competências."""
    print("\n--- CADASTRO DE NOVO PERFIL ---")
    
    while True:
        nome_perfil = input("Digite o nome do perfil (ex: João Pedro): ").strip()
        if nome_perfil and nome_perfil not in PERFIS_CADASTRADOS:
            break
        elif nome_perfil in PERFIS_CADASTRADOS:
            print("Erro: Já existe um perfil com este nome. Tente outro.")
        else:
            print("Erro: O nome do perfil não pode ser vazio.")

    novo_perfil = Perfil(nome_perfil)
    
    print("\n--- AVALIAÇÃO DE COMPETÊNCIAS ---")
    print("Avalie seu nível em cada competência de 1 (Básico) a 5 (Avançado).")
    
    competencias_list = list(COMPETENCIAS.values())
    
    for comp in competencias_list:
        while True:
            try:
                pontuacao = int(input(f"Avalie '{comp.nome}' ({comp.tipo}): "))
                if 1 <= pontuacao <= 5:
                    novo_perfil.adicionar_competencia(comp.nome, pontuacao)
                    break
                else:
                    print("Erro: A pontuação deve ser um número inteiro entre 1 e 5.")
            except ValueError:
                print("Erro: Entrada inválida. Digite um número inteiro.")

    PERFIS_CADASTRADOS[nome_perfil] = novo_perfil
    print(f"\nPerfil '{nome_perfil}' cadastrado com sucesso!")

def analisar_perfil():
    """Permite ao usuário selecionar um perfil existente e gerar a recomendação."""
    if not PERFIS_CADASTRADOS:
        print("\nErro: Nenhum perfil cadastrado. Cadastre um perfil primeiro (Opção 1).")
        return

    print("\n--- ANÁLISE DE PERFIL EXISTENTE ---")
    listar_perfis()
    
    while True:
        nome_perfil = input("Digite o nome do perfil que deseja analisar: ").strip()
        if nome_perfil in PERFIS_CADASTRADOS:
            perfil_selecionado = PERFIS_CADASTRADOS[nome_perfil]
            break
        else:
            print("Erro: Perfil não encontrado. Verifique a lista e tente novamente.")

    # Gera e exibe a recomendação
    resultado = gerar_recomendacao(perfil_selecionado)
    print(formatar_recomendacao(resultado))

def listar_perfis():
    """Lista todos os perfis cadastrados."""
    if not PERFIS_CADASTRADOS:
        print("\nNenhum perfil cadastrado.")
        return
    
    print("\n--- PERFIS CADASTRADOS ---")
    for nome in PERFIS_CADASTRADOS.keys():
        print(f"- {nome}")

def main():
    """Função principal que executa o loop da aplicação."""
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            cadastrar_perfil()
        elif escolha == '2':
            analisar_perfil()
        elif escolha == '3':
            listar_perfis()
        elif escolha == '4':
            print("\nObrigado por usar o Sistema de Orientação de Carreiras. Até mais!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 4.")

if __name__ == "__main__":
    main()
