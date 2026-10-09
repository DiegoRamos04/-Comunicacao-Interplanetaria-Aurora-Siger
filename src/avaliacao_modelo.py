import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = BASE_DIR / "data" / "dados_aurora_siger.json"
PASTA_GRAFICOS = BASE_DIR / "graficos_ou_imagens"

def avaliar_modelo_latencia():
    print("\n" + "=" * 80)
    print("      AVALIAÇÃO DE PERFORMANCE DO MODELO DE LATÊNCIA ")
    print("=" * 80)

    # 1. Carregar os dados
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
            dados = json.load(file)
    except FileNotFoundError:
        print(f"Erro: Banco de dados '{ARQUIVO_JSON.name}' não encontrado.")
        return
    
    df = pd.DataFrame.from_dict(dados['modulos'], orient='index')

    y_pred = df['latencia_estimada_ms']
    y_true = df['latencia_observada_ms']

    # Cálculo do Erro Absoluto e Relativo linha a linha (Requisito 5.2)
    df['erro_absoluto'] = abs(y_true - y_pred)
    # Evita divisão por zero caso a latência estimada seja 0
    df['erro_relativo'] = np.where(y_pred != 0, df['erro_absoluto'] / y_pred, 0)
    
    print("\nAmostra de Análise Numérica (Erro Absoluto e Relativo):")
    print(df[['latencia_observada_ms', 'latencia_estimada_ms', 'erro_absoluto', 'erro_relativo']].head())

    # 2. Cálculo das métricas
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    # 3. Exibição dos Resultados no Terminal
    print(f"Métricas Principais do Modelo:")
    print(f"- MAE (Erro Absoluto Médio):       {mae:.2f} ms")
    print(f"- MSE (Erro Quadrático Médio):     {mse:.2f} ms²")
    print(f"- RMSE (Raiz do Erro Quadrático):  {rmse:.2f} ms")
    print(f"- R² (Coef. de Determinação):      {r2:.4f}")
    
    # 4. Geração do Gráfico Futurista (Dark Mode)
    try:
        PASTA_GRAFICOS.mkdir(exist_ok=True)
        
        # Configuração do fundo escuro
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('#0d1117') # Cor de fundo da imagem (estilo GitHub Dark)
        ax.set_facecolor('#161b22')        # Cor de fundo da área do gráfico
        
        # Plot das linhas e pontos com cores vibrantes (Cyan e Red)
        ax.plot(df.index, y_pred, label='Latência Estimada (Normal)', color='#00ffcc', marker='o', linestyle='--', linewidth=2)
        ax.scatter(df.index, y_true, label='Latência Observada (Anomalia)', color='#ff3333', s=100, zorder=5)
        
        # Personalização dos Textos
        ax.set_title('PAINEL DE TELEMETRIA: Latência da Rede (Aurora Siger)', color='white', fontsize=14, fontweight='bold', pad=15)
        ax.set_ylabel('Tempo de Latência (ms)', color='#c9d1d9', fontsize=12)
        ax.set_xlabel('Módulos da Colônia', color='#c9d1d9', fontsize=12)
        
        # Personalização dos Eixos e Grelha
        ax.tick_params(axis='x', colors='#c9d1d9', rotation=45)
        ax.tick_params(axis='y', colors='#c9d1d9')
        for spine in ax.spines.values():
            spine.set_color('#30363d')
            
        ax.grid(True, color='#30363d', linestyle=':', linewidth=1)
        
        # Personalização da Legenda
        legend = ax.legend(facecolor='#0d1117', edgecolor='#30363d', labelcolor='white')
        
        plt.tight_layout()
        
        # Salvar o ficheiro
        caminho_imagem = PASTA_GRAFICOS / "grafico_anomalia_rede.png"
        plt.savefig(caminho_imagem, facecolor=fig.get_facecolor(), edgecolor='none')
        plt.close()
        print(f"\nSUCESSO: Gráfico de anomalias atualizado e salvo em '{PASTA_GRAFICOS.name}/grafico_anomalia_rede.png'")
    except Exception as e:
        print(f"\nNão foi possível gerar o gráfico visual: {e}")

    # 5. Interpretação
    print("\n" + "-" * 80)
    print("INTERPRETAÇÃO DOS RESULTADOS (DEFESA DO NÚCLEO COGNITIVO):")
    print("-" * 80)
    print("Conforme avaliado, um único número não é suficiente para validar a solução.")
    print("O R² apresentou um valor anômalo, indicando que o nosso modelo falhou em prever")
    print("a realidade. Isso não é um defeito do modelo, mas sim o sintoma da invasão.")
    print("\nA enorme diferença entre o MAE e o RMSE indica a presença de um grande 'outlier'")
    print("(ponto fora da curva). O RMSE penaliza erros maiores, e como o módulo de")
    print("Comunicação teve um pico de 185ms (contra 5ms previstos), o MSE e o RMSE")
    print("explodiram, denunciando a anomalia na rede da Aurora Siger.")
    print("\nAlém disso, a análise do Erro Relativo revelou-se fundamental para a colônia.")
    print("Como os módulos operam em escalas de latência completamente diferentes, o erro")
    print("relativo permite comparar a gravidade do desvio de forma percentual e justa.")
    print("Isso garante que um desvio num módulo crítico não passe despercebido, enquanto")
    print("pequenas oscilações aceitáveis em módulos secundários não gerem falsos alarmes.")
    print("=" * 80)

if __name__ == "__main__":
    avaliar_modelo_latencia()