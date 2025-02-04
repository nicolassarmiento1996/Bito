import streamlit as st

# Configuración de la sesión
if "habitos" not in st.session_state:
    st.session_state.habitos = []

def crear_habito():
    """Función para crear un nuevo hábito"""
    st.title("Crear Hábito")

    # Campo para el nombre del hábito
    nombre_habito = st.text_input("Nombre del hábito")

    # Campo para seleccionar los días de la semana
    dias_semana = st.multiselect("Días de la semana", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

    # Campo para la sanción
    sancion = st.text_input("Sanción en caso de no realizar el hábito")

    # Botón para aceptar
    if st.button("Aceptar"):
        # Agregar el hábito a la lista de hábitos
        st.session_state.habitos.append({
            "nombre": nombre_habito,
            "dias_semana": dias_semana,
            "sancion": sancion
        })
        st.success("Hábito creado exitosamente!")
        st.session_state.pantalla = "dashboard"
        st.experimental_rerun()  # Recargar la página para mostrar la siguiente pantalla

# Llamar a la función para crear un hábito
if st.session_state.pantalla == "crear_habito":
    crear_habito()
