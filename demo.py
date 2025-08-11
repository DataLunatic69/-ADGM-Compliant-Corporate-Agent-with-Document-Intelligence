#!/usr/bin/env python3
"""
Demo script to test ADGM Corporate Agent functionality
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'streamlit',
        'langchain',
        'langchain_groq',
        'langgraph',
        'docx',
        'PyPDF2',
        'pdfplumber',
        'pydantic'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} - Not installed")
    
    if missing_packages:
        print(f"\n🚨 Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -e . to install all dependencies")
        return False
    else:
        print("\n🎉 All dependencies are installed!")
        return True

def test_document_processor():
    """Test document processor functionality"""
    try:
        from utils.document_processor import DocumentProcessor
        processor = DocumentProcessor()
        print("✅ DocumentProcessor can be imported and instantiated")
        
        # Test with empty bytes (should handle gracefully)
        result = processor.extract_document_content(b"", "test.docx")
        if "error" in result:
            print("✅ Error handling works correctly")
        
        return True
    except Exception as e:
        print(f"❌ DocumentProcessor test failed: {e}")
        return False

def main():
    """Main demo function"""
    print("🏛️ ADGM Corporate Agent - Demo & Health Check")
    print("=" * 50)
    
    print("\n📦 Checking Dependencies:")
    deps_ok = check_dependencies()
    
    if deps_ok:
        print("\n🧪 Testing Core Components:")
        processor_ok = test_document_processor()
        
        if processor_ok:
            print("\n🚀 Ready to launch!")
            print("Run: streamlit run src/main.py")
        else:
            print("\n❌ Some tests failed. Check your installation.")
    
    print("\n📋 Quick Start:")
    print("1. Get a Groq API key from https://console.groq.com/")
    print("2. Run: streamlit run src/main.py")
    print("3. Enter your API key in the sidebar")
    print("4. Upload DOCX or PDF documents")
    print("5. Click 'Analyze Documents'")

if __name__ == "__main__":
    main()