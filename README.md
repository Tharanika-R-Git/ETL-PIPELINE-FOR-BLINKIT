
# 🚀 ETL-PIPELINE-FOR-BLINKIT

A robust ETL (Extract, Transform, Load) pipeline project designed for Blinkit, featuring a FastAPI backend with SQLite database integration and a React.js frontend for data visualization and management.

---

## 📖 Introduction

**ETL-PIPELINE-FOR-BLINKIT** streamlines the process of handling product datasets for Blinkit. The pipeline automates data extraction, transformation, and loading into a SQLite database, and exposes APIs for data access and management. The frontend enables users to interact visually with the processed data, making analytics and reporting simple and intuitive.

---

## ✨ Features

- **Backend (FastAPI + SQLite):**
  - ETL scripts for loading and managing product data.
  - RESTful API endpoints for CRUD operations.
  - Secure and scalable database design.

- **Frontend (React.js):**
  - Interactive UI for viewing and managing products.
  - Data visualization with charts.
  - Responsive design for seamless user experience.

- **Database Utilities:**
  - Scripts to check, create, and manage tables.
  - CSV loader for bulk data import.

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ETL-PIPELINE-FOR-BLINKIT.git
cd ETL-PIPELINE-FOR-BLINKIT
```

### 2. Backend Setup

#### a. Create a Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### b. Install Dependencies
```bash
pip install fastapi uvicorn pandas sqlite3
```

#### c. Set Up the Database
```bash
cd Backend/database
python create_table.py
```

#### d. Load CSV Data
Place your processed CSV in the appropriate directory and run:
```bash
python load_csv_todb.py
```

#### e. Start FastAPI Server
```bash
cd ..
uvicorn main:app --reload
```

### 3. Frontend Setup

#### a. Install Node.js Dependencies
```bash
cd ../../Frontend/frontend
npm install
```

#### b. Start the React App
```bash
npm start
```

---

## 🚦 Usage

- **Backend API:**  
  The FastAPI server runs at `http://localhost:8000`. Use endpoints to fetch, add, update, or delete product records.

- **Frontend UI:**  
  The React app runs at `http://localhost:3000`. Open it in your browser to interact with the product data visually.

- **Database Operations:**  
  Use the database scripts in `Backend/database/` to check tables (`checktable.py`), create tables (`create_table.py`), and load CSVs (`load_csv_todb.py`).

---

## 🤝 Contributing

Contributions are welcome!  
Please follow these guidelines:

1. Fork this repo.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes.
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

For major changes, please open an issue first to discuss what you want to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> **ETL-PIPELINE-FOR-BLINKIT** is crafted for efficiency and scalability.  
> For questions, suggestions, or support, please open an issue or contact the maintainers.

---



## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/Tharanika-R-Git/ETL-PIPELINE-FOR-BLINKIT
Vercel Link : https://etl-pipeline-for-blinkit-tk55.vercel.app/
