import streamlit as st

# Simulación de usuarios registrados
USERS = {
    "admin": "1234",
    "usuario1": "contraseña123",
}

# Configuración de la sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

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

def login():
    """Función para manejar el inicio de sesión"""
    st.title("🔐 Inicio de Sesión")

    # Campos de inicio de sesión
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón de iniciar sesión con HTML para cambiar el color
    if st.button("Iniciar sesión"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"✅ Bienvenido, {username}!")
            st.session_state.next_page = "crear_habito"  # Indicamos que la siguiente página es la de creación de hábitos
            st.experimental_rerun()  # Recargar la página para mostrar la siguiente pantalla
        else:
            st.error("❌ Usuario o contraseña incorrectos")

def logout():
    """Función de cierre de sesión"""
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.next_page = ""  # Limpiamos la página a redirigir
    st.experimental_rerun()

# Agregar un botón de cerrar sesión en la parte superior derecha
if st.session_state.logged_in:
    st.sidebar.button("Cerrar sesión", on_click=logout)

# Control de flujo: Mostrar la pantalla de login si no está autenticado
if not st.session_state.logged_in:
    login()
else:
    # Verificar la página que se debe mostrar según el flujo
    if st.session_state.next_page == "crear_habito":
        st.experimental_rerun()  # Redirige a la página de creación de hábitos
    else:
        st.write("Redirigiendo a la página de creación de hábitos...")
        st.experimental_rerun()
