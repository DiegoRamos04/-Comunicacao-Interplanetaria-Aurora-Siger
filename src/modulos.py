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
    # Cálculo de potência (Lei de Ohm: P = V * I)
    tensao = info['tensao_v']
    corrente = info['corrente_a']
    potencia_calculada = tensao * corrente

    print("MÉTRICAS ELÉTRICAS (LEI DE OHM):")
    print(f"Tensão:                 {tensao} V")
    print(f"Corrente:               {corrente} A")
    print(f"Pot. Aprox. (Catálogo): {info['potencia_aproximada_w']} W")
    print(f"Pot. Real Calculada:    {potencia_calculada:.2f} W")
    print("-" * 60)
    print("MÉTRICAS DE COMUNICAÇÃO E REDE:")
    print(f"Necessidade:            {info['necessidade_comunicacao']}")
    print(f"Latência Estimada:      {info['latencia_estimada_ms']} ms")
    print(f"Latência Observada:     {info['latencia_observada_ms']} ms")
    # Estabilidade com Banco de Capacitores em Paralelo
    print("-" * 60)
    print("ESTABILIDADE DA REDE (CAPÍTULO 11 - CAPACITORES):")
    print("Prevenção contra oscilações (micro-interrupções e picos de demanda).")
    
    # Simulação de 3 capacitores comerciais de 4700 µF associados em paralelo
    c1 = c2 = c3 = 4700e-6 
    c_eq = c1 + c2 + c3  # Ceq = C1 + C2 + C3
    
    # Cálculo da carga (Q = C * V) e da Energia armazenada (En = 1/2 * Q * V)
    carga_total = c_eq * tensao
    energia_armazenada = 0.5 * carga_total * tensao
    
    print(f"Banco de Proteção:      3x capacitores de 4700 µF (Paralelo)")
    print(f"Capacitância Equiv.:    {c_eq * 1e6:.2f} µF")
    print(f"Carga Acumulada (Q):    {carga_total:.4f} C")
    print(f"Energia de Backup (En): {energia_armazenada:.2f} J")
    
    print("\nConexões:")
    for destino, distancia in info["conexoes"]:
        print(f"  → {destino}: peso/distância {distancia}")
    print("=" * 60)

