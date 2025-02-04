import streamlit as st

# Variables globales para almacenar hábitos
if "habitos" not in st.session_state:
    st.session_state.habitos = []

def crear_habito():
    """Pantalla para crear un nuevo hábito"""
    st.title("📅 Crear Nuevo Hábito")

    # Nombre del hábito
    habit_name = st.text_input("¿Qué hábito deseas crear?", "")

    # Selección de días de la semana
    st.write("Selecciona los días de la semana para realizar tu hábito:")
    days_of_week = ["L", "M", "X", "J", "V", "S", "D"]
    selected_days = []

    # Crear botones para seleccionar los días
    for day in days_of_week:
        if st.button(day, key=day):
            selected_days.append(day)

    # Sanción
    sanction = st.text_area("Escribe una sanción si no realizas el hábito:")

    # Aceptar y guardar el hábito
    if st.button("Aceptar"):
        if habit_name and selected_days and sanction:
            new_habit = {
                "name": habit_name,
                "days": selected_days,
                "sanction": sanction
            }
            st.session_state.habitos.append(new_habit)
            st.success(f"✅ Hábito '{habit_name}' creado con éxito!")
            st.experimental_rerun()  # Recargar para pasar a la siguiente pantalla
        else:
            st.error("❌ Por favor, completa todos los campos")

# Llamar a la función para crear un hábito
crear_habito()

