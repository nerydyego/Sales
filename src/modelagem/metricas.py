import pandas as pd


def registrar_resultado(resultados, nome_modelo, metricas):
    """
    Registra as métricas de um modelo no DataFrame de resultados.

    Parâmetros
    ----------
    resultados : pd.DataFrame
        DataFrame contendo os resultados dos modelos.

    nome_modelo : str
        Nome do modelo avaliado.

    metricas : dict
        Dicionário contendo as métricas do modelo.

    Retorna
    -------
    pd.DataFrame
        DataFrame atualizado com o novo resultado.
    """

    novo_resultado = {
        "Modelo": nome_modelo,
        **metricas
    }

    return pd.concat(
        [
            resultados,
            pd.DataFrame([novo_resultado])
        ],
        ignore_index=True
    )