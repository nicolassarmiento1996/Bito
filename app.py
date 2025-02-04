import streamlit as st

st.title("📅 Habit Tracker")

habit = st.text_input("Escribe un hábito que quieres seguir:")

if st.button("Agregar hábito"):
    st.success(f"¡'{habit}' agregado!")
