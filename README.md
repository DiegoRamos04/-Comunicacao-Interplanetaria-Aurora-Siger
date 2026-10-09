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
- **Simulação Dinâmica (EDO):** Modelagem da evolução temporal e estabilização de enlaces de comunicação utilizando Equações Diferenciais Ordinárias resolvidas numericamente via `scipy.integrate.solve_ivp` (`dinamica_rede.py`).

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
## Análise de Complexidade (Fundamentação Teórica)
Para garantir que o SCIC opere com eficiência em cenários de alta criticidade na colônia Aurora Siger, o projeto aplica conceitos de análise assintótica de algoritmos:

- **Buscas Otimizadas (Trie):** As operações de inserção e recuperação por prefixo possuem complexidade de tempo **O(m)** (onde *m* é o tamanho do prefixo), superando a busca linear tradicional.
- **Fila de Prioridade (Heap):** O escalonamento de alertas críticos utiliza operações logarítmicas **O(log n)** para inserção e remoção de prioridades.
- **Trade-off Espaço-Tempo:** O isolamento de falhas na simulação utiliza cópias estruturais em memória RAM, priorizando a segurança dos dados persistidos em detrimento de um consumo controlado de espaço auxiliar.

## 🔬 Fundamentação Teórica e Métodos Numéricos

Para garantir a precisão, a estabilidade e a confiabilidade nas transmissões críticas da colônia Aurora Siger, o SCIC incorpora os seguintes fundamentos matemáticos e computacionais estudados no projeto:

- **Aritmética de Ponto Flutuante (IEEE 754):** Os cálculos de latência e consumo elétrico respeitam os limites de representação de 64 bits da máquina, considerando o epsilon do sistema (`ε ≈ 2.22 × 10⁻¹⁶`) para mitigar erros de arredondamento inerentes à conversão binária.
- **Análise de Erros:** Utilização rigorosa de **Erro Absoluto** (para preservar a unidade original em milissegundos) e **Erro Relativo** (para comparar desvios percentuais justos entre módulos que operam em escalas de latência completamente distintas).
- **Simulação Dinâmica (EDO):** Modelagem matemática da recuperação de enlaces de rede degradados utilizando Equações Diferenciais Ordinárias (EDOs) e métodos incrementais inspirados na discretização temporal (passo `h`).
- **Estruturas de Dados Avançadas:** 
  - **Árvores Trie:** Buscas por prefixo com complexidade de tempo `O(m)` para recuperação instantânea de módulos, comandos e códigos de sensores.
  - **Fila de Prioridade (Heap):** Escalonamento e atendimento de alertas críticos em tempo logarítmico `O(log n)`, garantindo resposta imediata a anomalias severas na rede da colônia.

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