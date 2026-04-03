import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Análise de Veículos - Sprint 5", layout="wide")
st.header("Dashboard – Análise de Veículos (TripleTen Sprint 5)")

# ===== dados da raiz do repo =====
df = pd.read_csv("data/vehicles_us.csv")

# ===== pré-processamento (igual ao seu notebook) =====
for c in ['cylinders', 'is_4wd', 'date_posted']:
    if c in df.columns:
        df = df.drop(columns=c)
df = df.dropna()
df['model_year'] = df['model_year'].astype(int)
df['brand'] = df['model'].str.split().str[0].str.lower()

st.subheader("Exploração de Dados")

# 1) correlação (apenas plotly)
if st.button("Mapa de correlação"):
    numeric = df.select_dtypes(include="number").columns.tolist()
    corr = df[numeric].corr()
    fig = px.imshow(corr, text_auto=True, aspect="auto",
                    title="Correlação entre variáveis numéricas")
    st.plotly_chart(fig, use_container_width=True)

# 2) dispersão: preço x ano
if st.button("Preço x Ano"):
    fig = px.scatter(df, x='model_year', y='price', title='Preço x Ano do Modelo')
    fig.update_layout(xaxis_title='Ano do modelo', yaxis_title='Preço (US$)')
    st.plotly_chart(fig, use_container_width=True)

# 3) dispersão: odômetro x ano
if st.button("Odômetro x Ano"):
    fig = px.scatter(df, x='model_year', y='odometer', title='Odômetro x Ano do Modelo')
    fig.update_layout(xaxis_title='Ano do modelo', yaxis_title='Odômetro')
    st.plotly_chart(fig, use_container_width=True)

# 4) dispersão: preço x odômetro
if st.button("Preço x Odômetro"):
    fig = px.scatter(df, x='odometer', y='price', title='Preço x Odômetro')
    fig.update_layout(xaxis_title='Odômetro', yaxis_title='Preço (US$)')
    st.plotly_chart(fig, use_container_width=True)

# 5) histograma de quilometragem
if st.button("Histograma de Quilometragem"):
    fig = px.histogram(df, x='odometer', title='Distribuição de Quilometragem')
    fig.update_layout(xaxis_title='Odômetro', yaxis_title='Contagem')
    st.plotly_chart(fig, use_container_width=True)

# 6) histograma por tipo de combustível
if st.button("Histograma por Tipo de Combustível"):
    fig = px.histogram(df, x='odometer', color='fuel', opacity=0.6,
                       barmode="overlay",
                       title='Distribuição de Quilometragem por Tipo de Combustível')
    fig.update_layout(xaxis_title='Odômetro', yaxis_title='Contagem')
    st.plotly_chart(fig, use_container_width=True)

# 7) boxplots de preço (top marcas e tipos)
if st.button("Boxplots de Preço"):
    top_brands = df['brand'].value_counts().head(10).index
    top_types  = df['type'].value_counts().head(4).index
    dff = df[df['brand'].isin(top_brands) & df['type'].isin(top_types)]

    order_brand = dff.groupby('brand')['price'].median().sort_values().index
    fig1 = px.box(dff, x='brand', y='price', color='brand', points='outliers',
                  title='Preço por Marca', category_orders={'brand': order_brand})
    fig1.update_layout(xaxis_title='Marca', yaxis_title='Preço (US$)')
    st.plotly_chart(fig1, use_container_width=True)

    order_type = dff.groupby('type')['price'].median().sort_values().index
    fig2 = px.box(dff, x='type', y='price', color='type', points='outliers',
                  title='Preço por Tipo de Veículo', category_orders={'type': order_type})
    fig2.update_layout(xaxis_title='Tipo', yaxis_title='Preço (US$)')
    st.plotly_chart(fig2, use_container_width=True)

st.caption("Fonte de dados: vehicles_us.csv (TripleTen Sprint 5)")
