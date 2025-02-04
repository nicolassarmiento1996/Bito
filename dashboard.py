import streamlit as st
import datetime

# Función de cierre de sesión
def logout():
    """Cerrar sesión"""
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.next_page = ""  # Limpiar la página a redirigir
    st.experimental_rerun()

# Mostrar el botón de cerrar sesión en la parte superior derecha
if st.session_state.logged_in:
    st.sidebar.button("Cerrar sesión", on_click=logout)

# Verificar si el usuario está autenticado
if not st.session_state.logged_in:
    st.write("Por favor, inicia sesión para continuar.")
else:
    st.title("📊 Dashboard de Hábitos")

    # Mostrar los hábitos registrados
    if "habits" in st.session_state and st.session_state.habits:
        for habit in st.session_state.habits:
            st.subheader(habit["habit_name"])
            st.write(f"Días seleccionados: {', '.join(habit['selected_days'])}")
            st.write(f"Sanción: {habit['penalty']}")

            # Mostrar progreso
            today = datetime.datetime.today().strftime('%A')[:1]  # Día de la semana en formato L, M, X...
            if today in habit['selected_days']:
                st.success(f"✔️ ¡Hoy estás cumpliendo con tu hábito!")
            else:
                st.warning(f"⚠️ Hoy no estás cumpliendo con este hábito.")

            st.write("---")

        # Agregar una función para resetear los hábitos o mostrar el progreso de todos
        if st.button("Ver progreso general"):
            st.write("🔄 Aquí se podría mostrar un gráfico de progreso similar a Strava.")
            # Esta es una idea para expandir con gráficos de barras o líneas usando la librería `matplotlib` o `plotly`.
    else:
        st.write("No tienes hábitos registrados aún.")
