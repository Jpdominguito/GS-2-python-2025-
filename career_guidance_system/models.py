class Competencia:
    """Representa uma habilidade específica, técnica (Hard Skill) ou comportamental (Soft Skill)."""
    def __init__(self, nome: str, tipo: str, descricao: str):
        self.nome = nome
        self.tipo = tipo  # Ex: "Soft" ou "Hard"
        self.descricao = descricao

    def __str__(self):
        return f"{self.nome} ({self.tipo}): {self.descricao}"

class Carreira:
    """Representa uma área profissional ou trilha de aprendizado recomendada."""
    def __init__(self, nome: str, descricao: str, competencias_chave: list):
        self.nome = nome
        self.descricao = descricao
        # Lista de nomes de Competencias que são cruciais para esta carreira
        self.competencias_chave = competencias_chave

    def __str__(self):
        return f"Carreira: {self.nome}\nDescrição: {self.descricao}\nCompetências Chave: {', '.join(self.competencias_chave)}"

class Perfil:
    """Representa o perfil do usuário, armazenando suas competências avaliadas."""
    def __init__(self, nome: str):
        self.nome = nome
        # Dicionário onde a chave é o nome da Competencia e o valor é a pontuação (1 a 5)
        self.competencias = {}

    def adicionar_competencia(self, nome_competencia: str, pontuacao: int):
        """Adiciona ou atualiza a pontuação de uma competência no perfil."""
        if 1 <= pontuacao <= 5:
            self.competencias[nome_competencia] = pontuacao
        else:
            raise ValueError("A pontuação deve ser entre 1 e 5.")

    def __str__(self):
        competencias_str = "\n".join([f"- {nome}: {pontuacao}" for nome, pontuacao in self.competencias.items()])
        return f"Perfil: {self.nome}\nCompetências Avaliadas:\n{competencias_str}"

