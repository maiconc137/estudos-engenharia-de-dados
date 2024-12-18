import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo (simulados para vendas diárias ao longo de 1 ano)
dias = np.arange(1, 366)  # Dias do ano
vendas = 100 + 30 * np.sin(2 * np.pi * dias / 7) + 10 * np.random.randn(len(dias))  # Sazonalidade semanal + ruído

# Aplicar a Transformada de Fourier
transformada = np.fft.fft(vendas)
frequencias = np.fft.fftfreq(len(dias))

# Filtrar frequências significativas
indice_frequencias = np.argsort(-np.abs(transformada))  # Ordenar pela magnitude
frequencias_dominantes = frequencias[indice_frequencias[:5]]

# Reconstrução das vendas usando as frequências dominantes
reconstrucao = np.fft.ifft(transformada * (np.abs(transformada) > np.max(np.abs(transformada)) * 0.5)).real

# Visualização
plt.figure(figsize=(12, 6))
plt.plot(dias, vendas, label="Vendas Reais", alpha=0.6)
plt.plot(dias, reconstrucao, label="Reconstrução (Padrão Principal)", linewidth=2)
plt.legend()
plt.xlabel("Dias")
plt.ylabel("Vendas")
plt.title("Análise de Sazonalidade com Transformada de Fourier")
plt.show()
