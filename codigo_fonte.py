import sys
import random
import json
import os
import copy
from pathlib import Path


from src.modulos import consultar_modulos, consultar_modulo_especifico
from src.registros import cadastrar_registro, consultar_registros
from src.avaliacao_modelo import avaliar_modelo_latencia
from src.alertas_heap import gerenciar_alertas
from src.trie_buscas import executar_busca_trie
from src.dinamica_rede import simular_evolucao_latencia

BASE_DIR = Path(__file__).resolve().parent
ARQUIVO_JSON = BASE_DIR / "data" / "dados_aurora_siger.json"

def simular_ataque_aleatorio():
    """Simula um ataque aleatório apenas na memória RAM, preservando o arquivo original."""
    print("\n" + "=" * 80)
    print("  [ALERTA SISTÊMICO] SIMULAÇÃO DE CIBERATAQUE NO NÚCLEO COGNITIVO INICIADA")
    print("=" * 80)

    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
            dados = json.load(file)
    except FileNotFoundError:
        print(f"Erro: Banco de dados '{ARQUIVO_JSON.name}' não encontrado.")
        return

    # Cria uma cópia isolada na memória (RAM) para o ataque não afetar o disco
    dados_simulacao = copy.deepcopy(dados)

    modulos_disponiveis = list(dados_simulacao['modulos'].keys())
    alvo = random.choice(modulos_disponiveis)

    # Modifica apenas a cópia em memória
    dados_simulacao['modulos'][alvo]['latencia_observada_ms'] = random.randint(300, 999)
    dados_simulacao['modulos'][alvo]['status_operacional'] = "Alerta - Invasão Detectada"

    print(f"\n[CRÍTICO] O módulo '{alvo.upper()}' foi comprometido na simulação!")
    print(f"Latência disparou para {dados_simulacao['modulos'][alvo]['latencia_observada_ms']} ms.")
    print("Encaminhando dados simulados para o Sistema de Priorização (Heap)...\n")
    
    # Passa os dados em memória diretamente para o Heap
    gerenciar_alertas(dados_customizados=dados_simulacao)
    print("\nSimulação concluída com sucesso. (O arquivo original permaneceu intacto no disco).")

def exibir_menu():
    while True:
        # Limpa o terminal para o menu ficar sempre organizado
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n" + "=" * 60)
        print("  SISTEMA DE COMUNICAÇÃO INTERPLANETÁRIA (SCIC) - AURORA SIGER  ")
        print("=" * 60)
        print("1. Consultar Painel de Módulos (Pandas)")
        print("2. Consultar Módulo Específico (Lei de Ohm)")
        print("3. Cadastrar Registro Manual")
        print("4. Consultar Histórico de Registros")
        print("5. Avaliar Performance da IA (scikit-learn: MAE, RMSE, R²)")
        print("6. Processar Alertas Críticos (Fila de Prioridade / Heap)")
        print("7. Busca Ultrarrápida de Módulos (Árvore Trie & Conv. Bases)")
        print("8. [SIMULAÇÃO] Lançar Ataque Aleatório na Rede")
        print("9. Simular Evolução Dinâmica da Rede (EDO & SciPy solve_ivp)")
        print("0. Encerrar Sistema")
        print("=" * 60)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            consultar_modulos()
        elif opcao == '2':
            consultar_modulo_especifico()
        elif opcao == '3':
            cadastrar_registro()
        elif opcao == '4':
            consultar_registros()
        elif opcao == '5':
            avaliar_modelo_latencia()
        elif opcao == '6':
            gerenciar_alertas()
        elif opcao == '7':
            executar_busca_trie()
        elif opcao == '8':
            simular_ataque_aleatorio()
        elif opcao == '9':
            simular_evolucao_latencia()
        elif opcao == '0':
            print("\nEncerrando comunicação com a Colônia Aurora Siger. Até logo!")
            sys.exit()
        else:
            print("\nOpção inválida. Tente novamente.")

        
        if opcao != '0':
            input("\n[Pressione ENTER para voltar ao menu principal...]")

if __name__ == "__main__":
    exibir_menu()