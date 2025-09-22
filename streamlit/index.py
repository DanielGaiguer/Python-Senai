import streamlit as st
import datetime
import json

def carregar_dados():
    try:
        with open("agendamento.json", "r") as arquivo:
            st.session_state.agendamento = json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        st.session_state.agendamento = {}

def salvar_dados():
    with open("agendamento.json", "w") as arquivo:
        json.dump(st.session_state.agendamento, arquivo, indent=4, default=str)

if 'agendamento' not in st.session_state:
    carregar_dados()

if "editando" not in st.session_state:
    st.session_state.editando = None

if "excluindo" not in st.session_state:
    st.session_state.excluindo = None


st.title("Agendamento de compromissos")

tab1, tab2 = st.tabs(["Agendar", "Ver agendamentos"])


with tab1:
    st.header("Agendar compromisso")
    nome = st.text_input("Nome da pessoa:")
    data = st.date_input("Data do compromisso:", min_value=datetime.date.today())
    horario = st.time_input("Horário do compromisso:")
    descricao = st.text_area("Descrição do compromisso (Opcional): ")
    local = st.text_input("Local do compromisso (Opcional): ")
    observacoes = st.text_area("Observações Gerais (Opcional): ")
    if st.button("Agendar", key="Agendar"):
        if nome and data and horario :
            st.session_state.agendamento[nome] = {"nome": nome, "data": data, "horario": horario, "descricao": descricao, "local": local, "observacoes": observacoes}
            salvar_dados()
            st.success(f"Agendamento para '{nome}' agendado com sucesso!")
        else:
            st.error("Preencha todos os campos corretamente.")

with tab2:
    st.header("Ver agendamentos")
    if 'agendamento' not in st.session_state:
        st.info("Nenhum agendamento marcado")
    else:
        i = 0
        for i, (nome, dados) in enumerate(st.session_state.agendamento.items()):
            agendamento_exibir = []
            mais_exibir = []
            agendamento_exibir.append({
                "Nome": nome,
                "Data": dados['data'],
                "Horário": dados['horario'],
            })

            if agendamento_exibir: 
                st.dataframe(agendamento_exibir, use_container_width=True)
            else:
                st.info("Nenhum Agendamento atual")
                
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("Ver mais", key=f"vermais_{i}"):
                    mais_exibir.append({
                        "Descrição": dados.get("descricao", "Descrição vazia"),
                        "Local": dados.get("local", "Local vazio"),
                        "Observações": dados.get("observacoes", "Observações vazias")
                    });

                    if agendamento_exibir and mais_exibir:
                        st.dataframe(mais_exibir, use_container_width=True)
            
            with col2:
                if st.button("Editar Informações", key=f"Editar_{i}"):
                    st.session_state.editando = nome
                
                #nome_edit = st.text_input("Nome da pessoa:", value=f"{nome}")
                #data_edit = st.date_input("Data do compromisso:", min_value=datetime.date.today(), value=f"{dados['data']}")
                #horario_edit = st.time_input("Horário do compromisso:", value=f"{dados['horario']}")
                #descricao_edit = st.text_area(
                #    "Descrição do compromisso (Opcional): ", 
                #    value=f"{dados.get('descricao', 'Descrição vazia')}",
                #    key=f"descricao_edit_{i}"
                #)
                #local_edit = st.text_input(
                #    "Local do compromisso (Opcional): ", 
                #    value=f"{dados.get('local', 'Local vazio')}",
                #    key=f"local_edit_{i}"
                #    )
                #observacoes_edit = st.text_area(
                #    "Observações Gerais (Opcional): ",
                #    value=f"{dados.get('observacoes', 'Observações vazias')}",
                #    key=f"observacoes_edit_{i}"
                #    )
                #if st.button("Editar", key=f"Confirmar_{i}"):
                #    if nome_edit and data_edit and horario_edit :
                #        st.session_state.agendamento[nome] = {"nome": nome_edit, "data": data_edit, "horario": horario_edit, "descricao": descricao_edit, "local": local_edit, "observacoes": observacoes_edit}
                #        salvar_dados()
                #        st.success(f"Agendamento para '{nome}' agendado com sucesso!")
                #    else:
                #        st.error("Preencha todos os campos corretamente.")
                

            with col3:
                if st.button("Excluir Agendamento", key=f"Excluir_{i}"):
                    st.session_state.excluindo = nome

                #if st.button("Confirmar exclusão", key=f"Confirmar_excluir_{i}"):
                #    if nome:
                #        del st.session_state.agendamento[nome]
                #        salvar_dados()
                #        st.success(f"Agendamento para '{nome}' excluído com sucesso!")
                #    else:
                #        st.error("Erro ao tentar excluir agendamento.")

    if st.session_state.editando:
        nome = st.session_state.editando
        dados = st.session_state.agendamento[nome]
        nome_edit = st.text_input("Nome:", value=nome)
        data_edit = st.date_input("Data:", value=datetime.datetime.strptime(dados['data'], "%Y-%m-%d").date())
        horario_edit = st.time_input("Horário:", value=datetime.datetime.strptime(dados['horario'], "%H:%M:%S").time())
        descricao_edit = st.text_area("Descrição:", value=dados.get("descricao",""))
        local_edit = st.text_input("Local:", value=dados.get("local",""))
        observacoes_edit = st.text_area("Observações:", value=dados.get("observacoes",""))

        if st.button("Confirmar Edição"):
            del st.session_state.agendamento[nome]  # Remove antigo
            st.session_state.agendamento[nome_edit] = {
                "nome": nome_edit,
                "data": str(data_edit),
                "horario": str(horario_edit),
                "descricao": descricao_edit,
                "local": local_edit,
                "observacoes": observacoes_edit
            }
            st.session_state.editando = None
            salvar_dados()
            st.success("Agendamento atualizado!")


    if st.session_state.excluindo:
        nome = st.session_state.excluindo
        st.warning(f"Deseja realmente excluir {nome}?")
        if st.button("Confirmar exclusão"):
            del st.session_state.agendamento[nome]
            st.session_state.excluindo = None
            salvar_dados()
            st.success("Agendamento excluído!")
