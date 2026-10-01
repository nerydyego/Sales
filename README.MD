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
- [`notebook/ml.ipynb`](notebook/ml.ipynb): preparação de dados, treinamento de modelos de regressão para prever `Profit`, avaliação em holdout e validação cruzada para comparar profundidades da Árvore de Decisão.

### Modelagem e avaliação
O objetivo do experimento é estimar o lucro (`Profit`) de uma transação. As variáveis preditoras são modalidade de envio, segmento, região, categoria, subcategoria, vendas, quantidade e desconto. O notebook separa 20% dos dados para teste (`random_state=42`) e processa as variáveis categóricas com One-Hot Encoding, usando `ColumnTransformer` e `Pipeline` do scikit-learn.

Foram avaliados Regressão Linear e Árvore de Decisão. O notebook também compara árvores com profundidades máximas de 2, 3, 5, 7, 10, 15 e 20 e utiliza validação cruzada de cinco folds no conjunto de treino. As métricas incluem MAE, RMSE e R².

**Resultados no holdout 80/20**

| Modelo | Conjunto | MAE | RMSE | R² |
| --- | --- | ---: | ---: | ---: |
| Regressão Linear | Teste | 67,76 | 282,51 | -0,6461 |
| Árvore de Decisão sem limite de profundidade | Treino | 0,06 | 0,95 | 0,99998 |
| Árvore de Decisão sem limite de profundidade | Teste | 34,61 | 285,94 | -0,6863 |

**Validação cruzada da Árvore de Decisão por profundidade**

Valores abaixo são médias dos cinco folds no conjunto de treino; `R² desvio` indica o desvio-padrão do R² entre folds.

| Profundidade máxima | MAE validação | RMSE validação | R² validação | R² desvio |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 54,50 | 176,68 | 0,3360 | 0,3058 |
| 3 | 59,05 | 169,81 | 0,4224 | 0,1495 |
| 5 | 42,82 | 138,77 | 0,5844 | 0,2063 |
| 7 | 32,30 | 131,64 | 0,6641 | 0,1334 |
| 10 | 25,88 | 130,11 | 0,6618 | 0,1800 |
| 15 | 23,80 | 126,67 | 0,6660 | 0,2226 |
| 20 | 22,87 | 108,38 | 0,7346 | 0,2185 |

Na validação cruzada, a profundidade 20 obteve o maior R² médio entre as opções avaliadas, embora haja variação entre folds. Em contrapartida, todas as profundidades avaliadas no holdout tiveram R² negativo no teste (de -0,9541 a -0,6785), assim como a Regressão Linear e a árvore sem limite. Além disso, como o notebook consultou `X_test` ao comparar profundidades, esse conjunto não é mais uma avaliação final independente para a escolha do modelo. A árvore praticamente perfeita no treino também evidencia risco de sobreajuste. Os resultados são exploratórios; para uma estimativa final, será necessário manter um conjunto de teste realmente intocado ou adotar uma avaliação aninhada de validação cruzada. Nenhum modelo deve ser considerado validado para uso operacional neste estágio.

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
