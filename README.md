# Comunicação Interplanetária - Aurora SIGER

## Sobre o Projeto
Projeto acadêmico da FIAP: Análise exploratória, estruturação e defesa de dados do Núcleo Cognitivo da colônia espacial Aurora Siger. O sistema foi implementado em Python utilizando Pandas para processamento de métricas operacionais, elétricas e de comunicação a partir de bases JSON. 

O projeto também integra conceitos de estruturas de dados avançadas para buscas e alertas, além de fundamentação teórica sobre microrredes de energia e automação.

## Funcionalidades
* **Processamento de Dados:** Leitura e manipulação estruturada das bases de dados operacionais utilizando Pandas.
* **Buscas Otimizadas:** Implementação de árvores Trie (`trie_buscas.py`) para indexação e recuperação rápida de registros da colônia.
* **Sistema de Alertas:** Utiliza de estruturas de Heap (`alertas_heap.py`) para classificar e escalonar anomalias na infraestrutura elétrica com base na gravidade.
* **Avaliação e Métricas:** Validação do desempenho dos algoritmos e da precisão do processamento de dados (`avaliacao_modelo.py`).
* **Visualização de Anomalias:** Geração de análises visuais do comportamento da rede elétrica.
- **Simulação Dinâmica (EDO):** Modelagem da evolução temporal e estabilização de enlaces de comunicação utilizando Equações Diferenciais Ordinárias resolvidas numericamente via `scipy.integrate.solve_ivp` (`dinamica_rede.py`).
- **Assistente Virtual e Automação de Fluxos:** Simulação de um agente inteligente para intermediar a comunicação em linguagem natural entre humanos e o sistema SCIC.

## Tecnologias e Dependências Utilizadas

* **Linguagem:** Python
* **Manipulação de Dados:** `pandas` (necessária para leitura, limpeza e organização tabular dos dados operacionais da colônia) e JSON.
* **Estruturas de Dados:** Tries (para busca ultrarrápida por prefixos) e Min/Max Heaps (para filas de prioridade e escalonamento de alertas).
* **Visualização:** `matplotlib` (utilizada para a plotagem gráfica e visualização diagnóstica das anomalias de rede).
* **Machine Learning e Simulação Numérica:** 
  * `scikit-learn`: Implementação do modelo preditivo e cálculo das métricas de performance (MAE, MSE, RMSE e R²).
  * `scipy`: Necessária para resolver a Equação Diferencial (EDO) da rede usando a função solve_ivp.
  * `statsmodels`: Utilizada para a avaliação estrutural do modelo e extração dos Critérios de Akaike (AIC) e Bayesiano (BIC).

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
├── 📁 docs/                       # Documentações e fundamentação teórica
│   ├── 📄 relatorio_tecnico.pdf   # Relatório com a explicação técnica e reflexão social
│   └── 📄 link_video.txt          # Link para o vídeo de apresentação no YouTube
│
├── 📁 graficos_ou_imagens/        # Visualizações de dados e outputs
│   ├── 🖼️ grafico_anomalia_rede.png 
│   └── 🖼️ grafico_dinamica_rede.png
└── 📁 src/                        # Código-fonte e módulos auxiliares
    ├── 📄 alertas_heap.py         # Lógica de priorização de alertas (Heap)
    ├── 📄 avaliacao_modelo.py     # Scripts de validação e testes
    ├── 📄 dinamica_rede.py        # Simulação EDO e recuperação de rede (SciPy)
    ├── 📄 modulos.py              # Funções modulares de apoio (Pandas e Lei de Ohm)
    ├── 📄 registros.py            # Manipulação de logs e registros manuais
    └── 📄 trie_buscas.py          # Lógica de busca otimizada e conversão (Trie)
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
   pip install pandas matplotlib scikit-learn scipy statsmodels
   ```

5. **Execute o programa principal:**
   ```bash
   python codigo_fonte.py
   ```
