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
    st.session_state.page = "login"  # Asegurarse de que se inicie en la pantalla de login

# Fondo con la imagen y el color de texto blanco
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/2908175/pexels-photo-2908175.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
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

# Función de inicio de sesión
def login():
    """Función para manejar el inicio de sesión"""
    st.title(" Inicio de Sesión")

    # Campos de inicio de sesión
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón de iniciar sesión
    if st.button("Iniciar sesión"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "crear_habito"  # Cambiar a la pantalla de crear hábito
        else:
            st.error("Usuario o contraseña incorrectos")

# Función para la pantalla de crear hábito
# Función para la pantalla de crear hábito
def crear_habito():
    """Pantalla para crear hábitos"""
    st.title("Crear un Hábito")
    
    # Campo para el nombre del hábito
    habit_name = st.text_input("Nombre del hábito")

    # Selección de días de la semana
    days_of_week = st.multiselect(
        "Selecciona los días de la semana",
        ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    )
    
    # Campo para la sanción
    sanction = st.text_input("Escribe una sanción en caso de no cumplir con el hábito")

    # Botones para guardar el hábito y ver mis hábitos
    col1, col2 = st.columns([3, 1])
    if col1.button("Aceptar"):
        st.session_state.habit_name = habit_name
        st.session_state.days_of_week = days_of_week
        st.session_state.sanction = sanction
        st.success(f"Hábito {habit_name} creado exitosamente!")
    
    if col2.button("Ver mis hábitos"):
        st.session_state.page = "dashboard"  # Cambiar a la pantalla de dashboard

# Control de flujo: Mostrar la pantalla correcta según el estado
if not st.session_state.logged_in:
    login()
elif st.session_state.page == "crear_habito":
    crear_habito()
elif st.session_state.page == "dashboard":
    # Aquí debes agregar la función para mostrar la pantalla de dashboard
    def dashboard():
        st.title("Dashboard")
        # Aquí debes agregar el código para mostrar los hábitos creados
        st.write("Hábitos creados:")
        st.write(st.session_state.habit_name)
        st.write(st.session_state.days_of_week)
        st.write(st.session_state.sanction)
    
    dashboard()
