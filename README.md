# **Personalized AI Assistant Builder**

**Create your own intelligent AI assistant with real-time web search, weather updates, and customizable interactions — powered by your own API keys.**

This project provides a modular, extensible framework for building a personalized AI assistant using OpenAI, SerpAPI, and OpenWeatherMap. You maintain control over service usage, API keys, and functionality, making it suitable for developers, hobbyists, and learners looking to experiment with AI capabilities.

---

## 🔧 **Features**

- **🔑 Personal API Key Integration**  
  Securely input and manage your own API credentials:
  - **OpenAI** – Core NLP functionality (chat, Q&A, text generation, etc.)
  - **SerpAPI** – Real-time web search for up-to-date knowledge
  - **OpenWeatherMap** – Fetch current weather and forecast data

- **🧩 Modular Design**  
  Clean code separation for maintainability and extension:
  - `app.py` – Main application entry point and user interface
  - `assistant.py` – Core logic for interacting with the AI model and services
  - `search_service.py` – Handles queries and responses from SerpAPI
  - `weather_service.py` – Communicates with OpenWeatherMap API
  - `web_scraper.py` – *(Optional)* Stub for adding web scraping functionality

- **🔐 Secure Key Handling**  
  - No need to manually edit a `.env` file
  - API keys are entered securely through the application interface
  - Stored temporarily within the session

- **📦 Dependency Management**
  - `requirements.txt` ensures easy setup with `pip`
  - `.gitignore` protects sensitive files and caches from being tracked

---

## 🚀 **Getting Started**

### ✅ Prerequisites

- Python 3.7+
- API keys for:
  - [OpenAI](https://platform.openai.com/account/api-keys)
  - [SerpAPI](https://serpapi.com/)
  - [OpenWeatherMap](https://openweathermap.org/api)

---

### 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ItsWip/Personal_AI_Assistant.git
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

### 🔐 API Key Configuration

- When you run the assistant (`app.py`), you’ll be prompted to enter your API keys via a secure input interface.
- No need to modify `.env` manually — your credentials remain safe in the current session.

---

### ▶️ Running the Assistant

```bash
python app.py
```

Use the terminal or UI (depending on your implementation) to interact with your assistant.

---

## 🗂️ Project Structure

```
.
├── .env                   # (Optional) – If used, stores API keys (ignored by Git)
├── .gitignore             # Specifies files/folders to ignore in version control
├── app.py                 # Main application entry point
├── assistant.py           # Core AI assistant logic
├── search_service.py      # Handles SerpAPI search queries
├── weather_service.py     # Manages weather data retrieval
├── web_scraper.py         # *(Optional)* Web scraping stub
└── requirements.txt       # Project dependencies
```

---

## 💡 Usage

Once running, your assistant can:

- ✨ Generate responses using OpenAI
- 🔍 Perform real-time web searches with SerpAPI
- 🌦️ Fetch weather reports via OpenWeatherMap

Customize your queries to ask the assistant anything—from casual chat and research to localized weather reports.

---

## ⚙️ Customization

You can easily tailor the assistant’s functionality by editing specific modules:

| File | Purpose |
|------|---------|
| `assistant.py` | Modify AI prompts, output formatting, or flow |
| `search_service.py` | Customize how search results are queried or filtered |
| `weather_service.py` | Format the weather response or switch to different endpoints |
| `app.py` | Modify the user interface or CLI logic |

---

## 🤝 Contributing

We welcome improvements, features, or bug fixes! Here's how to contribute:

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add your feature"`)  
4. Push to your fork (`git push origin feature-name`)  
5. Open a Pull Request and describe your changes

---

## 📜 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
