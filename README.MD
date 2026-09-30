# Análise de Vendas Superstore

## Visão geral
Projeto de análise de dados e machine learning desenvolvido com o conjunto **Superstore Sales**. O trabalho explora o desempenho de vendas e lucros por região, categoria, produto, cliente e período, além de iniciar a construção de modelos para estimar o lucro de uma transação.

O projeto está organizado em notebooks para exploração e experimentação, com funções reutilizáveis separadas em módulos Python dentro de `src/`.

## Objetivos
- Investigar a qualidade, a distribuição e as relações entre as variáveis do conjunto de dados.
- Explorar padrões comerciais relacionados a faturamento, lucro, clientes, produtos, regiões e sazonalidade.
- Preparar variáveis e avaliar modelos de regressão para prever `Profit` (lucro).
- Registrar hipóteses e métricas para orientar as próximas etapas da análise.

## Dados
O conjunto utilizado é o [Superstore Sales, disponível no Kaggle](https://www.kaggle.com/datasets/ishanshrivastava28/superstore-sales/data). Os arquivos locais estão em `data/raw/`; os notebooks leem principalmente `Superstore.csv`. Há também uma versão Excel do conjunto nessa pasta.

## Notebooks
- [`notebook/analise.ipynb`](notebook/analise.ipynb): análise exploratória, estatística descritiva, identificação de valores extremos, visualizações comerciais e criação de variáveis temporais, como mês, ano, trimestre, dia da semana e tempo de entrega.
- [`notebook/ml.ipynb`](notebook/ml.ipynb): experimento de regressão para prever `Profit`, comparar Regressão Linear e Árvore de Decisão e avaliar as previsões.

### Experimento de machine learning
O alvo é `Profit`. Como preditoras, o experimento usa modalidade de envio, segmento, região, categoria, subcategoria, vendas, quantidade e desconto. Os dados são divididos em treino e teste na proporção 80/20, com `random_state=42`. As variáveis categóricas passam por One-Hot Encoding dentro de um `ColumnTransformer` e de pipelines do scikit-learn.

Resultados registrados no notebook:

| Modelo | Conjunto | MAE | RMSE | R² |
| --- | --- | ---: | ---: | ---: |
| Regressão Linear | Teste | 67,76 | 282,51 | -0,6461 |
| Árvore de Decisão | Treino | 0,06 | 0,95 | 0,99998 |
| Árvore de Decisão | Teste | 34,61 | 285,94 | -0,6863 |

Esses números são resultados preliminares salvos no notebook, não uma validação de modelo para uso operacional. O R² negativo no teste indica que os modelos ainda não superam uma previsão de referência baseada na média do alvo. A diferença entre o desempenho da Árvore de Decisão no treino e no teste é compatível com sobreajuste. A próxima etapa é investigar a generalização com validação cruzada, regularização e comparação com um modelo de referência.

## Módulos Python
- `src/preprocessing/preprocessing.py`: conversão de colunas de data para `datetime`, com opções de formato, tratamento de erros e ordem dia/mês.
- `src/visualizacao/view.py`: função reutilizável para gerar boxplots de uma ou mais colunas.
- `src/visualizacao/resultado.py`: cálculo de métricas de regressão, incluindo MAE, MSE, RMSE, R², média, mediana e desvio padrão.
- `src/modelagem/metricas.py`: registro das métricas de modelos em um DataFrame comparativo.

## Estrutura
```text
data/
   processed/
   raw/
      Superstore.csv
      Superstore.xlsx
hipoteses/
   atepas.txt
   dados.txt
   etapas.txt
   hipoteses.txt
notebook/
   analise.ipynb
   ml.ipynb
src/
   modelagem/metricas.py
   preprocessing/preprocessing.py
   visualizacao/resultado.py
   visualizacao/view.py
image/
pyproject.toml
requirements.txt
```

## Instalação e execução
Requisitos: Python 3.11 ou superior. No PowerShell, na pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
python -m pip install jupyterlab ipykernel kagglehub charset-normalizer
```

Abra a pasta no VS Code ou inicie o JupyterLab e execute as células do notebook desejado em ordem. O notebook de análise contém uma célula para baixar o conjunto pelo KaggleHub; como o CSV também está disponível em `data/raw/`, essa etapa pode ser ignorada quando o arquivo local já estiver presente.

## Tecnologias
Python, pandas, NumPy, scikit-learn, Matplotlib, Seaborn e Jupyter.
