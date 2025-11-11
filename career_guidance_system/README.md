_# Sistema de Orientação de Carreiras - Future at Work

## 1. Descrição do Projeto e Propósito

Este projeto, desenvolvido para a disciplina de **Pensamento Computacional e Automação com Python** (GS 2025.2), consiste em um sistema de orientação de carreiras baseado em Python e Orientação a Objetos (OOP). O objetivo principal é simular uma **ferramenta inteligente de análise de perfis profissionais** do futuro, conectando as competências técnicas (Hard Skills) e comportamentais (Soft Skills) de um indivíduo com as carreiras emergentes no mercado de tecnologia.

O sistema permite o cadastro de perfis, a avaliação de competências em uma escala de 1 a 5, e a geração de **recomendações personalizadas** que incluem:
1.  **Carreiras mais adequadas** ao perfil, com base em um sistema de pontuação ponderada.
2.  **Trilhas de Aprimoramento** sugeridas para competências com baixa pontuação.

O foco da proposta é estimular a criação de soluções que preparem pessoas para o trabalho do futuro, utilizando a lógica de programação e a automação para o desenvolvimento humano e profissional.

## 2. Integrantes

| Nome Completo | RM |
| :--- | :--- |
| João Pedro Tomas Dominguito | 562166 |
| Luiz Gustavo Lima da Silva | 563554 |
| Vicente Casellato Rodriguez | 563865 |

## 3. Instruções de Execução

O sistema é uma aplicação de linha de comando (CLI) e requer apenas o Python 3 instalado.

### Pré-requisitos

*   Python 3.x

### Como Executar

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone [https://github.com/Jpdominguito/GS-2-python-2025-/tree/mainUI]
    cd career_guidance_system
    ```
2.  **Execute o arquivo principal** `main.py`:
    ```bash
    python3 main.py
    ```
3.  Siga as instruções do menu para cadastrar um novo perfil (Opção 1) e, em seguida, analisar o perfil (Opção 2) para obter as recomendações.

## 4. Estrutura de Arquivos e Classes

O projeto está organizado em módulos para atender ao requisito de código modularizado e Orientação a Objetos.

### Estrutura de Arquivos

```
career_guidance_system/
├── main.py         # Interface de Linha de Comando (CLI) e Menu Principal
├── models.py       # Definição das Classes (Competencia, Carreira, Perfil)
├── data.py         # Dados Iniciais (Seed Data) de Competências e Carreiras (Listas/Dicionários)
└── logic.py        # Lógica de Negócio (Função de Recomendação e Formatação)
```

### Modelo de Classes (Orientação a Objetos)

O sistema utiliza três classes principais, representando o modelo de dados:

| Classe | Propósito | Atributos Principais | Métodos Principais |
| :--- | :--- | :--- | :--- |
| **`Competencia`** | Define uma habilidade (Hard ou Soft Skill). | `nome`, `tipo`, `descricao` | `__init__` |
| **`Carreira`** | Define uma área profissional. | `nome`, `descricao`, `competencias_chave` (Lista) | `__init__` |
| **`Perfil`** | Armazena o perfil do usuário. | `nome`, `competencias` (Dicionário) | `__init__`, `adicionar_competencia` |

## 5. Demonstração (Prints)

Abaixo, um exemplo da interação com o sistema:

### Menu Principal
```
==================================================
SISTEMA DE ORIENTAÇÃO DE CARREIRAS - FUTURE AT WORK
==================================================
1. Cadastrar Novo Perfil
2. Analisar Perfil Existente
3. Listar Perfis Cadastrados
4. Sair
==================================================
Escolha uma opção: 1
```

### Relatório de Recomendação (Exemplo)
```
==================================================
RELATÓRIO DE ORIENTAÇÃO DE CARREIRA
==================================================
1. CARREIRAS MAIS ADEQUADAS:

1. Arquiteto de Cloud (Score de Adequação: 12/15)
   Descrição: Design e implementação de infraestruturas e serviços em nuvem, otimizando custos e recursos.
   Competências Chave: Cloud Computing, Lógica de Programação, Pensamento Analítico

2. Engenheiro de Software (Score de Adequação: 9/15)
   Descrição: Desenvolvimento e manutenção de sistemas e aplicações, com foco em escalabilidade e performance.
   Competências Chave: Lógica de Programação, Cloud Computing, Colaboração e Liderança
   *Atenção: Competências Chave não avaliadas: Colaboração e Liderança*

3. Especialista em Cibersegurança (Score de Adequação: 7/15)
   Descrição: Proteção de redes, sistemas e dados contra ataques e vulnerabilidades, garantindo a integridade.
   Competências Chave: Cibersegurança, Lógica de Programação, Resiliência e Flexibilidade
   *Atenção: Competências Chave não avaliadas: Resiliência e Flexibilidade*

--------------------------------------------------
2. TRILHAS DE APRIMORAMENTO SUGERIDAS:

- Cibersegurança (Pontuação: 2/5)
  Aprimorar Cibersegurança (Hard). Sugestão: Buscar cursos e projetos práticos sobre Cibersegurança.

- Criatividade e Inovação (Pontuação: 1/5)
  Aprimorar Criatividade e Inovação (Soft). Sugestão: Buscar cursos e projetos práticos sobre Criatividade e Inovação.

==================================================
```
