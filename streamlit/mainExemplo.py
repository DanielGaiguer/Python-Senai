import streamlit as st
import datetime
import json

# criando os arquivos json p/ salvar os dados
def carregar_dados():
    try:
        with open("catalogo.json", "r") as arquivo:
            st.session_state.catalogo_produtos = json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        st.session_state.catalogo_produtos = {}

    try:
        with open("historico_vendas.json", "r") as arquivo:
            st.session_state.historico_vendas = json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        st.session_state.historico_vendas = []

def salvar_dados():
    with open("catalogo.json", "w") as arquivo:
        json.dump(st.session_state.catalogo_produtos, arquivo, indent=4)
    with open("historico_vendas.json", "w") as arquivo:
        json.dump(st.session_state.historico_vendas, arquivo, indent=4)

# Visual do Streamlit
st.title("🏪 Gerenciador e Calculadora de Vendas")

# iniciar o estado da sessão se ainda não foi iniciado
if 'catalogo_produtos' not in st.session_state:
    carregar_dados()

##menu principal
tab1, tab2, tab3 = st.tabs(["Cadastrar Produto", "Realizar Venda", "Visualizar Dados"])

with tab1:
    st.header("Cadastrar Produto")
    nome = st.text_input("Nome do Produto:")
    preco = st.number_input("Preço:")
    estoque = st.number_input("Quantidade em Estoque:", step=1)
    if st.button("Cadastrar"):
        if nome and preco and estoque > 0:
            st.session_state.catalogo_produtos[nome]={"preco": preco, "estoque": estoque}
            salvar_dados()
            st.success(f"Produto '{nome}' cadastrado com sucesso!")
        else:
            st.error("Preencha todos os campos corretamente.")

with tab2:
    st.header("Realizar Venda")
    if not st.session_state.catalogo_produtos:
        st.info("Nenhum produto cadastrado")
    else:
        produto_nomes = list(st.session_state.catalogo_produtos.keys())
        nome_produto = st.selectbox("Selecione o Produto:", produto_nomes)
        qtd = st.number_input("Quantidade:", step=1)
        if st.button("Finalizar Venda"):
            if nome_produto in st.session_state.catalogo_produtos and qtd > 0:
                if st.session_state.catalogo_produtos[nome_produto]["estoque"] >= qtd:
                    total = st.session_state.catalogo_produtos[nome_produto]["preco"] * qtd
                    st.session_state.catalogo_produtos[nome_produto]["estoque"] -= qtd
                    venda = {
                        "produto": nome_produto,
                        "quantidade": qtd,
                        "total": total,
                        "data": str(datetime.datetime.now())
                    }
                    st.session_state.historico_vendas.append(venda)
                    salvar_dados()
                    st.success(f"Venda de {qtd} '{nome_produto}' realizada. Total: R$ {total:.2f}")
                else:
                    st.error("Estoque insuficiente!")
            else:
                st.error("Produto não selecionado ou quantidade inválida.")
with tab3:
    st.header("Visualizar Dados")
    if st.button("Ver Catálogo de Produtos"):
        produtos_para_exibir = []
        for nome, dados in st.session_state.catalogo_produtos.items():
            produtos_para_exibir.append({
                "Produto": nome,
                "Preço": dados['preco'],
                "Estoque": dados['estoque']
            })

        if produtos_para_exibir:
            st.dataframe(produtos_para_exibir, use_container_width=True)
        else:
            st.info("Nenhum produto cadastrado.")

    if st.button("Ver histórico de vendas"):
        st.dataframe(st.session_state.historico_vendas)