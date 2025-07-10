# Expentia

Expentia is a Python-based application designed to help users manage and analyze their personal expenses with ease. By combining intelligent financial recommendations, interactive data visualizations, and a conversational chatbot interface, Expentia empowers users to make informed decisions about their spending habits. The modular design allows for easy extension and integration of new features.

---

## Features

- **Smart financial recommendations**
- **Interactive charts and data visualizations**
- **Chatbot for expense-related queries**

---

## Getting Started

### Prerequisites
- Python 3.7+
- Required packages (see below)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/expentia.git
   cd expentia
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Copy `api.env` to `.env` and fill in your API keys as needed.

### Running the Application
```bash
python app.py
```

---

## File Structure & Details

- **app.py** — Main application entry point. Orchestrates the app, routes user requests, and integrates modules.
- **charts.py** — Logic for generating interactive charts and data visualizations of spending patterns.
- **chatbot_logic.py** — Implements the chatbot interface for natural language queries about expenses.
- **data_utils.py** — Utility functions for data processing, cleaning, and transformation.
- **recommender.py** — Recommendation engine for analyzing user data and offering personalized financial advice.

--- 
