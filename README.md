# LangChain Search Agent Chatbot

A Streamlit-based AI chatbot powered by LangChain and Groq LLM with integrated search tools including Wikipedia, ArXiv, and DuckDuckGo. The application supports conversational memory using session-based history.

## Overview

This project implements a tool-enabled AI assistant using LangChain Agents. The chatbot can dynamically decide whether to retrieve information from:

- Wikipedia
- ArXiv research papers
- DuckDuckGo web search

The application maintains session-specific chat history and provides an interactive web interface using Streamlit.

## Features

- Groq LLM integration (`openai/gpt-oss-120b`)
- Tool-based agent architecture
- Wikipedia integration
- ArXiv paper retrieval
- DuckDuckGo web search
- Session-based conversational memory
- Streamlit chat interface

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- Wikipedia API
- ArXiv API
- DuckDuckGo Search
- FAISS (optional vector storage)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-search-agent.git
cd langchain-search-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a requirements file:

```bash
pip freeze > requirements.txt
```

## Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Alternatively, you can enter the API key directly in the Streamlit sidebar.

## Running the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## How It Works

1. The user submits a query through the Streamlit interface.
2. A LangChain agent determines which tool (Wikipedia, ArXiv, or web search) to use.
3. The Groq LLM processes the retrieved information.
4. Session-based message history is maintained using `RunnableWithMessageHistory`.
5. The assistant returns a contextual response.

## Example Queries

- Who is Geoffrey Hinton?
- Latest research on diffusion models
- What is LangChain?
- Recent AI research papers on RAG

## Core Components

- `ChatGroq`
- `create_agent`
- `RunnableWithMessageHistory`
- `WikipediaQueryRun`
- `ArxivQueryRun`
- `DuckDuckGoSearchRun`
- `Streamlit`

## Future Improvements

- Streaming responses
- Persistent database-backed memory
- Document upload support (PDF)
- Vector-based RAG implementation
- Docker deployment

## License

MIT License
