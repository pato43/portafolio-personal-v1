import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

# Paleta de colores, estilos CSS y animaciones avanzadas
st.markdown(
    """
    <style>
        .main {background-color: #1c1c1c; color: #FFFFFF; font-family: 'Arial', sans-serif;}

        .stButton>button, .stDownloadButton>button {
            color: #FFFFFF; background-color: #0055a2; border-radius: 8px; padding: 12px;
            transition: all 0.3s ease; font-weight: bold; border: none;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #003366; transform: scale(1.07);
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.5);
        }

        .section-header {
            font-size: 36px; font-weight: bold; color: #00aaff; margin-top: 20px;
            animation: slideIn 1s ease-out;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.5);
        }

        .sidebar-image {
            border-radius: 50%; width: 180px; height: 180px; display: block; margin: 0 auto 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease;
        }
        .sidebar-image:hover {
            transform: scale(1.1);
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
st.sidebar.image("files/WhatsApp Image 2024-10-23 at 7.23.55 PM(1).jpeg", width=180, caption="Data Scientist | Matemático y Físico")

# Información de contacto
st.sidebar.markdown("**📍 Ubicación:** CDMX")
st.sidebar.markdown("**📞 Teléfono:** 722-559-7963")
st.sidebar.markdown("**📧 Correo:** rojasalexander10@gmail.com")

# Botones de descarga de CV en español e inglés
cv_es_path = "files/CV-AlexanderEduardoRojasGaray.pdf"
cv_en_path = "files/CV-AlexanderEduardoRojasGaray-EN.pdf"

if Path(cv_es_path).is_file():
    with open(cv_es_path, "rb") as pdf_es:
        st.sidebar.download_button(label="📄 Descargar CV en Español", data=pdf_es, file_name="CV-AlexanderEduardoRojasGaray.pdf", mime="application/pdf")
if Path(cv_en_path).is_file():
    with open(cv_en_path, "rb") as pdf_en:
        st.sidebar.download_button(label="📄 Download CV in English", data=pdf_en, file_name="CV-AlexanderEduardoRojasGaray-EN.pdf", mime="application/pdf")

# Tabs para la navegación
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Inicio", "Experiencia", "Educación", "Certificaciones", "Habilidades", "Proyectos", "Visualizaciones", "Descargas"])

# Sección de inicio
with tab1:
    st.title("Alexander Eduardo Rojas Garay")
    st.image("files/WhatsApp Image 2024-10-23 at 7.23.55 PM(1).jpeg", width=240)
    st.markdown("## Data Scientist | Analista de Datos")
    st.write("Soy un científico de datos apasionado por aprovechar el poder de los datos para resolver problemas complejos. Tengo una sólida formación en física, matemáticas y programación, complementada con experiencia práctica en proyectos de machine learning y análisis predictivo.")
    st.write("Mis contribuciones incluyen la creación de modelos de predicción, el desarrollo de plataformas web, y la optimización de procesos empresariales mediante la automatización. Mi objetivo es impulsar el cambio y la innovación a través de soluciones basadas en datos.")

# Sección de Experiencia Profesional
with tab2:
    st.markdown("<div class='section-header'>Experiencia Profesional</div>", unsafe_allow_html=True)
    st.write("**Instituto de Matemáticas (UNAM) - Data Scientist**")
    st.write("En este rol, trabajé en el desarrollo de modelos predictivos para investigaciones avanzadas. Mis responsabilidades incluyeron el análisis de grandes volúmenes de datos, la aplicación de técnicas de machine learning como regresión logística y redes neuronales, y la presentación de resultados a investigadores y tomadores de decisiones.")

    st.write("**Colmena Space (UNAM) - Machine Learning Engineer**")
    st.write("En este proyecto aeroespacial, diseñé simulaciones para trayectorias de sondas lunares, optimizando el uso de recursos computacionales. Implementé algoritmos de machine learning para mejorar la precisión de las simulaciones y trabajé en colaboración con equipos interdisciplinarios para garantizar el éxito de las misiones.")

    st.write("**Asociación Aeroespacial de la Facultad de Ingeniería (UNAM) - Analista de Datos**")
    st.write("Analicé datos experimentales de pruebas de cohetes, proporcionando insights críticos para optimizar el diseño y las estrategias de lanzamiento. Esto incluyó la creación de dashboards interactivos para monitorear el rendimiento en tiempo real.")

    st.write("**Freelancer - Desarrollador Web**")
    st.write("He trabajado en proyectos de desarrollo web que abarcan desde páginas informativas hasta plataformas e-commerce. Entre los proyectos destacados se incluyen infrax.mx, una herramienta de gestión empresarial, y tecistem.com, un sitio educativo para cursos tecnológicos.")

    st.write("**Holtmont México - Automatización de Procesos**")
    st.write("Desarrollé un sistema de automatización utilizando Google Sheets y Apps Script, logrando una mayor eficiencia en la asignación de tareas y la consolidación de datos. Este proyecto redujo significativamente los tiempos de respuesta y mejoró la colaboración entre equipos.")

# Sección de Educación
with tab3:
    st.markdown("<div class='section-header'>Educación</div>", unsafe_allow_html=True)
    st.write("**Licenciatura en Física y Matemáticas - Universidad Nacional Autónoma de México (UNAM)** (2019 - 2024)")
    st.write("Mi formación académica se centró en el estudio de fenómenos físicos y matemáticos, complementado con cursos avanzados en programación y análisis de datos. Participé en investigaciones sobre simulación de sistemas cuánticos y diseño de algoritmos eficientes.")

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
    st.write("En este proyecto, utilicé modelos de machine learning para analizar tendencias electorales en estados clave de Estados Unidos. La combinación de datos históricos y técnicas avanzadas de predicción permitió identificar posibles resultados con un alto nivel de precisión, apoyando a analistas políticos en la toma de decisiones estratégicas.")
    st.write("[Ver proyecto completo](https://lnkd.in/e7DrEZEE)")

    st.write("🔬 **Articulo de Divulgación Sobre El Nobel de Física 2024: Inteligencia Artificial y Física Computacional en Materiales 2D**")
    st.write("Este artículo aborda el impacto de la inteligencia artificial en el diseño de materiales bidimensionales. Exploré cómo los algoritmos de machine learning pueden acelerar el descubrimiento de nuevos materiales y optimizar sus propiedades para aplicaciones tecnológicas avanzadas.")
    st.write("[Ver publicación completa](https://lnkd.in/e6q5QQfg)")

    st.write("🔗 **Aplicación de Predicción de Enfermedades Dentales**")
    st.write("Diseñé una herramienta basada en deep learning que analiza radiografías panorámicas para detectar enfermedades dentales. Utilizando YOLO V5 y Flask, el sistema permite a los odontólogos realizar diagnósticos más rápidos y precisos, mejorando la atención al paciente.")
    st.write("[Ver detalles del proyecto](https://github.com/usuario/dental-disease-detection)")

    st.write("💼 **Digitalización del Mercado Xochiquetzal**")
    st.write("Dirigí la creación de una plataforma e-commerce para empoderar a los comerciantes locales del Mercado Xochiquetzal en Tenancingo. Esta iniciativa mejoró la visibilidad de los productos en línea, incrementando las ventas y fortaleciendo la economía local.")

# Sección de Visualizaciones
with tab7:
    st.markdown("<div class='section-header'>Visualizaciones Interactivas</div>", unsafe_allow_html=True)
    data = pd.DataFrame({
        "Habilidad": ["Python", "SQL", "Machine Learning", "Visualización", "Cloud"],
        "Nivel": [95, 90, 85, 80, 75]
    })
    fig = px.bar(data, x="Habilidad", y="Nivel", title="Dominio de Habilidades", labels={"Nivel": "Porcentaje (%)"})
    st.plotly_chart(fig)

# Sección de Descargas
with tab8:
    st.markdown("<div class='section-header'>Descarga mis CVs</div>", unsafe_allow_html=True)
    if Path(cv_es_path).is_file():
        with open(cv_es_path, "rb") as pdf_es:
            st.download_button(label="📄 Descargar CV en Español", data=pdf_es, file_name="CV-AlexanderEduardoRojasGaray.pdf", mime="application/pdf")
    if Path(cv_en_path).is_file():
        with open(cv_en_path, "rb") as pdf_en:
            st.download_button(label="📄 Download CV in English", data=pdf_en, file_name="CV-AlexanderEduardoRojasGaray-EN.pdf", mime="application/pdf")
