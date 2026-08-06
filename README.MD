# Projeto de Análise de Vendas

## Resumo do projeto
Este projeto tem como objetivo realizar uma análise exploratória do dataset de vendas, com foco em compreender o comportamento de vendas, lucro, clientes, categorias, regiões e produtos. A análise é conduzida principalmente em um notebook principal, com funções auxiliares organizadas em módulos de pré-processamento e visualização.

## Dataset
O conjunto de dados utilizado neste projeto é o Superstore Sales, disponível em: https://www.kaggle.com/datasets/ishanshrivastava28/superstore-sales/data

## O que vem sendo executado
- Carregamento e exploração do dataset de vendas a partir da pasta de dados brutos.
- Limpeza e transformação de colunas, incluindo conversão de datas para o formato adequado.
- Geração de gráficos e visualizações para apoiar a interpretação dos resultados.
- Organização de hipóteses de negócio e material visual para a comunicação dos insights.

## Estrutura do projeto
- data/raw/: dados brutos utilizados no estudo.
- data/processed/: dados já tratados ou preparados para análise.
- notebook/analise.ipynb: notebook principal com a análise exploratória.
- src/preprocessing/preprocessing.py: funções para preparação e transformação dos dados.
- src/visualizacao/view.py: funções para criação de visualizações.
- hipoteses/: arquivo com hipóteses e direcionamentos de análise.
- image/: imagens e gráficos gerados durante o projeto.
- pyproject.toml: configuração do projeto e dependências.
- requirements.txt: dependências Python do projeto.

## Como replicar o projeto
1. Crie um ambiente virtual em Python 3.11.
2. Instale as dependências:
   - pip install -r requirements.txt
   - pip install -e .
3. Para trabalhar com notebooks, instale também os extras de notebook:
   - pip install -e .[notebook]
4. Abra o notebook em notebook/analise.ipynb e execute as células em ordem.

## Dependências principais
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- kaggle

## Observações
O projeto assume que o arquivo principal do dataset está disponível em data/raw/. A estrutura atual está organizada para permitir evolução futura para dashboards, modelos preditivos ou automação de relatórios.
