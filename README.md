

# 📘 School Development 📘

## 1. Description 📄

**Project name:** School System  
**Author:** Carlos Alavez  
**Start date:** [04/04/2026]  
**Main technologies:**  

- Database: PostgreSQL / SQLite3  
- Backend: FastAPI, Django Rest Framework  
- Frontend: Django, Flask  
- ORM: SQLAlchemy / Django ORM  
- Version control: Git + GitHub  

**General description:**  
This project simulates a school with management of people, courses, schedules, enrollments, and grades. Two APIs (FastAPI and DRF) and two applications (Django and Flask) are developed to demonstrate different development approaches.

---

## 2. Database 💾

### ER Diagram

![ER Diagram](/imgs/School_Diagram.png)

### Main tables

| Table | Description |
|--------|-------------|
| People | Contains general information about all individuals (students, teachers, administrative staff, staff). |
| School | Defines campuses and general institution data. |
| Courses | Defines available courses and their area. |
| Semesters | Represents academic periods. |
| Schedules | Defines available schedules for each course. |
| Enrollments | Records student enrollment in courses and their status. |
| Enrollment_Schedule | Links enrollments with selected schedules. |
| Grades | Records partial grades and semester averages. |

---

### 2.3 Relationships

- People → School (N:1)  
- School → Courses (1:N)  
- Courses → Schedules (1:N)  
- Semesters → Schedules (1:N)  
- People → Enrollments (1:N)  
- Courses → Enrollments (1:N)  
- Enrollments → Enrollment_Schedule (M:N)  
- Enrollments → Grades (1:1)  

---

### 2.4 Create the database

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

#### Install PostgreSQL

```bash 
sudo apt update

sudo apt install postgresql postgresql-contrib
sudo -u postgres psql

#### Enter the database

```sql
CREATE DATABASE EscolarSystem;

CREATE USER ADMIN WITH PASSWORD '4dm1n-p4ssw0rd';
ALTER ROLE ADMIN SET client_encoding TO 'utf8';
ALTER ROLE ADMIN SET default_transaction_isolation TO 'read committed';
ALTER ROLE ADMIN SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE EscolarSystem TO ADMIN;

#exit the database
\q
```