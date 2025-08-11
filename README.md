# 🏛️ ADGM Corporate Agent

> **AI-Powered Legal Document Review for Abu Dhabi Global Market**

An intelligent Streamlit-based application that helps review legal documents for ADGM (Abu Dhabi Global Market) compliance, identifies missing documents, and highlights potential issues using advanced AI capabilities.

## ✨ Features

### 🔍 **Intelligent Document Analysis**
- **Multi-format Support**: Process both DOCX and PDF documents
- **Legal Process Detection**: Automatically identifies the type of legal process (Company Incorporation, Licensing, Employment)
- **Compliance Scoring**: Provides detailed compliance scores (0-100%) based on ADGM requirements
- **Issue Detection**: Identifies critical, high, medium, and low severity issues

### 📋 **Comprehensive Document Review**
- **Missing Document Detection**: Identifies required documents that haven't been uploaded
- **Jurisdiction Validation**: Checks for proper ADGM jurisdiction references
- **Required Clauses Analysis**: Ensures mandatory clauses are present
- **Language Review**: Identifies ambiguous or prohibited language

### 🤖 **AI-Powered Workflow**
- **Multi-Agent Architecture**: Uses LangGraph with specialized agents:
  - **Parser Agent**: Extracts content and metadata
  - **Validator Agent**: Checks completeness and basic compliance
  - **Compliance Agent**: Performs detailed analysis
  - **Output Agent**: Generates annotated documents
- **Groq AI Integration**: Powered by latest Groq models for fast, accurate analysis

### 🔒 **Security & Privacy**
- **Local Processing**: Documents are processed in real-time and not stored
- **API Key Security**: Keys are not saved or transmitted beyond the session
- **File Validation**: Multiple layers of validation for uploaded files
- **Size Limits**: 10MB per file limit with content truncation protection

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Groq API key (starts with 'gsk_')

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd corporate_agent
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e .
   ```

### Running the Application

1. **Start the Streamlit app**:
   ```bash
   streamlit run src/main.py
   ```

2. **Access the application**:
   - Open your browser to `http://localhost:8501`
   - Enter your Groq API key in the sidebar
   - Select your preferred AI model
   - Upload DOCX or PDF documents
   - Click "Analyze Documents" to start the review

## 📁 Project Structure

```
corporate_agent/
├── src/
│   ├── main.py                 # Streamlit application entry point
│   ├── agents/                 # AI agent implementations
│   │   ├── supervisor.py       # Main workflow orchestrator
│   │   ├── parser_agent.py     # Document parsing and extraction
│   │   ├── validator_agent.py  # Document validation
│   │   ├── compliance_agent.py # Compliance analysis
│   │   └── output_agent.py     # Result generation
│   ├── models/
│   │   └── schema.py          # Pydantic data models
│   └── utils/
│       ├── document_processor.py # Document processing utilities
│       └── adgm_references.py    # ADGM compliance rules
├── tests/                      # Test files
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## 📚 Supported Document Types

### **Company Incorporation**
- Articles of Association
- Memorandum of Association
- Incorporation Application Form
- UBO Declaration Form
- Register of Members and Directors

### **Licensing**
- Business License Application
- Business Plan
- Financial Statements
- Compliance Certificate

### **Employment**
- Employment Contract
- Job Description
- Salary Certificate

## 🔧 Configuration

### **Supported AI Models**
- `llama-3.3-70b-versatile` (Recommended for complex documents)
- `llama-3.1-70b-versatile` (Best balance of speed and accuracy)
- `llama-3.1-8b-instant` (Fastest processing)
- `mixtral-8x7b-32768` (Large context window)
- `gemma2-9b-it` (Efficient processing)

### **File Requirements**
- **Formats**: DOCX, PDF
- **Size Limit**: 10MB per file
- **Multiple Upload**: Supported
- **Text Limit**: 500KB extracted text per document

## 🛡️ Security Features

- **API Key Validation**: Validates Groq API key format
- **File Type Validation**: Strict file type checking
- **Size Limits**: Multiple layers of size validation
- **Content Filtering**: Protection against malicious content
- **Session Isolation**: No cross-session data leakage

## 📊 Output Features

### **Analysis Results**
- Compliance score with color-coded indicators
- Detailed issue breakdown by severity
- Missing document identification
- Actionable recommendations

### **Document Downloads**
- **JSON Report**: Complete analysis results in structured format
- **Reviewed Documents**: Original documents with highlighted issues and comments
- **ZIP Package**: All processed documents in a single download

## 🔧 Development

### **Dependencies**
- `streamlit>=1.31.0` - Web application framework
- `langchain>=0.1.0` - AI framework
- `langchain-groq>=0.1.0` - Groq integration
- `langgraph>=0.1.0` - Multi-agent workflows
- `python-docx>=0.8.11` - DOCX processing
- `PyPDF2>=3.0.0` - PDF processing
- `pdfplumber>=0.10.0` - Advanced PDF text extraction
- `pydantic>=2.0.0` - Data validation

### **Running Tests**
```bash
pytest tests/
```

### **Code Quality**
```bash
# Run linting
flake8 src/

# Format code
black src/
```

## 🚨 Known Limitations

- PDF text extraction may vary depending on document structure
- Scanned PDFs (images) are not supported
- Complex document layouts may affect parsing accuracy
- AI analysis quality depends on document language and clarity

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the documentation in the `docs/` folder
- Review the usage guidelines in the application sidebar

## 🔄 Version History

- **v0.1.0** - Initial release with DOCX support and basic compliance checking
- **v0.2.0** - Added PDF support, improved UI, enhanced security features

---

**Built with ❤️ for ADGM legal compliance**