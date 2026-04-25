# Automação de Web Scraping para E-commerce

Um bot de Automação Robótica de Processos (RPA) desenvolvido em Python para extrair, estruturar e exportar dados de produtos em marketplaces.

## Objetivo do Projeto
Eliminar o trabalho manual de pesquisa de preços e concorrência. O script navega automaticamente pelo site do Mercado Livre, busca por um produto específico e extrai informações estratégicas dos principais resultados, consolida tudo em uma planilha Excel pronta para análise.

## Funcionalidades
- **Navegação Automatizada:** Interage com o navegador, preenche campos de busca e simula comportamento humano.
- **Extração de Dados (Scraping):** Coleta o Nome do Produto, Preço, Nome do Vendedor e Avaliação Média.
- **Tratamento de Erros:** Estrutura robusta com `try/except` para lidar com anúncios que possuem informações incompletas sem quebrar o script.
- **Exportação de Dados:** Consolida as informações extraídas e gera automaticamente um relatório em formato `.xlsx`.

## Tecnologias Utilizadas
- **Python 3**
- **Selenium:** Para automação web e interação com o DOM.
- **Pandas & OpenPyXL:** Para estruturação de dados e geração do relatório em Excel.

## Como executar este projeto

***1. Clone o repositório:***
```bash
git clone [https://github.com/iurignzg1/ecommerce-data-scraper.git](https://github.com/iurignzg1/ecommerce-data-scraper.git)

***2. Instale as dependências necessárias:***

pip install selenium pandas openpyxl

***3. Execute o script:***

python Automacao.py

(O script irá abrir o navegador Firefox automaticamente, realizar a busca e gerar o arquivo relatorio_produtos.xlsx na mesma pasta).