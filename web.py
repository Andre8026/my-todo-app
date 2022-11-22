import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my todo App")
st.write("This App will increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("", placeholder="Write here a new todo ...", on_change=add_todo, key="new_todo")

