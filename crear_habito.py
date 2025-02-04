import streamlit as st

# Función de cierre de sesión
def logout():
    """Cerrar sesión"""
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.next_page = ""  # Limpiamos la página a redirigir
    st.experimental_rerun()

# Mostrar el botón de cerrar sesión en la parte superior derecha
if st.session_state.logged_in:
    st.sidebar.button("Cerrar sesión", on_click=logout)

# Verificar si el usuario está autenticado
if not st.session_state.logged_in:
    st.write("Por favor, inicia sesión para continuar.")
else:
    st.title("📝 Creación de Hábito")

    # Entrada del nombre del hábito
    habit_name = st.text_input("¿Cómo se llama tu hábito?")

    # Selección de días de la semana
    days_of_week = ["L", "M", "X", "J", "V", "S", "D"]
    selected_days = st.multiselect("Selecciona los días en los que vas a realizar este hábito:",
                                   days_of_week, default=["L"])

    # Entrada para la sanción
    penalty = st.text_area("¿Cuál será la sanción si no cumples el hábito?")

    # Botón para guardar
    if st.button("Aceptar"):
        if habit_name and selected_days and penalty:
            # Guardar los hábitos en el estado de sesión (para mantener los datos)
            if "habits" not in st.session_state:
                st.session_state.habits = []
            st.session_state.habits.append({
                "habit_name": habit_name,
                "selected_days": selected_days,
                "penalty": penalty
            })
            st.success("✅ ¡Hábito creado exitosamente!")
            st.session_state.next_page = "dashboard"  # Cambiar la página a dashboard
            st.experimental_rerun()  # Recargar la página para redirigir al dashboard
        else:
            st.error("❌ Todos los campos deben ser completados.")

    # Botón para redirigir al dashboard si ya se creó el hábito
    if st.button("Ver Dashboard"):
        st.session_state.next_page = "dashboard"
        st.experimental_rerun()  # Redirige al dashboard
