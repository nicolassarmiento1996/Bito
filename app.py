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

# Agregar fondo de imagen de bienestar
st.markdown(
    """
    <style>
    .reportview-container {
        background: url('https://www.google.com/search?sca_esv=1e35dc1f4110e681&rlz=1C5CHFA_enCO942CO942&sxsrf=AHTn8zpmJA10yFRSSxYLxhQFrjt1IOXPiA:1738636667343&q=wellness&udm=2&fbs=ABzOT_BnMAgCWdhr5zilP5f1cnRvK9uZj3HA_MTJAA6lXR8yQBjuP0Gi2zaJk2jrCSzqvvc_CWluySj4hbIgcxtM4wLBGEbwvGyOm-Aff7Cd6CLXwRP9LJOKeow_-uywyq1awzcUMQDGRMYmvDY7H9EaZgcKs6clJoih7mAG5eoRjT2-Nmjfv8st6WbeslRwnMyPx92TqA3w0kNUcwI2k7yY33klsmd_BQ&sa=X&ved=2ahUKEwib58yn_qiLAxVhtYQIHXmONfEQtKgLegQIGRAB&biw=1680&bih=928&dpr=2#vhid=yHq_WOvrabL0eM&vssid=mosaic') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def login():
    """Función para manejar el inicio de sesión"""
    st.title("🔐 Inicio de Sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

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
