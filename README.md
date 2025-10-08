# 🧩 Blueprint

### **A Smart Multi-User Project Manager Powered by Django + Electron**


## 🚀 Overview

**Blueprint** is a desktop application built with **Electron** and **Django**, designed to streamline project management, documentation, and automation.
It combines the flexibility of a web-based dashboard with the performance and integration of a native desktop app.


## 🧠 Key Features

### 🖥️ Frontend (Electron)

* Modern desktop UI with smooth animations and responsive layout
* Frame-less window with custom minimize & close buttons
* Seamless integration with Django backend
* Automatic window state management (show/hide/loading)
* Supports multi-user environments on local machines

### ⚙️ Backend (Django)

* Powerful admin panel for managing projects, categories, and code snippets
* SQLite support by default (easily switchable to PostgreSQL/MySQL)
* Dynamic API endpoints for future scalability
* Auto-saves and retrieves project data efficiently
* Secure, modular app structure

### 📁 Project Management

* Add, edit, and delete projects with ease
* Categorize projects by type, tags, and description
* Store code snippets or setup steps directly in the database
* Instantly reflect admin updates on the Electron dashboard


## 🧩 Tech Stack

| Layer    | Technology                                           |
| -------- | ---------------------------------------------------- |
| Frontend | **Electron.js**, **HTML5**, **CSS3**, **JavaScript** |
| Backend  | **Django 5+**, **Python 3.11+**                      |
| Database | **SQLite3** (default)                                |
| APIs     | Django REST (future-ready)                           |
| UI/UX    | Bootstrap 5, Custom CSS, Responsive Layout           |


## ⚡ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/balamurugan-cholas/Blueprint.git
cd Blueprint
```

### 2️⃣ Setup Backend (Django)

```bash
cd backend
python -m venv venv
venv\Scripts\activate       # on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Django will start at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**


### 3️⃣ Setup Frontend (Electron)

In a new terminal window:

```bash
cd electron
npm install
npm start
```

Electron will launch the desktop app automatically.


## 🧱 Admin Panel Access

Once Django is running:

1. Create a superuser

   ```bash
   python manage.py createsuperuser
   ```
2. Open **[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)**
3. Manage all projects, categories, and code snippets directly from there.


## 💡 Future Plans

* 🔐 User authentication and login system
* ☁️ Cloud sync for multi-device access
* ⚙️ Customizable themes and layouts
* 📦 One-click project deployment
* 🧠 AI-based project recommendations


## 🧑‍💻 Author

**Bala Murugan**
💼 Developer of **Blueprint**
🌐 [GitHub](https://github.com/<Balamurugan-cholas>)
📧 Contact: [[your-email@example.com](mailto:balamuruganofficial3@gmail.com)]


## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute with attribution.


## 🏁 Version

**Blueprint v1.0.0**

> "Design smarter. Build faster. Manage seamlessly."
