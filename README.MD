# Sales Dataset

Projeto acadêmico de análise exploratória e modelagem preditiva aplicado ao conjunto de dados Superstore Sales, com foco na previsão do lucro de transações comerciais.

## Visão geral
Este repositório apresenta uma investigação aplicada em dados de varejo, combinando análise exploratória, engenharia de atributos, visualização analítica e comparação de modelos de regressão para prever a variável-alvo `Profit`.

O estudo foi estruturado para avaliar como variáveis comerciais e operacionais, como região, segmento, categoria, quantidade, desconto e faturamento, influenciam a rentabilidade das vendas. A abordagem combina fundamentos estatísticos, pré-processamento de dados e técnicas de aprendizado supervisionado.

## Objetivos
- compreender a estrutura e a qualidade dos dados de vendas;
- identificar variáveis associadas ao desempenho financeiro das transações;
- avaliar padrões por categoria, região, segmento e canal de venda;
- construir e comparar modelos de regressão para prever `Profit`;
- documentar hipóteses, limitações e oportunidades de refinamento metodológico.

## Contexto do dado
O conjunto de dados utilizado é o [Superstore Sales](https://www.kaggle.com/datasets/ishanshrivastava28/superstore-sales/data), disponibilizado publicamente no Kaggle. A base contém registros de transações comerciais com informações sobre:

- região e segmento de clientes;
- categoria e subcategoria de produtos;
- modalidade de envio;
- faturamento, desconto, quantidade e lucro;
- identificadores temporais e operacionais da venda.

## Estrutura do repositório
```text
Sales_dataset/
├── data/
│   ├── raw/
│   └── processed/
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
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── README.md
└── .git/
```

## Metodologia
### 1. Exploração e análise inicial
O notebook `notebook/analise.ipynb` foi utilizado para:
- verificar integridade e consistência dos dados;
- identificar valores ausentes, outliers e distribuições;
- analisar correlações e padrões de negócio;
- explorar atributos temporais e comportamentais relevantes.

### 2. Modelagem preditiva
O notebook `notebook/ml.ipynb` concentra a etapa de modelagem, com os seguintes passos:
- seleção das variáveis preditoras;
- definição da variável-alvo `Profit`;
- separação em treino e teste (`train_test_split`, `test_size=0.20`, `random_state=42`);
- preprocessing com `OneHotEncoder` e `ColumnTransformer`;
- comparação entre Regressão Linear, Árvore de Decisão e Random Forest;
- avaliação com métricas como MAE, RMSE e R²;
- uso de validação cruzada e `GridSearchCV` para ajuste de hiperparâmetros.

### 3. Módulos implementados
- `src/preprocessing/preprocessing.py`: conversão de colunas temporais para `datetime`;
- `src/visualizacao/view.py`: geração de boxplots para análise exploratória;
- `src/visualizacao/resultado.py`: cálculo de métricas de regressão;
- `src/modelagem/metricas.py`: consolidação de resultados em DataFrame comparativo.

## Modelos avaliados
Os modelos testados foram:
- Regressão Linear;
- Árvore de Decisão;
- Random Forest Regressor.

A comparação foi conduzida com foco em robustez preditiva, capacidade de generalização e análise de erro, em um contexto exploratório de aprendizado supervisionado.

## Principais achados
Os resultados indicam que:
- a relação entre faturamento e lucro não é linear nem necessariamente proporcional;
- em transações com faturamento muito alto, o desempenho do modelo se deteriora, sugerindo maior variabilidade na cauda superior da distribuição;
- o erro quadrático apresenta concentração em poucos casos extremos, evidenciando heterogeneidade na rentabilidade;
- apenas 2,65% das transações do conjunto de teste possuem `Product ID` novo, o que reduz a preocupação com produtos completamente desconhecidos;
- ainda há necessidade de validação mais rigorosa antes de qualquer uso operacional do modelo.

Esses achados reforçam a natureza exploratória do projeto e a importância de uma etapa adicional de refinamento, com conjunto de teste independente e avaliação mais robusta.

## Tecnologias
- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Requisitos e instalação
Pré-requisitos:
- Python 3.11+

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Como reproduzir
1. abra o projeto no VS Code;
2. inicialize o ambiente Jupyter;
3. execute os notebooks em ordem: `analise.ipynb` e `ml.ipynb`;
4. para uso local, mantenha o conjunto de dados em `data/raw/`.

## Limitações e próximos passos
- separar treino, validação e teste de forma mais formal para evitar vazamento de informação;
- aplicar engenharia de features mais robusta;
- comparar modelos com ajuste fino de hiperparâmetros;
- investigar erros por categoria, região e faixa de faturamento;
- preparar um pipeline de produção para aplicação prática.

## Conclusão
Este projeto representa uma aplicação acadêmica e prática de análise de dados e machine learning em contexto de varejo. A estrutura do repositório, os notebooks e os módulos desenvolvidos fornecem uma base sólida para desenvolvimento contínuo, refinamento metodológico e apresentação profissional em portfólio e projetos de estudo.

## Licença
O projeto é mantido para fins acadêmicos e de estudo. Consulte o arquivo de licença do repositório, caso seja necessário formalizar uso em contexto comercial ou colaborativo.
