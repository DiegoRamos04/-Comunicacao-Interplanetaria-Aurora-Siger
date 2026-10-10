import json
import heapq
from pathlib import Path

# Configuração do caminho do JSON
BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = BASE_DIR / "data" / "dados_aurora_siger.json"

def gerenciar_alertas(dados_customizados=None):
    print("\n" + "=" * 80)
    print("      SISTEMA DE PRIORIZAÇÃO DE ALERTAS ")
    print("=" * 80)

    # Se recebeu os dados simulados da memória, usa eles. Se não, lê o arquivo normal.
    if dados_customizados:
        dados = dados_customizados
    else:
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
                dados = json.load(file)
        except FileNotFoundError:
            print("Erro: Arquivo JSON não encontrado.")
            return

    fila_alertas = [] 

    print("\n[1] Varrendo módulos e calculando erros (Erro Absoluto e Relativo)...")
    
    for nome, info in dados['modulos'].items():
        prevista = info['latencia_estimada_ms']
        observada = info['latencia_observada_ms']
        prioridade = info['prioridade_operacional']
        
        erro_absoluto = abs(observada - prevista)
        erro_relativo = (erro_absoluto / prevista) * 100
        
        if erro_relativo > 50 or info['status_operacional'] == 'Alerta' or "Invasão" in info['status_operacional']:
            tupla_alerta = (prioridade, -erro_relativo, nome, erro_absoluto)
            heapq.heappush(fila_alertas, tupla_alerta)
            print(f"  -> {nome} (Erro Relativo: {erro_relativo:.2f}%) adicionado ao Heap.")

    print("\n[2] Processando a Fila de Prioridade (Heap)...")
    print("A vantagem do Heap é retirar o item mais urgente em tempo O(log n),")
    print("sem precisar reordenar toda a lista a cada remoção.\n")

    ordem = 1
    while fila_alertas:
        alerta_critico = heapq.heappop(fila_alertas)
        
        prioridade_alerta = alerta_critico[0]
        erro_rel_alerta = abs(alerta_critico[1]) 
        nome_modulo = alerta_critico[2]
        erro_abs_alerta = alerta_critico[3]

        print(f"{ordem}º ATENDIMENTO URGENTE:")
        print(f"   Módulo:     {nome_modulo}")
        print(f"   Prioridade: Nível {prioridade_alerta}")
        print(f"   Erro Abs.:  {erro_abs_alerta} ms de atraso na rede")
        print(f"   Erro Rel.:  {erro_rel_alerta:.2f}% de anomalia")
        
        # ADMS, FLISR e Microrredes
        if prioridade_alerta == 1 or erro_rel_alerta > 100:
            print("   [ADMS] Ação Automática: Isolando falha (FLISR).")
            print("   [ADMS] Comutando microrrede para 'Operação Ilhada' para garantir estabilidade local.\n")
        else:
            print("   [ADMS] Ação Automática: Ajustando fluxo via inversores inteligentes e manutenção preditiva.\n")
            
        ordem += 1

    print("=" * 80)

if __name__ == "__main__":
    gerenciar_alertas()