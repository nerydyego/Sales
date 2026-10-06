# Sales Dataset

Projeto de análise exploratória e modelagem preditiva para estimar o lucro de transações de varejo a partir do dataset Superstore Sales.

## Objetivo
Prever `Profit` com base em atributos comerciais como região, segmento, categoria, faturamento, quantidade e desconto.

## Estrutura
```text
Sales_dataset/
├── data/
│   ├── raw/
│   └── processed/
├── notebook/
│   ├── analise.ipynb
│   └── ml.ipynb
├── src/
│   ├── preprocessing/
│   ├── visualizacao/
│   └── modelagem/
├── pyproject.toml
├── requirements.txt
├── README.md
└── image/
```

## Pipeline utilizado
- seleção das features relevantes;
- separação em treino e teste com `train_test_split(test_size=0.20, random_state=42)`;
- preprocessamento com `OneHotEncoder` e `ColumnTransformer`;
- comparação de modelos de regressão: Regressão Linear, Árvore de Decisão e Random Forest;
- validação cruzada com 5 folds e ajuste de hiperparâmetros via `GridSearchCV`.

## Principais insights
- o modelo tende a piorar em transações com faturamento muito alto (`Sales > P99`), mostrando que vendas elevadas não garantem lucro proporcional;
- o erro quadrático é concentrado em poucos casos extremos, o que indica variabilidade significativa na cauda superior da distribuição;
- apenas 2,65% das transações do teste possuem `Product ID` novo, reduzindo o risco de generalização para produtos desconhecidos;
- o problema principal continua sendo a previsibilidade do lucro em transações de maior valor e maior heterogeneidade.

## Tecnologias
- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Jupyter

## Execução
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Observação
Os resultados atuais são exploratórios e indicam a necessidade de validação mais rigorosa antes de uso operacional, com foco em teste independente e refinamento do modelo.
