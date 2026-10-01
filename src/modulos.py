import json
import pandas as pd
from pathlib import Path

from .historico import registrar_historico
# Se quiser, pode remover a importação de 'tabela.py' neste arquivo, 
# pois o Pandas fará a formatação da tabela automaticamente.

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_DATA = BASE_DIR / "data"
ARQUIVO_JSON = PASTA_DATA / "dados_colonia.json"

def carregar_dados():
    """Carrega os dados JSON (Requisito 1.2: Ler registros e JSON)"""
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: Arquivo {ARQUIVO_JSON} não encontrado.")
        return None

def salvar_dados(dados):
    """Salva modificações de volta no arquivo JSON (Requisito 1.2: Salvar dados JSON)"""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def consultar_modulos():
    """Usa PANDAS para ler, organizar e exibir os dados (Requisito 1.1 e 1.2)"""
    print("\n" + "=" * 100)
    print("           STATUS DOS MÓDULOS DA COLÔNIA AURORA SIGER (ANÁLISE PANDAS)")
    print("=" * 100)

    dados = carregar_dados()
    if not dados or "modulos" not in dados:
        print("Nenhum módulo cadastrado ou erro na base de dados.")
        return

    # Converte o dicionário de módulos em um DataFrame do Pandas
    # orient='index' usa o nome do módulo (ex: 'Habitação') como índice da linha
    df = pd.DataFrame.from_dict(dados['modulos'], orient='index')

    # Seleciona as colunas mais importantes para mostrar na tabela geral
    df_exibicao = df[[
        'codigo_dispositivo', 'status_operacional', 'tensao_v', 
        'potencia_w', 'latencia_estimada_ms', 'latencia_observada_ms'
    ]]

    # Renomeia as colunas para a exibição ficar mais legível no terminal
    df_exibicao.columns = [
        'Código', 'Status', 'Tensão(V)', 'Potência(W)', 
        'Lat. Estimada(ms)', 'Lat. Observada(ms)'
    ]

    # Exibe a tabela formatada pelo próprio Pandas
    print(df_exibicao.to_string())
    print("=" * 100)

    registrar_historico(
        "Consulta de módulos",
        "Sistema",
        "Consulta geral dos módulos utilizando Pandas",
    )

def consultar_modulo_especifico():
    """Consulta detalhada de um módulo, mostrando todas as novas chaves elétricas"""
    dados = carregar_dados()
    modulos = dados.get("modulos", {})

    print("\nMódulos disponíveis:")
    for nome in modulos:
        print(f"- {nome}")

    nome = input("\nDigite o nome do módulo: ").strip()
    info = modulos.get(nome)

    if info is None:
        print("Módulo não encontrado.")
        return

    print("\n" + "=" * 60)
    print(f"              {nome.upper()} ({info['codigo_dispositivo']})")
    print("=" * 60)
    print(f"Status:                 {info['status_operacional']}")
    print(f"Prioridade operacional: {info['prioridade_operacional']}")
    print(f"Consumo diário:         {info['consumo_energetico_kwh']} kWh")
    print("-" * 60)
    print("MÉTRICAS ELÉTRICAS (LEI DE OHM):")
    print(f"Tensão:                 {info['tensao_v']} V")
    print(f"Corrente:               {info['corrente_a']} A")
    print(f"Potência Aproximada:    {info['potencia_w']} W")
    print("-" * 60)
    print("MÉTRICAS DE COMUNICAÇÃO E REDE:")
    print(f"Necessidade:            {info['necessidade_comunicacao']}")
    print(f"Latência Estimada:      {info['latencia_estimada_ms']} ms")
    print(f"Latência Observada:     {info['latencia_observada_ms']} ms")
    
    print("\nConexões:")
    for destino, distancia in info["conexoes"]:
        print(f"  → {destino}: peso/distância {distancia}")

    print("=" * 60)

    registrar_historico(
        "Consulta de módulo",
        nome,
        f"Consulta detalhada do módulo {nome}",
    )