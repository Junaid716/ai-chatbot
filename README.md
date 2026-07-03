<<<<<<< HEAD
# AI Document Chatbot 🤖

An intelligent chatbot that reads PDF documents and answers questions using Google Gemini AI.

## Features
- 📄 **PDF Document Processing** - Upload and analyze PDF files
- 🤖 **AI-Powered Responses** - Uses Google Gemini to answer questions
- 💬 **Interactive Chat** - Real-time conversation with your documents
- 🚀 **Easy Setup** - Simple installation and configuration

## Technologies Used
- **Python 3.8+**
- **Google Gemini API**
- **LangChain** - AI orchestration
- **PyPDF2** - PDF processing
- **python-dotenv** - Environment management

## Installation

### Prerequisites
- Python 3.8 or higher
- Git
- Google API Key (free at https://ai.google.dev/)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-chatbot.git
cd ai-chatbot
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup API Key**
- Go to https://ai.google.dev/
- Create a free API key
- Create `.env` file:
GOOGLE_API_KEY=GOOGLE_API_KEY=your_google_api_key_here
5. **Add a PDF**
- Place your PDF in `data/` folder
- Name it `sample.pdf`

6. **Run the chatbot**
```bash
python main.py
```

## Usage

```bash
python main.py
```

Then ask questions about your document:
You: What is machine learning?
Bot: Machine learning is... [AI response]

Type `exit` to quit.

## Project Structure
ai-chatbot/
├── main.py              # Main chatbot application
├── requirements.txt     # Python dependencies
├── .env                 # API keys (keep secret!)
├── README.md           # This file
├── data/               # PDF storage
│   └── sample.pdf
├── config/             # Configuration files
├── src/                # Source code modules
└── venv/               # Virtual environment

## Features Coming Soon
- [ ] Support multiple PDFs
- [ ] RAG (Retrieval-Augmented Generation)
- [ ] Web interface
- [ ] Document summarization
- [ ] Multi-language support

## License
MIT License

## Author
Mohammed Junaid
- GitHub: @Junaid716
- LinkedIn: linkedin.com/in/junaid-junnu-3b2ab924b

## Contact
junaidjunnu716@gmail.com

---

⭐ If you find this helpful, please star the repository!

=======
# ai-chatbot
AI Document Chatbot using Google Gemini API
>>>>>>> 4750618a37622fad6cec5aeb4e8a87cb4c4a2625
