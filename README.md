# 🚀 LinkedIn Post Generator

An AI-powered **LinkedIn Post Generator** built using **LangGraph's iterative workflow** to generate, review, and refine high-quality LinkedIn posts.

The system combines **Groq**, **Mistral AI**, and **Tavily Search** to create a workflow where AI-generated content is continuously improved through an iterative writing and reviewing process.

---

## ✨ Features

* 🤖 **AI-Powered Post Generation**

  * Generates professional and engaging LinkedIn posts from a given topic.

* 🔄 **Iterative AI Workflow**

  * Uses **LangGraph** to create a writer → reviewer → refinement workflow.
  * Posts are repeatedly improved based on reviewer feedback.

* ✍️ **AI Writer**

  * Uses **Groq** for fast content generation.

* 🧐 **AI Reviewer**

  * Uses **Mistral AI** to evaluate the generated post.
  * Provides feedback on clarity, engagement, structure, and relevance.

* 🔎 **Web Search**

  * Uses **Tavily Search** to retrieve relevant and up-to-date information.
  * Helps ground posts with current information when required.

* 🎯 **LinkedIn-Focused Content**

  * Produces structured posts with professional tone, hooks, readable formatting, and relevant hashtags.

---

## 🏗️ Architecture

```text
                         ┌──────────────────┐
                         │   User Topic     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  Tavily Search   │
                         │   Web Research   │
                         └────────┬─────────┘
                                  │
                                  ▼
                     ┌─────────────────────────┐
                     │      LangGraph          │
                     │   Iterative Workflow    │
                     └────────────┬────────────┘
                                  │
                         ┌────────▼────────┐
                         │   AI Writer     │
                         │     Groq        │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  AI Reviewer    │
                         │   Mistral AI    │
                         └────────┬────────┘
                                  │
                         ┌────────▼────────┐
                         │ Review Feedback │
                         └────────┬────────┘
                                  │
                            ┌─────▼─────┐
                            │  Improve? │
                            └─────┬─────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                   YES                         NO
                    │                           │
                    ▼                           ▼
              ┌───────────┐             ┌──────────────┐
              │  Rewrite  │             │ Final LinkedIn│
              │   Post    │             │     Post      │
              └─────┬─────┘             └──────────────┘
                    │
                    └──────────► Review
```

---

## 🔄 Iterative Workflow

The core of the project is a **LangGraph-based iterative workflow**.

### Workflow

1. **User provides a topic**
2. **Tavily searches the web** for relevant information.
3. **Groq generates the initial LinkedIn post.**
4. **Mistral AI reviews the generated post.**
5. The reviewer provides feedback.
6. LangGraph evaluates whether the post needs improvement.
7. If improvement is required, the writer generates a revised version.
8. The reviewer evaluates the revised post again.
9. The process continues until the post reaches the desired quality.
10. The final post is returned to the user.

This approach allows the system to behave more like an **AI content pipeline** rather than a simple one-shot text generator.

---

## 🧠 Why LangGraph?

LangGraph is used to manage the **stateful and iterative workflow**.

Instead of:

```text
Topic → LLM → Final Post
```

the project follows:

```text
Topic
  ↓
Research
  ↓
Write
  ↓
Review
  ↓
Improve
  ↓
Review
  ↓
Final Post
```

This makes it possible to implement:

* Stateful execution
* Conditional routing
* Iterative refinement
* Feedback loops
* Multiple AI agents/models
* Tool integration

---

## 🛠️ Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| 🐍 Python        | Core programming language       |
| 🦜 LangChain     | LLM and tool integration        |
| 🔄 LangGraph     | Workflow orchestration          |
| ⚡ Groq           | Fast AI-powered writing         |
| 🧠 Mistral AI    | Post reviewing and evaluation   |
| 🔎 Tavily        | Web search and research         |
| 🌐 Streamlit     | User interface                  |
| 🔐 python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
linkedin-post-generator/
│
├── app.py
├── agents.py
├── workflow.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── ...
```

> Your exact file structure may differ depending on how the project is organized.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/manasviantil/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Never commit `.env` to GitHub.

A `.env.example` file can be used instead:

```env
GROQ_API_KEY=
MISTRAL_API_KEY=
TAVILY_API_KEY=
```

---

## ▶️ Run the Application

If you're using Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example

### Input

```text
The future of Generative AI in software development
```

### Workflow

```text
User Topic
    ↓
Tavily Web Search
    ↓
Research Results
    ↓
Groq Writer
    ↓
Generated LinkedIn Post
    ↓
Mistral Reviewer
    ↓
Feedback
    ↓
Groq Writer
    ↓
Improved Post
    ↓
Final LinkedIn Post
```

### Output

The final output is a polished LinkedIn post containing:

* Attention-grabbing hook
* Relevant insights
* Clear structure
* Professional tone
* Engaging conclusion
* Relevant hashtags

---

## 🔥 Key Highlights

### Multi-Model Architecture

The project uses different AI models for different responsibilities:

```text
Groq
 ↓
Writing / Generation

Mistral AI
 ↓
Reviewing / Critiquing

Tavily
 ↓
Web Research

LangGraph
 ↓
Workflow Orchestration
```

This demonstrates how different models and tools can be combined into a single AI workflow.

---

## 🎯 Use Cases

This project can be useful for:

* LinkedIn content creation
* AI/ML professionals
* Developers sharing technical knowledge
* Students building their professional presence
* Personal branding
* Technology news posts
* Industry insights
* Educational content

---

## 🚀 Future Improvements

Potential improvements include:

* [ ] Multiple LinkedIn post styles
* [ ] Custom tone selection
* [ ] Post length control
* [ ] Audience selection
* [ ] Automatic hashtag generation
* [ ] LinkedIn API integration
* [ ] Post performance analysis
* [ ] Persistent conversation history
* [ ] Human-in-the-loop approval
* [ ] More specialized reviewer agents
* [ ] Deployment using Streamlit Cloud

---

## 📚 Concepts Demonstrated

This project demonstrates practical implementation of:

* Generative AI
* LLM orchestration
* LangGraph
* Agentic workflows
* State management
* Conditional edges
* Iterative refinement
* Prompt engineering
* Tool calling
* Web search integration
* Multi-model AI systems
* AI-based content evaluation

---

## 👨‍💻 Author

**Manasvi**

Computer Science & Engineering | AI/ML Enthusiast

🔗 GitHub: `https://github.com/manasviantil`

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!
