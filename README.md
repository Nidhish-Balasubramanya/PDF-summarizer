# PDF Summarizer using Gemini AI API

## 📌 Project Description
This project is a **PDF Summarizer** that uses **Google's Gemini AI API** to generate summaries of uploaded PDF documents. The application is built using **Streamlit** for an interactive UI and **PyPDF2** for extracting text from PDF files.

## 🛠 Features
- Upload and summarize PDF documents.
- Uses **Gemini AI** to generate concise and meaningful summaries.
- Interactive UI using **Streamlit**.
- Displays extracted summaries instantly.
- Error handling for file processing and API interactions.

---
## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/pdf-summarizer.git
cd pdf-summarizer
```

### 2️⃣ Create a Virtual Environment
It is recommended to create a virtual environment to manage dependencies.
```sh
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
Install the required dependencies using **pip**.
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project root directory and add your **Google Gemini API Key**:
```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---
## 🎯 How to Run the Application
Once everything is set up, run the application using:
```sh
streamlit run app.py
```

This will open a **Streamlit web app** in your default browser where you can upload PDFs and get instant summaries.

---
## 📜 Project Structure
```
📁 pdf-summarizer/
│-- app.py  # Main application file
│-- requirements.txt  # List of dependencies
│-- .env  # Environment variables (not shared in repo)
```

---
## 🛠 Technologies Used
- **Python**
- **Streamlit**
- **PyPDF2**
- **Google Gemini AI API**
- **python-dotenv**

---
## ⚡ Troubleshooting
**Issue:** API Key not found error.
- Ensure the `.env` file is properly set up with the correct API key.
- Run `echo $GOOGLE_API_KEY` (Linux/macOS) or `echo %GOOGLE_API_KEY%` (Windows) to check if the environment variable is loaded.

**Issue:** Streamlit not launching.
- Ensure you have activated the virtual environment before running Streamlit.
- Try reinstalling dependencies using `pip install -r requirements.txt`.

---
## 🏆 Contributing
Feel free to contribute! Fork the repository, make changes, and submit a pull request.

---
## 📜 License
This project is licensed under the **MIT License**.

---
## 📩 Contact
For any questions or issues, feel free to reach out via [GitHub Issues](https://github.com/your-username/pdf-summarizer/issues).
or mail to nidhishbalasubramanya@gmail.com

