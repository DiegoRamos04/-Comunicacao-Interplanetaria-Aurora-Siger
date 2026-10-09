import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_GRAFICOS = BASE_DIR / "graficos_ou_imagens"

def simular_evolucao_latencia():
    """
    Simula a evolução temporal da latência de um módulo comprometido 
    retornando ao estado estável, utilizando EDO de 1ª ordem (Capítulo 5).
    """
    print("\n" + "=" * 80)
    print("      SIMULAÇÃO DINÂMICA DE REDE (EQUAÇÕES DIFERENCIAIS - EDO / SCIPY)")
    print("=" * 80)

    # Parâmetros da EDO: taxa de recuperação do enlace da colônia (k)
    k = 0.4 
    latencia_ambiente = 15.0 # Latência normal esperada (ms)
    
    # EDO: dL/dt = -k * (L - L_ambiente) -> Lei de ajuste dinâmico inspirada em Newton
    def edo_latencia(t, L):
        return -k * (L - latencia_ambiente)

    # Condição inicial: Módulo de Comunicação sofreu um ataque e disparou para 185 ms
    l_inicial = [185.0] 
    t_span = (0.0, 15.0) # Intervalo de tempo da simulação (horas ou ciclos)
    t_eval = np.linspace(0.0, 15.0, 300)

    # Resolução numérica usando solve_ivp 
    sol = solve_ivp(edo_latencia, t_span, l_inicial, t_eval=t_eval, method='RK45')

    print(f"Estado Inicial (Anomalia): {l_inicial[0]} ms")
    print(f"Estado Final (Estabilizado após simulação): {sol.y[0][-1]:.2f} ms")
    print("\nA EDO modelou com sucesso a dissipação do atraso na rede da Aurora Siger.")

    # Geração do Gráfico de Comportamento Dinâmico
    try:
        PASTA_GRAFICOS.mkdir(exist_ok=True)
        fig, ax = plt.subplots(figsize=(9, 5))
        fig.patch.set_facecolor('#0d1117')
        ax.set_facecolor('#161b22')

        ax.plot(sol.t, sol.y[0], label='Latência Dinâmica L(t)', color='#00ffcc', linewidth=2.5)
        ax.axhline(latencia_ambiente, color='#ff3333', linestyle='--', label='Latência Alvo / Nominal (15ms)')

        ax.set_title('DINÂMICA DE REDE: Recuperação de Enlace (SciPy solve_ivp)', color='white', fontsize=12, fontweight='bold', pad=12)
        ax.set_xlabel('Tempo de Simulação', color='#c9d1d9', fontsize=10)
        ax.set_ylabel('Latência (ms)', color='#c9d1d9', fontsize=10)

        ax.tick_params(colors='#c9d1d9')
        for spine in ax.spines.values():
            spine.set_color('#30363d')
        ax.grid(True, color='#30363d', linestyle=':', linewidth=1)
        ax.legend(facecolor='#0d1117', edgecolor='#30363d', labelcolor='white')

        plt.tight_layout()
        caminho_img = PASTA_GRAFICOS / "grafico_dinamica_rede.png"
        plt.savefig(caminho_img, facecolor=fig.get_facecolor(), edgecolor='none')
        plt.close()
        print(f"Sucesso: Gráfico dinâmico salvo em '{PASTA_GRAFICOS.name}/grafico_dinamica_rede.png'")
    except Exception as e:
        print(f"Aviso ao gerar gráfico dinâmico: {e}")

    print("=" * 80)

if __name__ == "__main__":
    simular_evolucao_latencia()