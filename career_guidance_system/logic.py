from models import Perfil, Carreira
from data import CARREIRAS, COMPETENCIAS

def gerar_recomendacao(perfil: Perfil) -> dict:
    """
    Gera recomendações de carreira e aprimoramento para um Perfil.

    A lógica de recomendação é baseada em um sistema de pontuação ponderada.
    Para cada Carreira, o Score de Adequação é calculado somando as pontuações
    do usuário nas Competências-Chave daquela Carreira.
    """
    
    # 1. Calcular o Score de Adequação para cada Carreira
    scores_carreiras = {}
    for carreira in CARREIRAS:
        score = 0
        competencias_faltantes = []
        
        for comp_nome in carreira.competencias_chave:
            # Verifica se a competência chave está no perfil do usuário
            if comp_nome in perfil.competencias:
                pontuacao = perfil.competencias[comp_nome]
                # A pontuação é o peso da competência para a carreira
                score += pontuacao
            else:
                # Se a competência chave não foi avaliada, é considerada faltante
                competencias_faltantes.append(comp_nome)

        scores_carreiras[carreira.nome] = {
            "score": score,
            "carreira": carreira,
            "competencias_faltantes": competencias_faltantes
        }

    # 2. Ordenar as carreiras pelo Score de Adequação (do maior para o menor)
    recomendacoes_ordenadas = sorted(
        scores_carreiras.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    # 3. Gerar recomendações de Aprimoramento
    # Identifica as competências com baixa pontuação (<= 2)
    recomendacoes_aprimoramento = []
    for comp_nome, pontuacao in perfil.competencias.items():
        if pontuacao <= 2:
            comp_obj = COMPETENCIAS.get(comp_nome)
            if comp_obj:
                recomendacoes_aprimoramento.append({
                    "competencia": comp_nome,
                    "pontuacao": pontuacao,
                    "tipo": comp_obj.tipo,
                    "sugestao": f"Aprimorar {comp_obj.nome} ({comp_obj.tipo}). Sugestão: Buscar cursos e projetos práticos sobre {comp_obj.nome}."
                })

    return {
        "carreiras_recomendadas": recomendacoes_ordenadas,
        "aprimoramento_sugerido": recomendacoes_aprimoramento
    }

def formatar_recomendacao(resultado: dict) -> str:
    """Formata o resultado da recomendação para exibição amigável."""
    output = "\n" + "="*50 + "\n"
    output += "RELATÓRIO DE ORIENTAÇÃO DE CARREIRA\n"
    output += "="*50 + "\n"

    # 1. Carreiras Recomendadas
    output += "1. CARREIRAS MAIS ADEQUADAS:\n"
    for i, item in enumerate(resultado["carreiras_recomendadas"][:3]): # Top 3
        carreira = item["carreira"]
        score = item["score"]
        
        # O score máximo é 5 (pontuação máxima) * 3 (competências chave) = 15
        output += f"\n{i+1}. {carreira.nome} (Score de Adequação: {score}/15)\n"
        output += f"   Descrição: {carreira.descricao}\n"
        output += f"   Competências Chave: {', '.join(carreira.competencias_chave)}\n"
        
        if item["competencias_faltantes"]:
            output += f"   *Atenção: Competências Chave não avaliadas: {', '.join(item['competencias_faltantes'])}*\n"

    # 2. Aprimoramento Sugerido
    output += "\n" + "-"*50 + "\n"
    output += "2. TRILHAS DE APRIMORAMENTO SUGERIDAS:\n"
    if resultado["aprimoramento_sugerido"]:
        for item in resultado["aprimoramento_sugerido"]:
            output += f"\n- {item['competencia']} (Pontuação: {item['pontuacao']}/5)\n"
            output += f"  {item['sugestao']}\n"
    else:
        output += "\nNenhuma competência com baixa pontuação identificada. Continue aprimorando!\n"

    output += "\n" + "="*50 + "\n"
    return output

# Exemplo de uso (para testes)
if __name__ == "__main__":
    # Cria um perfil de exemplo
    perfil_exemplo = Perfil("Exemplo Dev Ops")
    perfil_exemplo.adicionar_competencia("Lógica de Programação", 5)
    perfil_exemplo.adicionar_competencia("Cloud Computing", 4)
    perfil_exemplo.adicionar_competencia("Pensamento Analítico", 3)
    perfil_exemplo.adicionar_competencia("Cibersegurança", 2) # Baixa pontuação para aprimoramento
    perfil_exemplo.adicionar_competencia("Criatividade e Inovação", 1) # Baixa pontuação para aprimoramento
    
    # Gera a recomendação
    resultado = gerar_recomendacao(perfil_exemplo)
    
    # Exibe o resultado formatado
    print(formatar_recomendacao(resultado))
