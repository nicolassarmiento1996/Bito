import streamlit as st

# Pantalla de Dashboard para visualizar los hábitos registrados
def dashboard():
    """Pantalla de Dashboard"""
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

# Llamar a la función de dashboard
dashboard()
