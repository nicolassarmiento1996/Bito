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

def dashboard():
    """Pantalla de Dashboard para visualizar los hábitos registrados"""
    st.title("📊 Dashboard de Hábitos")

    # Si no hay hábitos, mostrar mensaje
    if not st.session_state.habitos:
        st.write("No tienes hábitos registrados aún.")
    else:
        # Mostrar todos los hábitos
        for habit in st.session_state.habitos:
            st.write(f"**Hábito**: {habit['name']}")
            st.write(f"**Días**: {', '.join(habit['days'])}")
            st.write(f"**Sanción**: {habit['sanction']}")
            st.write("---")

            # Simular progreso de hábitos (por ejemplo, porcentaje de días cumplidos)
            st.progress(50)  # Aquí puedes hacer que el progreso sea dinámico

    if st.button("Crear nuevo hábito"):
        st.session_state.logged_in = False
        st.experimental_rerun()  # Regresar a la pantalla de creación de hábito

# Control de flujo: Mostrar la pantalla de creación de hábito si no hay hábitos creados
if not st.session_state.habitos:
    crear_habito()
else:
    dashboard()
