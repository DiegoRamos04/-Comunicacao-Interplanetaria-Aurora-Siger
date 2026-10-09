# Comunicação Interplanetária - Aurora SIGER

## Sobre o Projeto
Projeto acadêmico da FIAP: Análise exploratória, estruturação e defesa de dados do Núcleo Cognitivo da colônia espacial Aurora Siger. O sistema foi implementado em Python utilizando Pandas para processamento de métricas operacionais, elétricas e de comunicação a partir de bases JSON. 

O projeto também integra conceitos de estruturas de dados avançadas para buscas e alertas, além de fundamentação teórica sobre microrredes de energia e automação.

## Funcionalidades
* **Processamento de Dados:** Leitura e manipulação estruturada das bases de dados operacionais utilizando Pandas.
* **Buscas Otimizadas:** Implementação de árvores Trie (`trie_buscas.py`) para indexação e recuperação rápida de registros da colônia.
* **Sistema de Alertas:** Utilização de estruturas de Heap (`alertas_heap.py`) para classificar e escalonar anomalias na infraestrutura elétrica com base na gravidade.
* **Avaliação e Métricas:** Validação do desempenho dos algoritmos e da precisão do processamento de dados (`avaliacao_modelo.py`).
* **Visualização de Anomalias:** Geração de análises visuais do comportamento da rede elétrica.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, JSON
* **Estruturas de Dados:** Tries, Min/Max Heaps

## Estrutura do Projeto

```text
📁 -Comunicacao-Interplanetaria-Aurora-Siger/
│
├── 📄 codigo_fonte.py             # Script principal de orquestração do sistema
├── 📄 README.md                   # Documentação do projeto
├── 📄 .gitignore                  # Arquivos ignorados pelo Git
│
├── 📁 data/                       # Bases de dados da colônia
│   ├── 📄 dados_aurora_siger.json     
│   └── 📄 registros_colonia.txt       
│
├── 📁 src/                        # Código-fonte e módulos auxiliares
│   ├── 📄 alertas_heap.py         # Lógica de priorização de alertas (Heap)
│   ├── 📄 avaliacao_modelo.py     # Scripts de validação e testes
│   ├── 📄 modulos.py              # Funções modulares de apoio
│   ├── 📄 registros.py            # Manipulação de logs e registros
│   └── 📄 trie_buscas.py          # Lógica de busca otimizada (Trie)
│
├── 📁 graficos_ou_imagens/        # Visualizações de dados e outputs
│   └── 🖼️ grafico_anomalia_rede.png 
│
└── 📁 docs/                       # Documentações e fundamentação teórica
```

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/DiegoRamos04/-Comunicacao-Interplanetaria-Aurora-Siger.git](https://github.com/DiegoRamos04/-Comunicacao-Interplanetaria-Aurora-Siger.git)
   ```

2. **Acesse o Diretório:**
   ```bash
   cd -Comunicacao-Interplanetaria-Aurora-Siger
   ```

3. **Crie e ative um ambiente virtual (opcional, porém recomendado):**
   ```bash 
   python -m venv venv
   ```
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências necessárias:**
   ```bash
   pip install pandas matplotlib
   ```

5. **Execute o programa principal:**
   ```bash
   python codigo_fonte.py
   ```