import streamlit as st

# Configuración de la sesión
if "habitos" not in st.session_state:
    st.session_state.habitos = []

# Fondo con la imagen y el color de texto blanco
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/foto-gratis/personas-que-toman-clases-pilates-reformador_23-2151093272.jpg?t=st=1738638246~exp=1738641846~hmac=c98b8738e3217cfda46863036a62ca7f8745ab9d61d03d3e99de187a0da9ea6a&w=2000");
    background-size: cover;
    color: white;  /* Establecer color blanco para el texto */
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

h1, h2, h3, h4, h5, h6, p {
    color: white; /* Asegura que todos los textos sean blancos */
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def crear_habito():
    st.title("📝 Crear un Nuevo Hábito")

    # Nombre del hábito
    nombre_habito = st.text_input("Nombre del hábito")

    # Días de la semana
    dias_semana = st.multiselect(
        "Selecciona los días de la semana",
        options=["L", "M", "X", "J", "V", "S", "D"],
        default=["L", "M", "X", "J", "V"]
    )

    # Sanción en caso de no cumplir
    sancion = st.text_input("Sanción en caso de no cumplir")

    # Botón para guardar el hábito
    if st.button("Aceptar"):
        if nombre_habito and dias_semana and sancion:
            nuevo_habito = {
                "nombre": nombre_habito,
                "dias": dias_semana,
                "sancion": sancion,
                "progreso": 0  # Inicializar progreso en 0
            }
            st.session_state.habitos.append(nuevo_habito)
            st.success("¡Hábito creado exitosamente!")
        else:
            st.error("Por favor, completa todos los campos.")

    # Botón para volver al home
    if st.button("Volver al Inicio"):
        st.session_state.current_page = "home"
        st.experimental_rerun()

# Mostrar la pantalla de creación de hábitos
crear_habito()
