import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from collections.abc import Sequence

def boxplot(
    df: pd.DataFrame,
    columns: str | Sequence[str],
    figsize: tuple[float, float] = (6, 4)
) -> None:
    """
    Cria boxplots para uma ou mais colunas de um DataFrame.

    Args:
        df:
            DataFrame contendo os dados que serão visualizados.

        columns:
            Nome de uma coluna ou sequência com os nomes das colunas
            que serão apresentadas no gráfico.

        figsize:
            Tamanho da figura no formato ``(largura, altura)``,
            em polegadas.

    Returns:
        None. O gráfico é exibido com o Matplotlib.

    Raises:
        TypeError:
            Se ``df`` não for um DataFrame ou se ``columns`` não for
            uma string ou uma sequência de strings.

        ValueError:
            Se nenhuma coluna for informada.

        KeyError:
            Se alguma coluna não existir no DataFrame.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df deve ser um DataFrame do pandas.")

    # Transforma uma única coluna em uma lista
    if isinstance(columns, str):
        columns = [columns]

    # Valida se foi passada uma sequência
    elif not isinstance(columns, Sequence):
        raise TypeError(
            "columns deve ser uma string ou uma sequência de strings."
        )

    # Converte tuplas e outros tipos de sequência em lista
    columns = list(columns)

    if not columns:
        raise ValueError("Informe pelo menos uma coluna.")

    # Verifica se todos os elementos são strings
    if not all(isinstance(column, str) for column in columns):
        raise TypeError(
            "Todos os nomes das colunas devem ser strings."
        )

    # Procura colunas que não existem no DataFrame
    colunas_ausentes = [
        column
        for column in columns
        if column not in df.columns
    ]

    if colunas_ausentes:
        raise KeyError(
            f"Colunas não encontradas no DataFrame: {colunas_ausentes}"
        )

    plt.figure(figsize=figsize)

    plt.boxplot(
        [df[column].dropna() for column in columns],
        tick_labels=columns
    )

    plt.title(f"Boxplot das variáveis {', '.join(columns)}")
    plt.ylabel("Valores")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


