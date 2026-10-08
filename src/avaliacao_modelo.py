import json
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = BASE_DIR / "data" / "dados_aurora_siger.json"

def avaliar_modelo_latencia():
    print("\n" + "=" * 80)
    print("      AVALIAÇÃO DE PERFORMANCE DO MODELO DE LATÊNCIA ")
    print("=" * 80)

    # 1. Carregar os dados
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
        dados = json.load(file)
    
    df = pd.DataFrame.from_dict(dados['modulos'], orient='index')

    # Nossas variáveis para a Regressão
    # y_pred = Previsão do modelo (Latência estimada)
    # y_true = Realidade (Latência observada)
    y_pred = df['latencia_estimada_ms']
    y_true = df['latencia_observada_ms']

    # 2. Cálculo das métricas (Scikit-Learn)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    # 3. Exibição dos Resultados
    print(f"Métricas Principais do Modelo:")
    print(f"- MAE (Erro Absoluto Médio):       {mae:.2f} ms")
    print(f"- MSE (Erro Quadrático Médio):     {mse:.2f} ms²")
    print(f"- RMSE (Raiz do Erro Quadrático):  {rmse:.2f} ms")
    print(f"- R² (Coef. de Determinação):      {r2:.4f}")
    
    # 4. Interpretação exigida pelo edital
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
    print("=" * 80)

if __name__ == "__main__":
    avaliar_modelo_latencia()