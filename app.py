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
    st.session_state.pantalla = "login"
    st.session_state.habitos = []

# Fondo con la imagen y el color de texto blanco
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/13904988/pexels-photo-13904988.jpeg?auto=compress&cs=tinysrgb&w=600");
    background-size: cover;
    color: white;  /* Establecer color blanco para el texto */
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

.stButton > button {
    color: black; /* Establecer color negro para el texto de los botones */
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def login():
    """Función para manejar el inicio de sesión"""
    st.title(" Inicio de Sesión")

    # Campos de inicio de sesión
    with st.form("login_form"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submit_button = st.form_submit_button("Iniciar sesión", use_container_width=True)

        if submit_button:
            if username in USERS and USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.pantalla = "crear_habito"
            else:
                st.error("Usuario o contraseña incorrectos")

def crear_habito():
    """Función para crear un nuevo hábito"""
    st.title("Crear Hábito")

    # Campo para el nombre del hábito
    with st.form("crear_habito_form"):
        nombre_habito = st.text_input("Nombre del hábito")
        dias_semana = st.multiselect("Días de la semana", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
        sancion = st.text_input("Sanción en caso de no realizar el hábito")
        submit_button = st.form_submit_button("Aceptar", style="color:black")

        if submit_button:
            # Agregar el hábito a la lista de hábitos
            st.session_state.habitos.append({
                "nombre": nombre_habito,
                "dias_semana": dias_semana,
                "sancion": sancion
            })
            st.success("Hábito creado exitosamente!")
            st.session_state.pantalla = "dashboard"

def dashboard():
    """Función para mostrar el dashboard de hábitos"""
    st.title("Dashboard de Hábitos")

    # Mostrar la lista de hábitos
    for i, habito in enumerate(st.session_state.habitos):
        st.write(f"Hábito {i+1}: {habito['nombre']}")
        st.write(f"Días de la semana: {', '.join(habito['dias_semana'])}")
        st.write(f"Sanción: {habito['sancion']}")
        st.write("---")

    # Botón para crear un nuevo hábito
    with st.form("dashboard_form"):
        submit_button = st.form_submit_button("Crear Hábito", style="color:black")

        if submit_button:
            st.session_state.pantalla = "crear_habito"

    # Botón para cerrar sesión
    with st.form("cerrar_sesion_form"):
        submit_button = st.form_submit_button("Cerrar sesión", style="color:black")

        if submit_button:
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.pantalla = "login"

def main():
    if st.session_state.pantalla == "login":
        login()
    elif st.session_state.pantalla == "crear_habito":
        crear_habito()
    elif st.session_state.pantalla == "dashboard":
        dashboard()

if __name__ == "__main__":
    main()
