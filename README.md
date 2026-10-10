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
│   └── 🖼️ grafico_anomalia_rede.png 
│
└── 📁 src/                        # Código-fonte e módulos auxiliares
    ├── 📄 alertas_heap.py         # Lógica de priorização de alertas (Heap)
    ├── 📄 avaliacao_modelo.py     # Scripts de validação e testes
    ├── 📄 dinamica_rede.py        # Simulação EDO e recuperação de rede (SciPy)
    ├── 📄 modulos.py              # Funções modulares de apoio (Pandas e Lei de Ohm)
    ├── 📄 registros.py            # Manipulação de logs e registros manuais
    └── 📄 trie_buscas.py          # Lógica de busca otimizada e conversão (Trie)

## Análise de Complexidade (Fundamentação Teórica)
Para garantir que o SCIC opere com eficiência em cenários de alta criticidade na colônia Aurora Siger, o projeto aplica conceitos de análise assintótica de algoritmos:

- **Buscas Otimizadas (Trie):** As operações de inserção e recuperação por prefixo possuem complexidade de tempo **O(m)** (no qual *m* é o tamanho do prefixo), superando a busca linear tradicional.
- **Fila de Prioridade (Heap):** O escalonamento de alertas críticos utiliza operações logarítmicas **O(log n)** para inserção e remoção de prioridades.
- **Trade-off Espaço-Tempo:** O isolamento de falhas na simulação utiliza cópias estruturais em memória RAM, priorizando a segurança dos dados persistidos em detrimento de um consumo controlado de espaço auxiliar.

## Fundamentação Teórica e Métodos Numéricos

Para garantir a precisão, a estabilidade e a confiabilidade nas transmissões críticas da colônia Aurora Siger, o SCIC incorpora os seguintes fundamentos matemáticos e computacionais estudados no projeto:

- **Aritmética de Ponto Flutuante (IEEE 754):** Os cálculos de latência e consumo elétrico respeitam os limites de representação de 64 bits da máquina, considerando o epsilon do sistema (`ε ≈ 2.22 × 10⁻¹⁶`) para mitigar erros de arredondamento inerentes à conversão binária.
- **Análise de Erros:** Utilização rigorosa de **Erro Absoluto** (para preservar a unidade original em milissegundos) e **Erro Relativo** (para comparar desvios percentuais justos entre módulos que operam em escalas de latência completamente distintas).
- **Simulação Dinâmica (EDO):** Modelagem matemática da recuperação de enlaces de rede degradados utilizando Equações Diferenciais Ordinárias (EDOs) e métodos incrementais inspirados na discretização temporal (passo `h`).
- **Estruturas de Dados Avançadas:** 
  - **Árvores Trie:** Buscas por prefixo com complexidade de tempo `O(m)` para recuperação instantânea de módulos, comandos e códigos de sensores.
  - **Fila de Prioridade (Heap):** Escalonamento e atendimento de alertas críticos em tempo logarítmico `O(log n)`, garantindo resposta imediata a anomalias severas na rede da colônia.
  - **Infraestrutura Elétrica e Estabilidade de Rede:** Para proteger os microcontroladores e módulos críticos da Aurora Siger contra oscilações e quedas bruscas de tensão resultantes de picos de demanda (como o acionamento de motores ou sistemas vitais), o SCIC incorpora a modelagem matemática de bancos de capacitores. Utilizando as equações de associação em paralelo (Ceq = C1 + C2 + ... + Cn) e o cálculo da energia armazenada (En = 1/2 * Q * V), o sistema dimensiona reservas de energia eletrostática. Estas reservas operam em frações de segundo, garantindo que os componentes eletrônicos e enlaces de comunicação não reiniciem durante flutuações, assegurando a estabilidade ininterrupta da telemetria interplanetária.
  - **Gerenciamento Inteligente e Microrredes:** O SCIC atua como um sistema ADMS (Advanced Distribution Management System) simplificado. Através da análise de dados contínua (simulando sensores IoT e telemetria), o sistema detecta anomalias (como picos de latência) e aciona protocolos de automação. Em situações críticas, o algoritmo simula a transição da rede elétrica para "operação ilhada", isolando falhas (tecnologia FLISR) para que módulos vitais continuem operando de forma autônoma. Essa manutenção preditiva e a gestão da microrrede garantem a resiliência e a estabilidade da comunicação na Aurora Siger.
  - **Assistentes Virtuais e Automação:** O SCIC simula a orquestração de fluxos de trabalho baseada em nós (nodes), inspirada em plataformas low-code como o n8n. Através da simulação de gatilhos (triggers) e agentes de IA, o sistema demonstra como assistentes virtuais podem intermediar a comunicação entre os operadores humanos da Aurora Siger e a base de dados. Essa automação permite integrar serviços de mensagens (como Telegram) para notificar a equipe sobre alertas operacionais de forma autônoma e em linguagem natural, transformando automações estáticas em um ciclo dinâmico de percepção, decisão e ação.

  ## Avaliação de Performance e Aprendizado de Máquina 
O SCIC implementa um fluxo estrutural de Machine Learning para prever o comportamento da latência utilizando **Regressão Linear** (`scikit-learn` e `statsmodels`):
- **Divisão de Dados:** O particionamento (80% treino, 20% teste) foi aplicado para garantir que a IA seja avaliada em dados não observados, evitando overfitting.
- **Métricas:** Utilização de MAE, MSE, RMSE e R² diretamente no conjunto de teste.
- **Avaliação Estrutural:** Análise de adequação e penalização por complexidade paramétrica via critérios **AIC** e **BIC**, preparando a colônia para futuras comparações de modelos.

## Ferramentas Computacionais e Estrutura Algébrica 
A infraestrutura analítica do SCIC foi desenvolvida utilizando o ecossistema computacional de modelagem linear em Python, onde cada operação reflete um conceito matemático consolidado:
- **NumPy (Operações Vetorizadas):** As operações matemáticas de erro e as simulações de dados (como `np.random` e `np.where`) foram implementadas através de *arrays*, garantindo processamento otimizado na memória e evitando laços de repetição custosos para a colônia.
- **Pandas (Estruturação Tabular):** Utilizado para a conversão da base de dados heterogênea em JSON para objetos *DataFrame*, permitindo a manipulação relacional, indexação e preparação estrutural das features elétricas e operacionais.
- **Matplotlib (Diagnóstico Visual):** Empregado na análise exploratória e diagnóstica. A plotagem de dispersão e as linhas base permitem a verificação visual imediata de outliers e do comportamento empírico das latências na rede interplanetária.
- **Scikit-Learn (Integração e Validação):** A biblioteca padroniza o fluxo de *Machine Learning* por meio dos métodos de ajuste (`fit`) e predição (`predict`), materializando o princípio estatístico de generalização e otimização da função de custo sem a necessidade imediata de *frameworks* de tensores complexos baseados em gradiente descendente.

## Dispositivos, Interfaces e Arquitetura 
O protótipo SCIC foi projetado para interagir conceitualmente com a infraestrutura de hardware da Aurora Siger:
- **Dispositivos de Entrada (Input):** Os dados operacionais brutos são coletados por sensores IoT espalhados nas microrredes (simulados via JSON), enquanto teclados mecânicos/membrana são utilizados para a inserção de comandos manuais no terminal pelos operadores.
- **Dispositivos de Saída (Output):** O terminal interativo e os gráficos diagnósticos funcionam como painéis de telemetria projetados em monitores com tecnologia OLED ou LCD da base.
- **Interfaces de Comunicação:** O tráfego de dados e os gargalos de latência simulados refletem o comportamento de conexões sem fio locais (como Wi-Fi e Bluetooth) e o roteamento estruturado da colônia.
- **Bases Numéricas e Eletricidade:** O sistema converte parâmetros de potência energética para as linguagens nativas das máquinas (Binário) e microcontroladores (Hexadecimal), além de aplicar a Lei de Ohm no dimensionamento operacional.

## Gerenciamento Inteligente da Comunicação 
Os módulos de simulação (EDO) e o escalonamento via Fila de Prioridade (Heap) materializam os pilares de uma rede inteligente:
- **Monitoramento Contínuo:** A IA integrada e o SCIC rastreiam divergências entre latência prevista e observada (Erro Relativo), detectando invasões instantaneamente sem depender de varreduras humanas exaustivas.
- **Automação e Redundância:** Ao priorizar nós vitais (como *Produção de Oxigênio* e *Centro de Controle*), a rede permite rotear recursos emergenciais rapidamente, ativando manutenções preditivas antes que uma oscilação cause o colapso estrutural.

## Reflexão Social, Cultural e Sustentável

O desenvolvimento do SCIC transcende a aplicação técnica, englobando uma reflexão profunda sobre o impacto de tecnologias inteligentes na sociedade e no meio ambiente. A concepção deste protótipo para a Aurora Siger foi norteada por três pilares fundamentais, inspirados na história e cultura Afro-Brasileira e Indígena:

1. **Conhecimentos Tradicionais e Sustentabilidade:** Assim como os povos indígenas mantêm uma relação de profundo respeito com o meio ambiente e extraem da natureza apenas os recursos estritamente necessários para sobrevivência, o SCIC aplica essa filosofia à gestão de recursos tecnológicos. Ao priorizar falhas eficientemente (Heap) e agilizar consultas (Trie), o sistema garante o uso eficiente da energia de comunicação, contribuindo diretamente para a sustentabilidade da colônia e evitando o desperdício energético dos módulos.
2. **Valorização da Diversidade e Combate a Vieses:** A história de resistência dos povos afro-brasileiros e indígenas nos ensina a importância fundamental de construir estruturas equitativas. Nesse sentido, o banco de dados do SCIC foi modelado com total transparência para evitar sistemas excludentes, garantindo que as métricas de performance e as automações operacionais não incorporem linguagem discriminatória ou interpretações injustas ao analisar o trabalho humano e técnico na base.
3. **Supervisão Humana nas Decisões Automatizadas:** Embora o SCIC simule gerenciamento inteligente de rede e assistentes virtuais de notificação, a equipe humana e sua diversidade continuam sendo os responsáveis éticos e operacionais por validar as ações automatizadas (como o desligamento de módulos ou classificação de falhas graves), garantindo que a tecnologia atue como suporte ao bem-estar da comunidade, e não como uma caixa-preta isolada.


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