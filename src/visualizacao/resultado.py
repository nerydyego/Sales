import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, confusion_matrix, classification_report

def calcular_metricas_regressao(y_true, y_pred):
    """
    Calcula métricas de avaliação para modelos de regressão.

    Parâmetros:
    y_true (array-like): Valores reais.
    y_pred (array-like): Valores previstos pelo modelo.

    Retorna:
    dict: Um dicionário contendo as métricas calculadas.
    """
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    media = y_true.mean()
    mediana = y_true.median()
    desvio_padrao = y_true.std()

    return {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'R2': r2,
        "Média": media,
        "Mediana": mediana,
        "Desvio Padrão": desvio_padrao
    }


