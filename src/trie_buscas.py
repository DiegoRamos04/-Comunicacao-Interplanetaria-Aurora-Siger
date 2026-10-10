import json
from pathlib import Path

# Algoritmos de conversão numérica 
def decimal_para_binario(n):
    if n == 0: return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    return binario

def decimal_para_hexadecimal(n):
    hex_chars = "0123456789ABCDEF"
    if n == 0: return "0"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n = n // 16
    return hexadecimal

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = BASE_DIR / "data" / "dados_aurora_siger.json"


# Estruturas da Árvore Trie

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


# Conversão de bases e exibição

def executar_busca_trie():
    print("\n" + "=" * 80)
    print("      SISTEMA DE BUSCA RÁPIDA (TRIE) E CONVERSÃO DE BASES ")
    print("=" * 80)

    # Carregar Dados
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
            dados = json.load(file)
    except FileNotFoundError:
        print("Erro: Arquivo JSON não encontrado.")
        return

    # Inicializar a Árvore Trie e popular com os dados
    arvore_busca = Trie()
    for nome_modulo, info in dados['modulos'].items():
        arvore_busca.inserir(nome_modulo, info)

    # Interação com o usuário
    print("A estrutura Trie permite buscas ultrarrápidas por prefixo (Ex: 'com', 'agri').")
    prefixo = input("Digite o início do nome do módulo que deseja buscar: ").strip()

    resultados = arvore_busca.buscar_por_prefixo(prefixo)

    if not resultados:
        print(f"\n[!] Nenhum módulo encontrado com o prefixo '{prefixo}'.")
        return

    print(f"\nForam encontrados {len(resultados)} módulo(s) com o prefixo '{prefixo}':\n")

    # Exibir resultados 
    for nome_encontrado, info in resultados:
        nome_original = nome_encontrado.title() # Deixa a primeira letra maiúscula
        codigo = info['codigo_dispositivo']
        potencia = int(info['potencia_aproximada_w'])
        
        print("-" * 50)
        print(f"MÓDULO ENCONTRADO: {nome_original} ({codigo})")
        print(f"Status atual:      {info['status_operacional']}")
        print(f"Latência atual:    {info['latencia_observada_ms']} ms")
        
       # Conversões com algoritmo de divisão 
        binario_manual = decimal_para_binario(potencia)
        hexa_manual = decimal_para_hexadecimal(potencia)

        print("\n--- CONVERSÃO DE BASES NUMÉRICAS ---")
        print("Convertendo a Potência via Método da Divisão Sucessiva:")
        print(f"Decimal (Humano):      {potencia} W")
        print(f"Binário (Máquina):     {binario_manual} W")
        print(f"Hexadecimal (Sensor):  {hexa_manual} W")
        print("-" * 50)

if __name__ == "__main__":
    executar_busca_trie()