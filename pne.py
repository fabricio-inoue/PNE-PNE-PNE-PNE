#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Projeto Final ")

# Menu horizontal
selected = option_menu(
    menu_title="Monitoramento das Metas PNE (Plano Nacional de Educação)",
    options=["Home", "Plano Nacional de Educação", "Disponibilização de Dados", "Divisão das funções"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Header
if selected == "Home":
    st.header("Objetivo do projeto")
    st.subheader("Monitoramento das Metas da PNE")
    st.write("Realizar o acompanhamento das metas do Plano Nacional de Educação (PNE) por meio de análises estatísticas e democratizar o acesso aos seus dados. ")
    
if selected == "Plano Nacional de Educação":
    st.header("O que é a PNE (Plano Nacional de Educação)")
    st.subheader("O Plano Nacional de Educação (PNE) é uma Lei Federal nº 13.005/2014 com vigência decenal, que foi implementada no governo Dilma. Está de acordo com o artigo 214 da constituição. Suas diretrizes são:")
    st.write("I - erradicação do analfabetismo")
    st.write("II - universalização do atendimento escolar")
    st.write("III - melhoria da qualidade do ensino")
    st.write("V - promoção humanística, científica e tecnológica do País.")
    st.write("VI - estabelecimento de meta de aplicação de recursos públicos em educação como proporção do produto interno bruto. (Incluído pela Emenda Constitucional nº 59, de 2009)")

if selected == "Disponibilização de Dados":
    st.subheader("As cinco estrelas dos dados abertos: ⭐ ⭐ ⭐ ⭐ ⭐")
    st.write("Em 2010, o cientista britânico Tim Berners-Lee, inventor da Web, formulou um sistema de estrelas para encorajar a sociedade, especialmente guardiões de dados governamentais, a abrirem seus dados. O sistema ajuda a diagnosticar o nível de abertura de dados dos órgãos públicos e fornece degraus alcançáveis para se chegar a níveis cada vez mais refinados de dados abertos.")
    st.write("⭐ Publicar bases na Web (em qualquer formato) com licença aberta")
    st.write("⭐ ⭐ Publicar bases em formato estruturado com licença aberta (ex: arquivo Excel, em vez de imagem escaneada)")
    st.write("⭐ ⭐ ⭐ Usar formatos não proprietários e uma licença aberta (ex: arquivo CSV em vez de Excel)")
    st.write("⭐ ⭐ ⭐ ⭐ Usar URLs para descrever coisas, para que qualquer um possa identificá-las")
    st.write("⭐ ⭐ ⭐ ⭐ ⭐ Conectar seus dados a outras bases para dar contexto ")

if selected == "Divisão das funções":
    st.header("Divisão das funções")
    st.subheader("Coleta dos Dados")
    st.write("Coletamos os Dados de bases públicas não estruturadas disponibilizadas pelo governo")
    st.subheader("Estrutura unificada")
    st.write("Dividimos entre os membros do grupo as 20 metas para serem estruturadas e unificadas em um csv")
    st.subheader("Construção do Dashboard e Site")
    st.write("Sumarizamos os Dados coletados em um Dashboard interativo")
    st.write("[Flourish](https://public.flourish.studio/visualisation/11496831/)")


# %%
