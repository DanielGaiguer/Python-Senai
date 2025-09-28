import streamlit as st
import datetime
import json

def carregar_alunos():
    try:
        with open("alunos.json", "r") as arquivo:
            st.session_state.alunos = json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        st.session_state.alunos = {}

def carregar_turmas():
    try:
        with open("turmas.json", "r") as arquivo:
            st.session_state.turmas = json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        st.session_state.turmas = {}

def salvar_alunos():
    with open("alunos.json", "w") as arquivo:
        json.dump(st.session_state.alunos, arquivo, indent=4, default=str)

def salvar_turmas():
    with open("turmas.json", "w") as arquivo:
        json.dump(st.session_state.turmas, arquivo, indent=4, default=str)

if 'turmas' not in st.session_state:
    carregar_turmas()

if 'alunos' not in st.session_state:
    carregar_alunos()

if "notas" not in st.session_state:
    st.session_state.notas = []


st.session_state.next_id = 0
aluno_id = st.session_state.next_id 
st.session_state.next_id += 1

st.title("Bem vindo ao Gerenciador de Alunos")


##menu principal
tab1, tab2, tab3, tab4 = st.tabs(["Cadastrar Aluno", "Gerenciar Turmas", "Visualizar Turma", "Estatísticas da Turma"])

with tab1: 
    col1, col2 = st.columns(2) 
    with col1: 
        nome = st.text_input("Nome do Aluno")
        idade = st.number_input("Idade do Aluno", step=1, min_value=0)
        email = st.text_input("Email do Aluno")
        telefone = st.text_input("Telefone do Aluno")
    
    with col2: 
        turma = st.selectbox("Turma do Aluno", st.session_state.turmas["turmas"])
        materia = st.text_input("Materia do Aluno")
        nota = st.number_input("Adicione as notas do Aluno", format="%0.2f", min_value=0.00, max_value=10.00, step=0.10)
        col3, col4 = st.columns(2)
        with col3:
            if st.button("Adicionar nota", key="addNota"):
                st.session_state.notas.append(nota)
                st.info(f"Notas adicionadas: {st.session_state.notas}")
        with col4:
            if st.button("Apagar Notas", key="delNotas"):
                st.session_state.notas = []


    if st.button("Salvar Aluno", key="addAluno"):
        if nome and idade and email and telefone and turma and materia and len(st.session_state.notas) > 0:
            st.session_state.alunos[aluno_id] = { "Id": aluno_id, "nome": nome, "idade": idade, "email": email, "telefone": telefone, "turma": turma, "materia": materia, "notas": st.session_state.notas}
            salvar_alunos()
            st.success(f"Aluno {nome} cadastrado com sucesso.")
        else:
            st.error("Erro ao cadastrar aluno, preencha todos os campos corretamente.")

with tab2:
    
    st.subheader("Turmas")
    if st.session_state.turmas["turmas"]:
        select_turma = st.radio("Turmas cadastradas:", st.session_state.turmas["turmas"])
    else:
        st.info("Nenhuma turma cadastrada no momento")
    if st.button("Apagar Turma Selecionada", key="delTurma"):
        st.session_state.turmas["turmas"].remove(select_turma)  # remove pelo nome
        salvar_turmas()
        st.rerun()
        st.success(f"Turma {select_turma} apagada com sucesso!")

    turma = st.text_input("Deseja adicionar uma turma?", key="novaTurma")
    if st.button("Adicionar nova turma", key="addTurma"):
        if turma:
            if turma in st.session_state.turmas["turmas"]:
                st.info(f"Turma {turma} já existente")
            else:
                st.session_state.turmas["turmas"].append(turma)
                salvar_turmas()
                st.rerun()
                st.success(f"Turma {turma} adicionada com sucesso!")

with tab3:
    st.subheader("Visualizar Alunos")
    select_turma = st.selectbox("Turma", st.session_state.turmas["turmas"])
    
    for aluno_id, aluno in st.session_state.alunos.items():
        if aluno["turma"] == select_turma:
            st.dataframe([aluno])  

with tab4:
    alunos = 0
    soma = 0
    somaIdade = 0
    st.subheader("Estatistícas")
    select_turma = st.selectbox("Turma", st.session_state.turmas["turmas"], key="selectTab4")
    for aluno_id, aluno in st.session_state.alunos.items():
        if aluno["turma"] == select_turma:
            for nota in aluno["notas"]:
                somaNota = nota / len(aluno["notas"])
                soma += somaNota
            alunos += 1
            somaIdade += aluno["idade"]
    
    st.subheader(f"A média de notas da turma é: {soma / alunos:.2f}")
    st.subheader(f"Quantidade de alunos na turma: {alunos}")
    st.subheader(f"Média de idade dos alunos: {int(somaIdade / alunos)}")