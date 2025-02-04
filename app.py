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

# Agregar fondo de gradiente con CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to bottom, #A8D0E6, #FFFFFF); /* Azul pastel a blanco */
        height: 100vh;
        color: black;   /* Color de texto negro para mayor legibilidad */
    }
    .sidebar-content {
        background: rgba(0, 0, 0, 0.5);  /* Fondo oscuro para la barra lateral */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def login():
    """Función para manejar el inicio de sesión"""
    st.title("🔐 Inicio de Sesión")

    # Campos de inicio de sesión
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón de iniciar sesión
    if st.button("Iniciar sesión"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"✅ Bienvenido, {username}!")
            st.experimental_rerun()  # Recargar la página para mostrar la siguiente pantalla
        else:
            st.error("❌ Usuario o contraseña incorrectos")

def home():
    """Pantalla principal después de iniciar sesión"""
    st.title(f"🎉 Bienvenido {st.session_state.username}")
    st.write("¡Has iniciado sesión exitosamente!")

    if st.button("Cerrar sesión"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()

# Control de flujo: Mostrar la pantalla de login si no está autenticado
if not st.session_state.logged_in:
    login()
else:
    home()
