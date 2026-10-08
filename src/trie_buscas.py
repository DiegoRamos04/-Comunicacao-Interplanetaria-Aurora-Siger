import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = BASE_DIR / "data" / "dados_aurora_siger.json"


# ETAPA 1.5: ESTRUTURAS DA ÁRVORE TRIE

class NodoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_de_palavra = False
        self.dados_modulo = None  # Guarda as informações do módulo aqui

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def inserir(self, palavra, dados):
        """Insere uma palavra (nome do módulo) letra por letra na árvore"""
        nodo_atual = self.raiz
        # Salva tudo em minúsculo para facilitar a busca depois
        for letra in palavra.lower():
            if letra not in nodo_atual.filhos:
                nodo_atual.filhos[letra] = NodoTrie()
            nodo_atual = nodo_atual.filhos[letra]
        
        nodo_atual.fim_de_palavra = True
        nodo_atual.dados_modulo = dados

    def buscar_por_prefixo(self, prefixo):
        """Busca todas as palavras que começam com o prefixo digitado"""
        nodo_atual = self.raiz
        for letra in prefixo.lower():
            if letra not in nodo_atual.filhos:
                return [] # Prefixo não encontrado
            nodo_atual = nodo_atual.filhos[letra]
        
        # Se achou o prefixo, coleta todos os nós filhos que formam palavras
        return self._coletar_palavras(nodo_atual, prefixo.lower())

    def _coletar_palavras(self, nodo, prefixo_atual):
        resultados = []
        if nodo.fim_de_palavra:
            resultados.append((prefixo_atual, nodo.dados_modulo))
        
        for letra, nodo_filho in nodo.filhos.items():
            resultados.extend(self._coletar_palavras(nodo_filho, prefixo_atual + letra))
        
        return resultados


# Etapa 1.6: Conversão de bases e exibição

def executar_busca_trie():
    print("\n" + "=" * 80)
    print("      SISTEMA DE BUSCA RÁPIDA (TRIE) E CONVERSÃO DE BASES ")
    print("=" * 80)

    # 1. Carregar Dados
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
            dados = json.load(file)
    except FileNotFoundError:
        print("Erro: Arquivo JSON não encontrado.")
        return

    # 2. Inicializar a Árvore Trie e popular com os dados
    arvore_busca = Trie()
    for nome_modulo, info in dados['modulos'].items():
        arvore_busca.inserir(nome_modulo, info)

    # 3. Interação com o usuário
    print("A estrutura Trie permite buscas ultrarrápidas por prefixo (Ex: 'com', 'agri').")
    prefixo = input("Digite o início do nome do módulo que deseja buscar: ").strip()

    resultados = arvore_busca.buscar_por_prefixo(prefixo)

    if not resultados:
        print(f"\n[!] Nenhum módulo encontrado com o prefixo '{prefixo}'.")
        return

    print(f"\nForam encontrados {len(resultados)} módulo(s) com o prefixo '{prefixo}':\n")

    # 4. Exibir resultados e aplicar a Etapa 1.6 (Bases Numéricas)
    for nome_encontrado, info in resultados:
        nome_original = nome_encontrado.title() # Deixa a primeira letra maiúscula
        codigo = info['codigo_dispositivo']
        potencia = int(info['potencia_aproximada_w'])
        
        print("-" * 50)
        print(f"MÓDULO ENCONTRADO: {nome_original} ({codigo})")
        print(f"Status atual:      {info['status_operacional']}")
        print(f"Latência atual:    {info['latencia_observada_ms']} ms")
        
        # Etapa 1.6: Eletricidade básica aplicada à computação (Conversões)
        print("\n--- CONVERSÃO DE BASES NUMÉRICAS (ETAPA 1.6) ---")
        print("Convertendo a Potência Aproximada para os processadores dos sensores:")
        print(f"Decimal (Humano):      {potencia} W")
        # A função bin() retorna algo como '0b1010'. Usamos [2:] para tirar o '0b' e deixar só os números.
        print(f"Binário (Máquina):     {bin(potencia)[2:]} W")
        # A função hex() retorna '0x...'. Usamos [2:] e .upper() para ficar no formato clássico (Ex: 1388 -> 1388)
        print(f"Hexadecimal (Sensor):  {hex(potencia)[2:].upper()} W")
        print("-" * 50)

if __name__ == "__main__":
    executar_busca_trie()