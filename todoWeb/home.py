import streamlit as st
import functions


todos = functions.get_todos()
st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("A Todo App")
st.subheader("This is a simple todo app")
st.write("This app is to increase your <b>productivity.</b>", unsafe_allow_html=True)

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

# st.session_state


# to run this file, run the command
# streamlit run [path and file name]
# example:
# streamlit run /home/duygu/PycharmProjects/pythonToDoApp/todoWeb/home.py
