# 📘 Desarrollo Escuela 📘

## 1. Descripción 📄

**Nombre del proyecto:** Sistema Escolar  
**Autor:** Carlos Alavez
**Fecha de inicio:** [04/04/2026]
**Tecnologías principales:**  

- Base de datos: PostgreSQL / SQLite3
- Backend: FastAPI, Django Rest Framework  
- Frontend: Django, Flask  
- ORM: SQLAlchemy / Django ORM  
- Control de versiones: Git + GitHub

**Descripción general:**  
Este proyecto simula una escuela con gestión de personas, cursos, horarios, inscripciones y calificaciones. Se desarrollan dos APIs (FastAPI y DRF) y dos aplicaciones (Django y Flask) para demostrar diferentes enfoques de desarrollo.

---

## 2. Base de datos 💾

### Diagrama DER

![Diagrama DER](/imgs/Diagrama%20Entidad-Relación.png)

### Tablas principales

| Tabla | Descripción |
|--------|-------------|
| Personas | Contiene información general de todas las personas (alumnos, profesores, administrativos, staff). |
| Escuela | Define los campus y datos generales de la institución. |
| Cursos | Define los cursos disponibles y su área. |
| Semestres | Representa los periodos académicos. |
| Horarios | Define los horarios disponibles para cada curso. |
| Inscripciones | Registra la inscripción de alumnos en cursos y su estatus. |
| Inscripcion_Horario | Vincula inscripciones con horarios seleccionados. |
| Calificaciones | Registra las calificaciones parciales y promedio por semestre. |

---

### 2.3 Relaciones

- Personas → Escuela (N:1)
- Escuela → Cursos (1:N)
- Cursos → Horarios (1:N)
- Semestres → Horarios (1:N)
- Personas → Inscripciones (1:N)
- Cursos → Inscripciones (1:N)
- Inscripciones → Inscripcion_Horario (M:N)
- Inscripciones → Calificaciones (1:1)
