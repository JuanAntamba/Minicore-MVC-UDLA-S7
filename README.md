# 📊 Sistema de Gestión de Calificaciones - Minicore UDLA

Este es un proyecto universitario desarrollado con el framework Django aplicando el patrón de arquitectura **MVT** (Modelo-Vista-Template), que es la variante de Django para el patrón **MVC** (Modelo-Vista-Controlador).

[![Django](https://img.shields.io/badge/Framework-Django%205.0-092e20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Language-Python%203.11+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/Frontend-Semantic_HTML5-e34f26?logo=html5&logoColor=white)](#)
[![Deployment](https://img.shields.io/badge/Deployed_on-Render-46a35e?logo=render&logoColor=white)](https://render.com/)

Este proyecto implementa un sistema de cálculo de calificaciones dinámico utilizando el patrón **MVT (Model-View-Template)**. La aplicación está diseñada para filtrar registros académicos por fechas y proyectar la nota necesaria para la aprobación del semestre.

## 🎯 Objetivo de la Tarea
Desarrollar una aplicación funcional que demuestre el uso de:
1. **Modelos:** Relación Alumno-Nota.
2. **Vistas (Controlador):** Lógica de filtrado por rangos de fecha y promedios ponderados.
3. **Templates:** Interfaz de usuario construida con **HTML5 Semántico**

## 🧮 Lógica de Negocio (Algoritmo)
El sistema calcula la nota del **Progreso 3** basándose en una meta mínima de **6.0/10.0**, aplicando los siguientes pesos configurables:

| Progreso | Peso (%) | Rango de Fecha (Ejemplo) |
| :--- | :--- | :--- |
| **Progreso 1** | 25% | Marzo - Abril |
| **Progreso 2** | 35% | Noviembre - Diciembre |
| **Progreso 3** | 40% | *Cálculo Automático* |

**Fórmula aplicada:**
`P3 = (6.0 - (PromP1 * 0.25 + PromP2 * 0.35)) / 0.40`

## 🏗️ Estructura del Proyecto (MVT)
* **`models.py`**: Definición de entidades `Alumno` y `Nota` con relaciones de llave foránea.
* **`views.py`**: Filtros de QuerySets por fechas y procesamiento de diccionarios para la vista.
* **`templates/`**: Uso de etiquetas semánticas como `<main>`, `<header>`, y `<section>`.

## 🚀 Instalación y Uso Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/JuanAntamba/Minicore-MVC-UDLA-S7.git](https://github.com/JuanAntamba/Minicore-MVC-UDLA-S7.git)
    ```

2. **Configurar el entorno:**

```Bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt 
```

3. **Ejecutar migraciones y servidor:**

```Bash
python manage.py migrate
python manage.py runserver
```

Desarrollado por: Juan Carlos Antamba