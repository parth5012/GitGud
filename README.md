# GitGud

> AI-powered GitHub issue discovery agent that matches your skills with the perfect open-source contribution opportunities.

## Overview

**GitGud** is an intelligent agent that helps developers find meaningful open-source contributions by analyzing GitHub issues and matching them with their technical skills. Instead of manually searching through thousands of repositories, GitGud uses AI to discover, filter, and score issues based on your expertise, making it easier to find projects where you can make an impact.

## Features

- **AI-Powered Issue Discovery** - Automatically searches GitHub for relevant open issues
- **Smart Query Generation** - Transforms your goals and tech stack into optimized GitHub search queries
- **Skill-Based Scoring** - Evaluates issue compatibility using LLM-based analysis (0-100 score)
- **Dual Interface** - Choose between CLI or beautiful TUI (Terminal User Interface)
- **Codebase Analysis** - Fetch and analyze repository codebases when needed
- **LangGraph Architecture** - Built on modern agentic workflow framework

## Installation

### Prerequisites

- Python 3.13 or higher
- GitHub API token
- Google Gemini API key (or Groq API key)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/GitGud.git
   cd GitGud
   ```

2. **Install dependencies using uv** (recommended)
   ```bash
   pip install uv
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   GITHUB_TOKEN=your_github_token_here
   GROQ_API_KEY=your_groq_api_key_here
   DISCORD_WEBHOOK=your_discord_webhook_url
   ```

## Usage

### CLI Mode

For a simple command-line interface:

```bash
python main.py
```

Example interaction:
```
You: Find me good first issues in Python related to web scraping
Assistant: Generating optimized search query... Found 47 matching issues!
Analyzing compatibility with your skills... Top match: "Add retry logic to requests" (Score: 85/100)
```

### TUI Mode

For a rich terminal user interface with better visualization:

```bash
python cli.py
```

Features an interactive chat interface with:
- Real-time streaming responses
- Markdown rendering
- Scrollable chat history
- Beautiful UI with Textual framework

## Architecture

### Core Components

```
├── utils/
│   ├── graphs.py        # LangGraph workflow definitions
│   ├── nodes.py         # Agent nodes (chat, tools)
│   ├── tools.py         # GitHub API tools (fetch_issues, generate_query, etc.)
│   ├── states.py        # State schemas for agents
│   ├── prompts.py       # LLM prompts and templates
│   ├── helpers.py       # Utility functions
│   └── models.py        # LLM model configuration
├── main.py           # CLI entry point
└── cli.py            # TUI entry point
```

### Agent Tools

1. **generate_github_query** - Converts natural language goals into GitHub search queries
2. **fetch_issues** - Searches GitHub for matching issues
3. **get_likelihood_score** - Scores issue compatibility (0-100)
4. **fetch_codebase** - Downloads repository code for deeper analysis

### Planned Features

- **Filter Agent** - Evaluates repository health (star/issue ratio, maintainer responsiveness)
- **Semantic Matcher** - Redis-based vector search for skill matching
- **Notification System** - Discord/Slack webhooks for new opportunities

## Tech Stack

- **LangChain** - LLM orchestration framework
- **LangGraph** - Agentic workflow management
- **Google Gemini** / **Groq** - Large language models
- **PyGitHub** - GitHub API client
- **Textual** - Terminal UI framework
- **Redis** (planned) - Vector storage for skill matching
- **Celery** (planned) - Distributed task queue

## Contributing

Contributions are welcome! Feel free to:

- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is open source and available under the MIT License.

---

**Built with AI by developers, for developers**