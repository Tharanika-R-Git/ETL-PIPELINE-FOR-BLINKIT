# ETL-PIPELINE-FOR-BLINKIT

## 📌 Introduction

**ETL-PIPELINE-FOR-BLINKIT** is a robust ETL (Extract, Transform, Load) pipeline designed to automate the collection and processing of product data from Blinkit's APIs. This pipeline streamlines the extraction of data, transformation into structured formats, and loading into a database for seamless analysis and reporting. The project is modular, with dedicated scripts for each stage, ensuring scalability and maintainability.

---

## ✨ Features

- **Automated Data Extraction**  
  Utilizes Playwright for robust and efficient web scraping from Blinkit APIs.
- **Data Transformation**  
  Cleans, deduplicates, and structures raw data for downstream analytics (using Pandas).
- **Logging & Error Handling**  
  Generates logs for transparency and troubleshooting.
- **Modular Architecture**  
  Separate scripts for ingestion and transformation for easy extensibility.
- **Directory Structure**  
  Organized into `ingestion/`, `transform/`, `data/`, and `logs/` folders.

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ETL-PIPELINE-FOR-BLINKIT.git
   cd ETL-PIPELINE-FOR-BLINKIT
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Linux/Mac
   venv\Scripts\activate        # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   > **Note**: This project uses `playwright` and `pandas`. Install Playwright's browser binaries as well:
   ```bash
   playwright install
   ```

---

## 🚀 Usage

1. **Run Data Ingestion (Extraction)**
   ```bash
   python ingestion/scraper.py
   ```
   - Scrapes product data from Blinkit and stores it in `data/raw/`.
   - Logs the process in `logs/`.

2. **Run Data Transformation**
   ```bash
   python transform/transformation.py
   ```
   - Loads the latest raw data file, cleans it, removes duplicates, and prepares for loading.

3. **(Optional) Load into Database**
   - Extend the pipeline by adding a `load` module to insert data into your preferred database.

---

## 🏗️ Project Structure

```
ETL-PIPELINE-FOR-BLINKIT/
│
├── ingestion/
│   └── scraper.py           # Extracts data from Blinkit APIs
│
├── transform/
│   └── transformation.py    # Transforms and cleans the extracted data
│
├── data/
│   └── raw/                 # Stores raw scraped data
│
├── logs/                    # Logs for monitoring and debugging
│
├── README.md
└── requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and distribute as per the license terms.

---

> ⭐ **If you find this project useful, please star the repository!**

---

**Developed with ❤️ for data engineering and analytics.**

## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/Tharanika-R-Git/ETL-PIPELINE-FOR-BLINKIT
