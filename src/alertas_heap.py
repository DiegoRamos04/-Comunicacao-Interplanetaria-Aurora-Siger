import json
import heapq
from pathlib import Path

# Configuração do caminho do JSON
BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = BASE_DIR / "data" / "dados_colonia.json"

def gerenciar_alertas():
    print("\n" + "=" * 80)
    print("      SISTEMA DE PRIORIZAÇÃO DE ALERTAS (ETAPAS 1.2 E 1.4 - HEAP)")
    print("=" * 80)

    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
            dados = json.load(file)
    except FileNotFoundError:
        print("Erro: Arquivo JSON não encontrado.")
        return

    fila_alertas = [] # Nossa estrutura Heap

    print("\n[1] Varrendo módulos e calculando erros (Erro Absoluto e Relativo)...")
    
    for nome, info in dados['modulos'].items():
        prevista = info['latencia_estimada_ms']
        observada = info['latencia_observada_ms']
        prioridade = info['prioridade_operacional']
        
        # ETAPA 1.2: Cálculo de Erro Absoluto e Erro Relativo
        erro_absoluto = abs(observada - prevista)
        erro_relativo = (erro_absoluto / prevista) * 100
        
        # Regra do Alerta: Se o erro relativo passar de 50% ou o status for 'Alerta'
        if erro_relativo > 50 or info['status_operacional'] == 'Alerta':
            
            # Como o Python usa Min-Heap (menor valor no topo), a prioridade 1 fica acima da 3.
            # Usamos o erro relativo negativo (-erro_relativo) para que o MAIOR erro desempate.
            tupla_alerta = (prioridade, -erro_relativo, nome, erro_absoluto)
            
            # Adiciona na fila mantendo a estrutura de árvore Heap perfeita
            heapq.heappush(fila_alertas, tupla_alerta)
            print(f"  -> {nome} (Erro Relativo: {erro_relativo:.2f}%) adicionado ao Heap.")

    print("\n[2] Processando a Fila de Prioridade (Heap)...")
    print("A vantagem do Heap é retirar o item mais urgente em tempo O(log n),")
    print("sem precisar reordenar toda a lista a cada remoção.\n")

    # ETAPA 1.4: Extraindo do Heap pela ordem de urgência
    ordem = 1
    while fila_alertas:
        # heappop remove e retorna sempre o alerta mais crítico
        alerta_critico = heapq.heappop(fila_alertas)
        
        prioridade_alerta = alerta_critico[0]
        erro_rel_alerta = abs(alerta_critico[1]) # Tira o sinal negativo que usamos pro Heap
        nome_modulo = alerta_critico[2]
        erro_abs_alerta = alerta_critico[3]

        print(f"{ordem}º ATENDIMENTO URGENTE:")
        print(f"   Módulo:     {nome_modulo}")
        print(f"   Prioridade: Nível {prioridade_alerta}")
        print(f"   Erro Abs.:  {erro_abs_alerta} ms de atraso na rede")
        print(f"   Erro Rel.:  {erro_rel_alerta:.2f}% de anomalia\n")
        ordem += 1

    print("=" * 80)

if __name__ == "__main__":
    gerenciar_alertas()