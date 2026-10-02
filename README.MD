# Sales Dataset — Análise exploratória e modelagem de lucro

## Visão geral
Este projeto tem como objetivo explorar o conjunto de dados de vendas da empresa Superstore e desenvolver um fluxo inicial de modelagem preditiva para estimar o lucro de uma transação. A análise combina exploração estatística, visualização de padrões comerciais e avaliação de modelos de regressão.

O repositório foi estruturado para apoiar a etapa de pesquisa e análise, separando a lógica de preprocessamento, visualização e comparação de métricas em módulos reutilizáveis dentro da pasta `src/`.

## Objetivos
- Compreender a distribuição e a qualidade dos dados.
- Identificar fatores que influenciam faturamento e lucro.
- Explorar padrões por região, categoria, segmento, canal de venda e período temporal.
- Preparar variáveis para treinamento de modelos preditivos.
- Avaliar modelos de regressão para prever a variável alvo `Profit`.
- Registrar hipóteses, métricas e observações para orientar etapas futuras.

## Dataset
O conjunto utilizado é o [Superstore Sales](https://www.kaggle.com/datasets/ishanshrivastava28/superstore-sales/data), disponibilizado publicamente no Kaggle. Os dados estão armazenados em `data/raw/`, com foco principal no arquivo `Superstore.csv`.

A base contém informações comerciais como:
- região e segmento de clientes;
- categoria e subcategoria de produtos;
- datas de pedido e entrega;
- quantidade, vendas, descontos e lucro;
- canal de vendas e modalidade de envio.

## Estrutura do projeto
```text
Sales_dataset/
├── data/
│   ├── processed/
│   └── raw/
│       └── Superstore.csv
├── hipoteses/
│   ├── atepas.txt
│   ├── dados.txt
│   ├── etapas.txt
│   └── hipoteses.txt
├── image/
├── notebook/
│   ├── analise.ipynb
│   └── ml.ipynb
├── src/
│   ├── modelagem/
│   │   └── metricas.py
│   ├── preprocessing/
│   │   └── preprocessing.py
│   └── visualizacao/
│       ├── resultado.py
│       └── view.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Fluxo de trabalho
### 1. Exploração e análise exploratória
O notebook `notebook/analise.ipynb` é responsável por:
- revisar a integridade dos dados;
- identificar valores ausentes, outliers e inconsistências;
- analisar distribuições e correlações;
- gerar visualizações de negócio;
- transformar variáveis de tempo em features relevantes;
- apoiar a formulação de hipóteses sobre desempenho comercial.

### 2. Modelagem preditiva
O notebook `notebook/ml.ipynb` realiza:
- preparação dos dados para treinamento;
- encoding de variáveis categóricas;
- uso de pipelines com `ColumnTransformer` e `Pipeline` do scikit-learn;
- comparação entre Regressão Linear, Árvore de Decisão e Random Forest;
- avaliação por métricas como MAE, RMSE e R²;
- análise exploratória de hiperparâmetros e validação cruzada.

### 3. Módulos reutilizáveis
- `src/preprocessing/preprocessing.py`: conversão de colunas de data para `datetime` com suporte a tratamento de erros e formatação.
- `src/visualizacao/view.py`: geração de boxplots para análise univariada.
- `src/visualizacao/resultado.py`: cálculo de métricas de regressão.
- `src/modelagem/metricas.py`: consolidação de resultados de modelos em estrutura tabular.

## Modelagem e avaliação
A variável-alvo do experimento é `Profit`, e o objetivo é estimar o lucro de uma transação a partir de atributos como:
- segmento;
- região;
- categoria e subcategoria;
- vendas;
- quantidade;
- desconto;
- modalidade de envio.

Os modelos avaliados incluem:
- Regressão Linear;
- Árvore de Decisão;
- Random Forest.

### Resultados exploratórios
Os resultados obtidos são úteis para orientar a exploração, mas devem ser interpretados com cautela, especialmente por se tratarem de um estudo inicial. Em vários cenários, o desempenho em treino foi muito bom e o desempenho em teste foi instável, indicando risco de overfitting e necessidade de validação mais robusta.

Em síntese:
- a árvore de decisão apresentou bons resultados em validação cruzada em algumas profundidades;
- o Random Forest mostrou desempenho competitivo em validação cruzada;
- os resultados de holdout indicaram que a generalização ainda precisa ser melhor validada;
- uma avaliação final mais confiável exigirá conjunto de teste intocado e/ou validação cruzada aninhada.

> Importante: os experimentos atuais são exploratórios e não devem ser considerados prontos para uso operacional sem uma etapa adicional de validação estatística e seleção de modelo.

## Tecnologias
- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Instalação e execução
Requisitos: Python 3.11 ou superior.

No PowerShell, execute:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
python -m pip install jupyterlab ipykernel kagglehub charset-normalizer
```

Em seguida:
1. abra a pasta do projeto no VS Code;
2. inicie o Jupyter ou JupyterLab;
3. execute os notebooks na ordem desejada;
4. se o dataset local já estiver presente em `data/raw/`, a etapa de download via KaggleHub pode ser ignorada.

## Próximos passos sugeridos
- definir uma divisão final de treino/validação/teste sem vazamento de dados;
- aplicar engenharia de features mais robusta;
- comparar modelos com tuning mais sistemático;
- analisar erros de previsão e segmentação por categoria/cliente/região;
- preparar um pipeline de produção para automatizar a predição de lucro.

## Observação final
Este repositório representa uma base sólida para análise exploratória e experimentação inicial com machine learning em dados de vendas. O projeto está bem organizado para continuidade, refinamento metodológico e evolução em direção a um processo mais profissional e orientado à decisão de negócio.
