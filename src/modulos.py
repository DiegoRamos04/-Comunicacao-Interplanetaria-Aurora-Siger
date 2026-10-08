import json
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_DATA = BASE_DIR / "data"
ARQUIVO_JSON = PASTA_DATA / "dados_aurora_siger.json"

def carregar_dados():
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: Arquivo {ARQUIVO_JSON.name} não encontrado na pasta data.")
        return None

def salvar_dados(dados):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def consultar_modulos():
    print("\n" + "=" * 100)
    print("           STATUS DOS MÓDULOS DA COLÔNIA AURORA SIGER (ANÁLISE PANDAS)")
    print("=" * 100)

    dados = carregar_dados()
    if not dados or "modulos" not in dados:
        return 

    df = pd.DataFrame.from_dict(dados['modulos'], orient='index')

    df_exibicao = df[[
        'codigo_dispositivo', 'status_operacional', 'tensao_v', 
        'potencia_aproximada_w', 'latencia_estimada_ms', 'latencia_observada_ms'
    ]]

    df_exibicao.columns = [
        'Código', 'Status', 'Tensão(V)', 'Potência(W)', 
        'Lat. Estimada(ms)', 'Lat. Observada(ms)'
    ]

    print(df_exibicao.to_string())
    print("=" * 100)

def consultar_modulo_especifico():
    dados = carregar_dados()
    if not dados or "modulos" not in dados:
        return 
        
    modulos = dados.get("modulos", {})

    print("\nMódulos disponíveis:")
    for nome in modulos:
        print(f"- {nome}")

    nome_digitado = input("\nDigite o nome do módulo: ").strip().lower()
    
    # Sistema de busca que ignora letras maiúsculas ou minúsculas
    chave_correta = None
    for chave in modulos.keys():
        if chave.lower() == nome_digitado:
            chave_correta = chave
            break

    if not chave_correta:
        print("\n[!] Módulo não encontrado. Verifique a ortografia e tente novamente.")
        return
        
    info = modulos[chave_correta]
    nome_oficial = chave_correta

    print("\n" + "=" * 60)
    print(f"              {nome_oficial.upper()} ({info['codigo_dispositivo']})")
    print("=" * 60)
    print(f"Status:                 {info['status_operacional']}")
    print(f"Prioridade operacional: {info['prioridade_operacional']}")
    print(f"Consumo diário:         {info['consumo_energetico_kwh']} kWh")
    print("-" * 60)
    print("MÉTRICAS ELÉTRICAS (LEI DE OHM):")
    print(f"Tensão:                 {info['tensao_v']} V")
    print(f"Corrente:               {info['corrente_a']} A")
    print(f"Potência Aproximada:    {info['potencia_aproximada_w']} W")
    print("-" * 60)
    print("MÉTRICAS DE COMUNICAÇÃO E REDE:")
    print(f"Necessidade:            {info['necessidade_comunicacao']}")
    print(f"Latência Estimada:      {info['latencia_estimada_ms']} ms")
    print(f"Latência Observada:     {info['latencia_observada_ms']} ms")
    
    print("\nConexões:")
    for destino, distancia in info["conexoes"]:
        print(f"  → {destino}: peso/distância {distancia}")
    print("=" * 60)

