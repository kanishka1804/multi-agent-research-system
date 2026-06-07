# 🍀 Multi-Agent Research System

> An autonomous AI research pipeline powered by multi-agent orchestration — searches, reads, verifies and writes research reports automatically.

---

## 🧠 What is this?

**Multi-Agent Research System** is a fully autonomous research pipeline where multiple AI agents collaborate to produce structured, fact-checked research reports on any topic.

You enter a topic → 6 agents work together → you get a complete research report in minutes.

---

## ⚙️ How it Works

```
User enters topic
       ↓
🧭 Supervisor Agent    →  Plans research strategy & generates search queries
       ↓
🔍 Search Agent        →  Searches the web using Tavily API
       ↓
📖 Reader Agent        →  Scrapes & extracts content from top URLs
       ↓
✍️  Writer             →  Drafts a structured research report
       ↓
🔬 Fact Checker Agent  →  Verifies key claims with evidence
       ↓
⚖️  Critic Agent       →  Reviews and scores the report quality
       ↓
📄 Final Report        →  Downloadable report with sources & fact-check
```

---

## 🚀 Features

- **6-agent pipeline** — Supervisor, Search, Reader, Writer, Fact Checker, Critic
- **Supervisor pattern** — plans research strategy before agents start
- **Automated fact-checking** — verifies claims with ✅ / ❌ / ⚠️ verdicts
- **Critic scoring** — rates report quality out of 10
- **Real URLs only** — no hallucinated sources
- **Beautiful Streamlit UI** — dark clover theme with live agent status
- **User API keys** — users bring their own keys, yours are never used
- **Download report** — export as `.txt` file
- **Session persistence** — results stay after clicking buttons

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **LangChain** | Agent orchestration & LLM chains |
| **LangGraph** | Supervisor agent framework |
| **Groq (LLaMA 3.3 70b)** | LLM inference |
| **Tavily API** | Web search & URL extraction |
| **Streamlit** | Web UI |
| **Python 3.12** | Core language |

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/kanishka1804/multi-agent-research-system.git
cd multi-agent-research-system
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API keys
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Get your free API keys:
- **Groq** → [console.groq.com](https://console.groq.com)
- **Tavily** → [tavily.com](https://tavily.com)

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the app in your browser at `http://localhost:8501`
2. Enter your **Groq** and **Tavily** API keys in the sidebar
3. Type a research topic in the search box
4. Press **Enter** or click **Run Research Pipeline**
5. Watch all 6 agents work in real time
6. View the report, fact-check results, and critic score
7. Download the report as a `.txt` file

---

## 📁 Project Structure

```
multi-agent-research-system/
│
├── app.py            # Streamlit UI — main entry point
├── agents.py         # Agent & chain definitions
├── supervisor.py     # Supervisor agent — research planning
├── tools.py          # Web search, scraping & fact-check tools
├── pipeline.py       # Core research pipeline logic
├── requirements.txt  # Python dependencies
├── .gitignore        # Ignored files
└── README.md         # This file
```

---

## 🔑 API Keys Required

| Key | Where to get | Cost |
|---|---|---|
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) | Free tier available |
| `TAVILY_API_KEY` | [tavily.com](https://tavily.com) | Free tier available |

> **Note:** Your API keys are never stored. They are used only for your session.
