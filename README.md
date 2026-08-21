# 🎓 SnapClass — Landing Page

The marketing/landing page for **SnapClass**, an AI-powered classroom attendance system using face and voice recognition. Built with **Flask** and custom CSS, this page introduces the product and links visitors to the live app.

🔗 **Try the live app:** [SnapClass AI Attendance](https://snapclass-ai-attendance-app-4gw6keezdpnv5fkbsyva5m.streamlit.app/)

> For the full technical README (architecture, database schema, ML pipelines, setup), see the [main SnapClass repository](#).

---

## ✨ What's on this page

- Hero section introducing the product
- Feature highlights (AI Face Analysis, Voice ID, QR-based enrollment)
- Step-by-step "Teacher's Journey" and "Student's Journey" walkthroughs
- Tech stack showcase
- Call-to-action linking to the live Streamlit app

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Flask (Python) |
| Templating | Jinja2 (`render_template`) |
| Styling | Custom CSS (responsive, mobile-first breakpoints) |

---

## 📁 Project Structure

```
snap_class_frontend/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── img/
│       ├── app_logo.png
│       └── demo/            # Product screenshots
│
├── templates/
│   └── index.html
│
├── app.py                   # Flask entry point
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 🚀 Getting Started (Local)

### 1. Clone the repository
```bash
git clone https://github.com/JashSolanki1503/snapclass-ai-attendance-app-landing-page.git
cd snapclass-ai-attendance-app-landing-page
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 👤 Author

**Jash Solanki**
AI Engineering Student | Agentic AI & RAG Systems

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).