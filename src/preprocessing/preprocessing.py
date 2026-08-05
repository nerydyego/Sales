import pandas as pd

def converter_data(
    df: pd.DataFrame,
    coluna: str,
    formato: str | None = None,
    dayfirst: bool = True,
    errors: str = "raise"
) -> pd.DataFrame:
    """
    Converte uma coluna para datetime.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de entrada.
    coluna : str
        Nome da coluna.
    formato : str, optional
        Formato esperado da data (ex.: "%d-%m-%Y").
    dayfirst : bool
        Considera o dia antes do mês quando o formato não é informado.
    errors : {'raise', 'coerce', 'ignore'}
        Estratégia para tratar erros.

    Returns
    -------
    pd.DataFrame
        DataFrame com a coluna convertida.
        
    Examples:
    --------
        df = converter_data(
            df,
            coluna="Order Date",
            formato=None,
            errors="coerce"
        ) -> se você não souber o formato
    """

    if coluna not in df.columns:
        raise KeyError(f"Coluna '{coluna}' não encontrada.")

    df[coluna] = pd.to_datetime(
        df[coluna],
        format=formato,
        dayfirst=dayfirst,
        errors=errors
    )

    return df