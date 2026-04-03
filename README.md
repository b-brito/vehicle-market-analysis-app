# Web App de Análise de Veículos

## Objetivo

Desenvolver uma aplicação web interativa para análise de anúncios de veículos, com deploy em nuvem, aplicando boas práticas de engenharia de software, como versionamento, ambientes virtuais e publicação de serviços.

---

## Aplicação

A aplicação está disponível em:
https://tripleten-7wh5.onrender.com

---

## Contexto

O projeto teve como foco complementar habilidades de ciência de dados com práticas de engenharia de software, incluindo:

- Criação e gerenciamento de ambientes virtuais em Python  
- Desenvolvimento de aplicação web com Streamlit  
- Deploy em nuvem (Render)  
- Versionamento com Git e GitHub  

---

## Abordagem

Antes do desenvolvimento da aplicação, foi realizada uma análise exploratória dos dados (EDA) para:

- Entender o comportamento das variáveis  
- Identificar padrões relevantes  
- Definir visualizações adequadas  

A aplicação foi então construída para exibir gráficos interativos que permitem explorar os dados de forma intuitiva.

---

## Principais Insights

- Correlação positiva entre **preço e ano do modelo (0,43)**  
- Correlação negativa entre:
  - **quilometragem e ano (-0,47)**  
  - **quilometragem e preço (-0,41)**  

Indica que:
- Carros mais novos tendem a ser mais caros e rodados menos  
- O preço diminui conforme a quilometragem aumenta  

- A variável **days_listed** não apresentou correlação relevante  
  - sugerindo influência de fatores qualitativos (marca, condição, combustível)

- Presença de **outliers em todas as marcas**, refletindo variações entre versões e categorias  

- Diferenças por tipo de veículo:
  - **Sedans → menor preço e menor dispersão**  
  - **SUVs → intermediários**  
  - **Pickups e trucks → maiores preços e maior variabilidade**

---

## Tecnologias

- Python (pandas, plotly, streamlit)  
- Visualização de dados  
- Git & GitHub  
- Render (deploy em nuvem)  

---

## Autor

Bruno Brito