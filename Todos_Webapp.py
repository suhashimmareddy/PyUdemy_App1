import streamlit as st

import Function_Todo_App
import Function_Todo_App as fta

Todos = fta.get_todos()

def add_todo():
    todo = st.session_state["New_Todo"]+'\n'
    Todos.append(todo)
    Function_Todo_App.write_todos(Todos)

st.title('Su''s Todo List Items:')
st.subheader('A Web-APP to track the tasks related to a project.')
st.write("Hello My Puny Humans Muhahahahahahahaha :)")

for index, todo in enumerate(Todos):
    x = st.checkbox(todo, key=todo)
    if x:
        Todos.pop(index)
        Function_Todo_App.write_todos(Todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = '', placeholder = 'Enter your todo item...', on_change=add_todo, key = "New_Todo")