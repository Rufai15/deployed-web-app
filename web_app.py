import streamlit as st
import functions
todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("It's good to document your daily activities.")
st.write("The app is to help you structure your day.")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo", placeholder="Enter a new todo!",
              on_change=add_todo, key='new_todo')
