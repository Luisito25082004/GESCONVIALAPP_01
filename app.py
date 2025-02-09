import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(page_title="Perfil Ingeniero Civil", layout="wide")

    # Barra lateral con información adicional
    with st.sidebar:
        # st.image("https://via.placeholder.com/200", caption="Ingeniero Civil", use_column_width=True)
        st.markdown("## Contacto")
        st.markdown("📧 Email: luisenriquesanchezvelasquez@gmail.com")
        st.markdown("📞 Teléfono: +51 976421668")
        st.markdown("🔗 [LinkedIn](https://linkedin.com)")

    # Título principal
    st.title("👷 Perfil Profesional - Ingeniero Civil")
    st.write("Especializado en diseño estructural, gestión de proyectos y consultoría.")

    # Sección de Proyectos
    st.header("🏗️ Proyectos Destacados")
    col1, col2 = st.columns(2)

    with col1:
        # st.image("https://via.placeholder.com/400", caption="Proyecto 1 - Edificio Comercial")
        st.write("Diseño y cálculo estructural para un edificio de 10 pisos.")

    with col2:
        # st.image("https://via.placeholder.com/400", caption="Proyecto 2 - Puente Vehicular")
        st.write("Supervisión y ejecución de un puente de 100 metros de longitud.")

    # Sección de Habilidades
    st.header("🛠️ Habilidades Técnicas")
    with st.expander("Ver habilidades"):
        st.markdown("""
        - Diseño estructural y análisis de cargas
        - Supervisión de obras civiles
        - Modelado con software como SAP2000, ETABS y AutoCAD
        - Gestión de proyectos con metodología PMI
        - Evaluación de suelos y cimentaciones
        """)

    # Sección de Cálculo Estructural
    st.header("📐 Cálculo de Carga en Viga Simple")
    st.write("Ingrese los datos para calcular el momento flector máximo en una viga simplemente apoyada.")
    
    carga = st.number_input("Carga en kN/m", min_value=0.0, step=0.1, value=10.0)
    longitud = st.number_input("Longitud de la viga (m)", min_value=1.0, step=0.5, value=5.0)
    momento_max = (carga * longitud ** 2) / 8

    st.success(f"💡 El momento flector máximo es: **{momento_max:.2f} kN·m**")

    # Formulario de Contacto
    st.header("📩 Contacto")
    with st.form("contact_form"):
        nombre = st.text_input("Nombre")
        email = st.text_input("Correo Electrónico")
        mensaje = st.text_area("Mensaje")
        enviado = st.form_submit_button("Enviar")

        if enviado:
            if nombre and email and mensaje:
                st.success(f"¡Gracias {nombre}! Me pondré en contacto contigo pronto.")
            else:
                st.error("Por favor, complete todos los campos.")

if __name__ == "__main__":
    main()