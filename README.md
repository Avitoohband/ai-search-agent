# AI Search Agent 🔍

A powerful multi-source research agent that combines Google, Bing, and Reddit searches to provide comprehensive, well-researched answers to any question. Built with LangGraph and powered by GPT-4o.

## 🚀 Features

- **Multi-Source Research**: Simultaneously searches Google, Bing, and Reddit for comprehensive coverage
- **Intelligent Reddit Analysis**: Automatically identifies and retrieves the most relevant Reddit discussions
- **AI-Powered Synthesis**: Uses GPT-4o to analyze and synthesize findings from all sources
- **Parallel Processing**: Leverages LangGraph for efficient concurrent searches
- **Real User Insights**: Extracts community opinions and real-world experiences from Reddit

## 🏗️ Architecture

The agent uses a graph-based workflow built with LangGraph:

1. **Parallel Search Phase**: Simultaneously queries Google, Bing, and Reddit
2. **Reddit Analysis**: AI selects the most valuable Reddit posts for deeper investigation
3. **Content Retrieval**: Downloads full Reddit discussions and comments
4. **Individual Analysis**: Analyzes results from each source separately
5. **Synthesis**: Combines all insights into a comprehensive final answer

## 📋 Prerequisites

- Python 3.12+
- OpenAI API key
- BrightData API key (for web scraping)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-search-agent.git
   cd ai-search-agent
   ```

2. **Install dependencies using uv** (recommended):
   ```bash
   uv sync
   ```

   Or with pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   BRIGHTDATA_API_KEY=your_brightdata_api_key_here
   ```

## 🚀 Usage

Run the interactive chatbot:

```bash
python main.py
```

The agent will prompt you for questions and provide comprehensive research-backed answers.

### Example Session

```
Multi-Source Research Agent
Type 'exit' to quit

Ask me anything: What are the pros and cons of remote work?

Starting parallel research process...
Launching Google, Bing, and Reddit searches...

Searching Google for: What are the pros and cons of remote work?
Searching Bing for: What are the pros and cons of remote work?
Searching Reddit for: What are the pros and cons of remote work?
Selected URLs:
   1. https://reddit.com/r/remotework/comments/xyz123/remote_work_reality_check
   2. https://reddit.com/r/programming/comments/abc456/working_from_home_experience

Getting reddit post comments
Processing 2 Reddit URLs
Successfully got 47 posts

Analyzing google search results
Analyzing bing search results
Analyzing reddit search results
Combine all results together

Final Answer:
[Comprehensive synthesized answer combining insights from all sources...]
```

## 📁 Project Structure

```
ai-search-agent/
├── main.py                 # Main application and graph workflow
├── prompts.py             # AI prompt templates for different analysis stages
├── web_operations.py      # Google, Bing, and Reddit search functions
├── snapshot_operations.py # BrightData API utilities for data retrieval
├── pyproject.toml         # Project dependencies and metadata
├── .env                   # Environment variables (create this)
└── README.md             # Project documentation
```

## 🔧 Core Components

### `main.py`
- Defines the LangGraph workflow
- Orchestrates parallel searches and sequential analysis
- Provides the interactive chatbot interface

### `prompts.py`
- Contains specialized AI prompts for analyzing different data sources
- Includes templates for Google, Bing, Reddit analysis and final synthesis

### `web_operations.py`
- Handles API interactions with BrightData for web scraping
- Implements search functions for Google, Bing, and Reddit
- Manages Reddit post content retrieval

### `snapshot_operations.py`
- Utilities for BrightData's asynchronous data collection
- Handles polling and downloading of search results

## 🌐 API Dependencies

### OpenAI API
Used for:
- Analyzing search results from each source
- Selecting relevant Reddit posts for deeper analysis  
- Synthesizing final comprehensive answers

### BrightData API
Used for:
- Scraping Google and Bing search results
- Retrieving Reddit search results and post content
- Bypassing rate limits and anti-bot measures

## ⚙️ Configuration

The agent can be customized by modifying parameters in `web_operations.py`:

- **Reddit search parameters**: Date range, sort order, number of posts
- **Reddit content depth**: Days back, comment limits, reply loading
- **Search engines**: Easy to extend with additional search sources

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] Add support for additional search engines (DuckDuckGo, Yandex)
- [ ] Implement caching for repeated queries
- [ ] Add web interface with Streamlit or FastAPI
- [ ] Support for image and video search results
- [ ] Integration with academic databases (arXiv, Google Scholar)
- [ ] Real-time streaming of search progress
- [ ] Export results to various formats (PDF, JSON, Markdown)

## 🐛 Troubleshooting

### Common Issues

**API Rate Limits**: BrightData has usage limits. Check your dashboard if searches fail.

**Reddit Retrieval Timeout**: Large Reddit threads may take time to process. Consider reducing `comment_limit` parameter.

**OpenAI API Errors**: Ensure your API key has sufficient credits and proper permissions.

### Debug Mode

For detailed logging, modify the print statements in `main.py` or add logging configuration.

## 📞 Support

If you encounter issues or have questions:
1. Check the troubleshooting section above
2. Search existing [GitHub Issues](https://github.com/yourusername/ai-search-agent/issues)
3. Create a new issue with detailed information about your problem

---

Built with ❤️ using LangGraph, OpenAI GPT-4o, and BrightData APIs.
