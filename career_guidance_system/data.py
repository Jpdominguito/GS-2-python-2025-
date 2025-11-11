from models import Competencia, Carreira

# 1. Dicionário de Competências
# Chave: Nome da Competência
# Valor: Objeto Competencia
COMPETENCIAS = {
    "Pensamento Analítico": Competencia(
        "Pensamento Analítico", "Soft", "Capacidade de resolver problemas complexos e tomar decisões baseadas em dados."
    ),
    "Resiliência e Flexibilidade": Competencia(
        "Resiliência e Flexibilidade", "Soft", "Capacidade de se adaptar a mudanças e lidar com pressão."
    ),
    "Criatividade e Inovação": Competencia(
        "Criatividade e Inovação", "Soft", "Habilidade de gerar novas ideias e soluções."
    ),
    "Colaboração e Liderança": Competencia(
        "Colaboração e Liderança", "Soft", "Habilidade de trabalhar em equipe e influenciar positivamente."
    ),
    "Lógica de Programação": Competencia(
        "Lógica de Programação", "Hard", "Fundamento essencial para o desenvolvimento de software."
    ),
    "Inteligência Artificial (IA)": Competencia(
        "Inteligência Artificial (IA)", "Hard", "Conhecimento em Machine Learning, Deep Learning e modelos de IA."
    ),
    "Cloud Computing": Competencia(
        "Cloud Computing", "Hard", "Conhecimento em plataformas de nuvem (AWS, Azure, GCP)."
    ),
    "Cibersegurança": Competencia(
        "Cibersegurança", "Hard", "Habilidade em proteger sistemas e dados contra ameaças."
    ),
    "Big Data e Análise": Competencia(
        "Big Data e Análise", "Hard", "Habilidade em processar e interpretar grandes volumes de dados."
    ),
}

# 2. Lista de Carreiras
# Valor: Objeto Carreira
CARREIRAS = [
    Carreira(
        "Engenheiro de Software",
        "Desenvolvimento e manutenção de sistemas e aplicações, com foco em escalabilidade e performance.",
        ["Lógica de Programação", "Cloud Computing", "Colaboração e Liderança"]
    ),
    Carreira(
        "Cientista de Dados",
        "Análise de dados complexos para extrair insights, construir modelos preditivos e prever tendências.",
        ["Big Data e Análise", "Inteligência Artificial (IA)", "Pensamento Analítico"]
    ),
    Carreira(
        "Especialista em Cibersegurança",
        "Proteção de redes, sistemas e dados contra ataques e vulnerabilidades, garantindo a integridade.",
        ["Cibersegurança", "Lógica de Programação", "Resiliência e Flexibilidade"]
    ),
    Carreira(
        "Arquiteto de Cloud",
        "Design e implementação de infraestruturas e serviços em nuvem, otimizando custos e recursos.",
        ["Cloud Computing", "Lógica de Programação", "Pensamento Analítico"]
    ),
    Carreira(
        "Especialista em IA/ML",
        "Criação, treinamento e otimização de modelos de Inteligência Artificial e Machine Learning.",
        ["Inteligência Artificial (IA)", "Lógica de Programação", "Criatividade e Inovação"]
    ),
]

# 3. Dicionário de Perfis (Simulação de armazenamento)
# Chave: Nome do Perfil
# Valor: Objeto Perfil
PERFIS_CADASTRADOS = {}
