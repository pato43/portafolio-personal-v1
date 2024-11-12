import streamlit as st
from pathlib import Path

# Paleta de colores, estilos CSS y animaciones avanzadas
st.markdown(
    """
    <style>
        /* Fondo y estilo general */
        .main {background-color: #1c1c1c; color: #FFFFFF; font-family: 'Arial', sans-serif;}

        /* Diseño y animaciones de botones */
        .stButton>button, .stDownloadButton>button {
            color: #FFFFFF; background-color: #0055a2; border-radius: 8px; padding: 12px;
            transition: all 0.3s ease; font-weight: bold; border: none;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #003366; transform: scale(1.07);
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.5);
        }

        /* Encabezados y texto con efectos de animación */
        .section-header {
            font-size: 28px; font-weight: bold; color: #00aaff; margin-top: 20px;
            animation: slideIn 1s ease-out;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .content {
            font-size: 18px; color: #CCCCCC;
            animation: fadeIn 1.5s ease-in;
        }

        /* Imagen redonda de la barra lateral */
        .sidebar-image {
            border-radius: 50%; width: 140px; height: 140px; display: block; margin: 0 auto 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease;
        }
        .sidebar-image:hover {
            transform: scale(1.05);
        }

        /* Animaciones */
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        @keyframes slideIn {
            from {transform: translateX(-50px); opacity: 0;}
            to {transform: translateX(0); opacity: 1;}
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Barra lateral con imagen redonda y detalles de contacto
st.sidebar.title("Alexander Eduardo Rojas Garay")
st.sidebar.image("WhatsApp Image 2024-10-23 at 7.23.55 PM(1)_upscayl_6x_realesrgan-x4plus.png", width=140, caption="Data Scientist | Matemático y Físico")

# Información de contacto
st.sidebar.markdown("**📍 Ubicación:** CDMX")
st.sidebar.markdown("**📞 Teléfono:** 722-559-7963")
st.sidebar.markdown("**📧 Correo:** rojasalexander10@gmail.com")

# Botones de descarga de CV en español e inglés
cv_es_path = "files/CV-AlexanderEduardoRojasGaray.pdf"
cv_en_path = "files/CV-AlexanderEduardoRojasGaray-EN.pdf"

# Mostrar botón para el CV en Español si el archivo existe
if Path(cv_es_path).is_file():
    with open(cv_es_path, "rb") as pdf_es:
        st.sidebar.download_button(label="📄 Descargar CV en Español", data=pdf_es, file_name="CV-AlexanderEduardoRojasGaray.pdf", mime="application/pdf")
else:
    st.write("Archivo de CV en Español no encontrado.")

# Mostrar botón para el CV en Inglés si el archivo existe
if Path(cv_en_path).is_file():
    with open(cv_en_path, "rb") as pdf_en:
        st.sidebar.download_button(label="📄 Download CV in English", data=pdf_en, file_name="CV-AlexanderEduardoRojasGaray-EN.pdf", mime="application/pdf")
else:
    st.write("Archivo de CV en Inglés no encontrado.")

# Enlace a LinkedIn en la barra lateral
st.sidebar.markdown("[🌐 Visita mi LinkedIn](https://www.linkedin.com/in/alexander-eduardo-rojas-garay-b17471235)", unsafe_allow_html=True)

# Tabs para la navegación
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Inicio", "Experiencia", "Educación", "Certificaciones", "Habilidades", "Proyectos", "Publicaciones"])

# Sección de inicio
with tab1:
    st.title("Alexander Eduardo Rojas Garay")
    st.image("WhatsApp Image 2024-10-23 at 7.23.55 PM(1).jpeg", width=200)
    st.markdown("## Data Scientist | Analista de Datos")
    st.write("Apasionado por el análisis y la ciencia de datos, con experiencia en machine learning y modelado predictivo. Me especializo en Python, SQL, y herramientas de visualización de datos como Looker Studio. Tengo un enfoque en soluciones basadas en datos, contribuyendo a resolver problemas complejos en áreas diversas.")

# Sección de Experiencia Profesional
with tab2:
    st.markdown("<div class='section-header'>Experiencia Profesional</div>", unsafe_allow_html=True)
    st.write("**Instituto de Matemáticas (UNAM) - Data Scientist**")
    st.write("Desarrollo de modelos de machine learning para proyectos complejos, aplicando técnicas avanzadas de análisis estadístico en investigación.")
    st.write("• Optimización de modelos predictivos mediante TensorFlow y scikit-learn para soportar decisiones estratégicas.")
    
    st.write("**Colmena Space (UNAM) - Machine Learning Engineer**")
    st.write("Responsable de crear modelos de predicción y simulación para optimizar trayectorias de sondas lunares, mejorando la eficiencia en planificación de misiones.")
    st.write("• Trabajo en la nube con AWS y Azure para escalar soluciones de machine learning y garantizar la eficiencia de cálculo.")

    st.write("**Asociación Aeroespacial de la Facultad de Ingeniería (UNAM) - Analista de Datos**")
    st.write("Análisis y visualización de datos experimentales para optimizar resultados en lanzamientos de cohetes, utilizando Python y herramientas numéricas.")
    st.write("• Implementación de análisis estadísticos para mejorar la precisión de experimentos en lanzamientos.")

    st.write("**Freelancer - Desarrollador Web**")
    st.write("Desarrollo de plataformas web dinámicas y optimización para sitios de proyectos tecnológicos y comerciales.")
    st.write("• Proyectos destacados incluyen el desarrollo de infrax.mx, Tecistem.com, y masmigrar.com.")

# Sección de Educación
with tab3:
    st.markdown("<div class='section-header'>Educación</div>", unsafe_allow_html=True)
    st.write("**Licenciatura en Física y Matemáticas - Universidad Nacional Autónoma de México (UNAM)** (2019 - 2024)")
    st.write("Formación sólida en física teórica y aplicada, análisis matemático, álgebra y programación. Participación en proyectos de investigación, utilizando habilidades cuantitativas y analíticas para resolver problemas complejos.")

# Sección de Certificaciones
with tab4:
    st.markdown("<div class='section-header'>Certificaciones y Cursos</div>", unsafe_allow_html=True)
    st.write("• **Certificado en Ciencia de Datos** - Microsoft")
    st.write("• **Certificado en Análisis de Datos** - Microsoft")
    st.write("• **Certificado en SQL y Azure** - Microsoft")
    st.write("• **Certificado en Data Driven Astronomy** - UNAM")
    st.write("• **Certificado en Python** - Microsoft")
    st.write("• **Certificado en Python y Análisis de Datos** - Santander")

# Sección de Habilidades Técnicas
with tab5:
    st.markdown("<div class='section-header'>Habilidades Técnicas</div>", unsafe_allow_html=True)
    st.write("Lenguajes de programación: Python, SQL, C++, JavaScript")
    st.write("Bibliotecas: numpy, pandas, matplotlib, seaborn, TensorFlow, PyTorch, scikit-learn, PySpark")
    st.write("Bases de datos: SQL, MongoDB, Cassandra")
    st.write("Visualización de datos: Looker Studio, matplotlib, seaborn")
    st.write("Cloud Computing: AWS, Azure")

# Sección de Proyectos Destacados
with tab6:
    st.markdown("<div class='section-header'>Proyectos Destacados</div>", unsafe_allow_html=True)
    st.write("🔍 **Predicciones de las Elecciones de EE. UU. 2024 usando Machine Learning**")
    st.write("Análisis de resultados en estados clave con técnicas de ajuste de tendencias, momentum y promedios de encuestas.")
    st.write("[Ver proyecto completo](https://lnkd.in/e7DrEZEE)")
    
    st.write("🔬 **El Nobel de Física 2024: Inteligencia Artificial y Física Computacional en Materiales 2D**")
    st.write("Investigación sobre la aplicación de Machine Learning y modelado en materiales bidimensionales para el diseño de semiconductores.")
    st.write("[Ver publicación completa](https://lnkd.in/e6q5QQfg)")
    
    st.write("🔗 **Aplicación de Predicción de Enfermedades Dentales**")
    st.write("Desarrollo de un sistema de reconocimiento de anomalías en radiografías panorámicas con YOLO V5 y Flask.")
    st.write("[Ver detalles del proyecto](https://github.com/usuario/dental-disease-detection)")

# Sección de Publicaciones
with tab7:
    st.markdown("<div class='section-header'>Publicaciones</div>", unsafe_allow_html=True)
    st.write("📄 **Paper sobre Machine Learning en Física Experimental**")
    st.write("Aplicaciones de machine learning en física experimental, explorando algoritmos de predicción en fenómenos cuánticos.")

