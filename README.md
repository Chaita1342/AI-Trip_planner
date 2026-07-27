<div align="center">

# 🌍 AI Trip Planner

### Plan Smarter. Travel Better. Powered by AI.

An intelligent travel planning assistant that leverages **LangGraph**, **LangChain**, **Groq LLM**, and multiple external APIs to generate personalized travel itineraries with real-time recommendations for attractions, restaurants, transportation, weather, and trip budgeting.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-Agent-green)
![LangGraph](https://img.shields.io/badge/LangGraph-MultiAgent-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)


</div>

---

# ✨ Overview

Planning a trip often requires switching between multiple websites to find attractions, restaurants, weather forecasts, transportation options, and budget estimates.

**AI Trip Planner** simplifies this process by combining multiple APIs and AI-powered reasoning into a single conversational assistant capable of generating personalized travel plans in seconds.

---

# 🚀 Features

✅ AI-powered trip planning 

✅ Intelligent reasoning using LangGraph

✅ Search popular tourist attractions

✅ Discover highly-rated restaurants

✅ Find local transportation options

✅ Real-time weather forecasting

✅ Currency conversion

✅ Hotel cost estimation

✅ Daily travel budget calculation

✅ Interactive Streamlit interface

---

# 🏗️ System Architecture
<!-- <div align="center"> -->

```text
                                         ┌─────────────────────────┐
                                         │          User           │
                                         └────────────┬────────────┘
                                                      │
                                                      ▼
                                     ┌────────────────────────────────┐
                                     │      Streamlit Frontend        │
                                     │      (streamlit_app.py)        │
                                     └────────────────┬───────────────┘
                                                      │
                                             HTTP Request
                                                      │
                                                      ▼
                                     ┌────────────────────────────────┐
                                     │        FastAPI Backend         │
                                     │          (main.py)             │
                                     └────────────────┬───────────────┘
                                                      │
                                                      ▼
                                     ┌────────────────────────────────┐
                                     │      LangGraph AI Agent        │
                                     │ Intent → Reason → Tool Choice  │
                                     └────────────────┬───────────────┘
                                                      │
                      ┌───────────────────────────────┼────────────────────────────────┐
                      │                               │                                │
                      ▼                               ▼                                ▼
             ┌────────────────┐              ┌────────────────┐               ┌─────────────────┐
             │  Weather Tool  │              │  Places Tool   │               │ Expense Tool    │
             └───────┬────────┘              └───────┬────────┘               └────────┬────────┘
                     │                               │                                 │
                     ▼                               ▼                                 ▼
           OpenWeatherMap API              Google Places API                 Calculator Engine
                                                     │
                                ┌────────────────────┼────────────────────┐
                                ▼                    ▼                    ▼
                       Foursquare API        Tavily Search API      Google AI API
                                                 (Fallback)

                                                      │
                                                      ▼
                                     ┌────────────────────────────────┐
                                     │     LangChain + Groq LLM       │
                                     │ Combines retrieved information │
                                     │ Generates final travel plan    │
                                     └────────────────┬───────────────┘
                                                      │
                                                      ▼
                              ┌────────────────────────────────────────────────┐
                              │        Personalized Travel Itinerary           │
                              │                                                │
                              │ • Tourist Attractions                          │
                              │ • Restaurants & Cafés                          │
                              │ • Weather Forecast                             │
                              │ • Transportation Options                       │
                              │ • Currency Conversion                          │
                              │ • Hotel Cost Estimation                        │
                              │ • Trip Budget Breakdown                        │
                              └────────────────┬───────────────────────────────┘
                                               │
                                               ▼
                                   Displayed in Streamlit UI
```


# 📁 Project Structure

```text
AI-Trip-Planner
│
├── agent/
│   └── agentic_workflow.py          # LangGraph agent workflow
│
├── config/
│   └── config.yaml                  # Application configuration
│
├── frontend/
│   ├── assets/
│   │     travel1.jpg
│   │     ...
│   │     travel6.jpg
│   │
│   ├── gallery.html
│   └── styles.css
|
├── notebook/
│   └── experiment.ipynb             # Development & experimentation
│
├── prompt_library/
│   └── prompt.py                    # System prompts
│
├── tools/
│   ├── arithmetic_op_tool.py
│   ├── currency_con_tool.py
│   ├── expense_calculator_tool.py
│   ├── place_search_tool.py
│   └── weather_info_tool.py
│
├── utils/
│   ├── calculator.py
│   ├── config_loader.py
│   ├── currency_conv.py
│   ├── expense_calculator.py
│   ├── model_loaders.py
│   ├── place_info_search.py
│   ├── save_to_doc.py
│   └── weather_info.py
│
├── main.py                          # FastAPI backend
├── streamlit_app.py                 # Streamlit frontend
├── setup.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Tech Stack

## AI Frameworks

- LangChain
- LangGraph
- Groq LLM
  
## 🖥️ Frontend

- Streamlit
- HTML5
- CSS3
- JavaScript (ES6)
## Backend

- Python
- Streamlit

## APIs

- Google Places API
- Google AI (Gemini) API
- Foursquare Places API
- Tavily Search API
- OpenWeatherMap API
- Exchange Rate API
- Groq API
- LangSmith API *(Optional – Used for LangChain tracing and monitoring)*

## Configuration

- YAML (`config.yaml`)
- Environment Variables (`.env`)
- python-dotenv
- pyproject.toml

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Chaita1342/AI-Trip_planner.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root and add the following API keys:

```env
# Groq LLM API
GROQ_API_KEY=

# Google AI (Gemini) API
GOOGLE_API_KEY=

# Google Places API
GPLACES_API_KEY=

# Foursquare Places API
FOURSQUARE_API_KEY=

# Tavily Search API
TAVILAY_API_KEY=

# OpenWeatherMap API
OPENWEATHERMAP_API_KEY=

# Exchange Rate API
EXCHANGE_RATE_API_KEY=

# LangSmith API (Optional)
LANGCHAIN_API_KEY=
```

> **Note:** These API keys are required for the application to access external services such as LLM inference, place search, weather forecasting, currency conversion, and travel recommendations.

---

# ▶️ Running the Application

The application consists of:

- **FastAPI Backend**
- **Streamlit Frontend**

## Step 1 — Start the FastAPI Server

Open a terminal and run:

```bash
uvicorn main:app --reload --port 8000
```

The backend will be available at:

```
http://127.0.0.1:8000
```

---

## Step 2 — Start the Streamlit Frontend

Open **another terminal** and run:

```bash
streamlit run streamlit_app.py
```

The frontend will open at:

```
http://localhost:8501
```

Now you can interact with the AI Trip Planner through the Streamlit interface.

---

# 💡 Example Prompt

```
Plan a 5-day trip to New York with a budget of $1500.
Include tourist attractions, restaurants, transportation,
daily weather, and estimated expenses.
```

---

# 🔄 Workflow

```text
User Query
      │
      ▼
LangGraph Agent
      │
      ▼
Reasoning & Planning
      │
      ▼
Tool Selection
      │
      ├── Weather Tool
      ├── Google Places Tool
      ├── Expense Calculator
      ├── Currency Converter
      └── Tavily Search
      │
      ▼
Response Generation
      │
      ▼
Personalized Travel Plan
```

---

# 📡 APIs Used

| API / Service | Purpose |
|----------------|---------|
| **Groq API** | Large Language Model (LLM) inference for generating personalized travel plans |
| **Google Places API** | Search attractions, restaurants, landmarks, and transportation information |
| **Google AI (Gemini) API** | Google's Generative AI models (optional/alternative LLM support) |
| **Foursquare Places API** | Discover nearby restaurants, attractions, hotels, and points of interest |
| **Tavily Search API** | Web search and fallback information retrieval for travel recommendations |
| **OpenWeatherMap API** | Fetch real-time weather conditions and forecasts |
| **Exchange Rate API** | Retrieve live exchange rates and perform currency conversion |
| **LangSmith API** *(Optional)* | Trace, monitor, and debug LangChain/LangGraph executions |
---

---

# 🛣️ Future Enhancements

- Flight recommendation system
- Hotel booking integration
- Interactive maps
- Voice-enabled travel assistant
- PDF itinerary export
- User authentication
- Saved trips
- Multi-language support
- AI memory for returning users

---




<div align="center">

⭐ If you found this project useful, please consider giving it a star!

</div>
