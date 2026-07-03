import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

def read_pdf_simple(file_path):
    """Read PDF file content"""
    try:
        import PyPDF2
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def create_chatbot():
    """Create and run the chatbot"""
    print("\n" + "="*60)
    print("🤖 AI Document Chatbot (Google Gemini)")
    print("="*60 + "\n")
    
    # Load document
    pdf_path = "data/sample.pdf"
    if not os.path.exists(pdf_path):
        print(f"❌ PDF not found at {pdf_path}")
        return
    
    print(f"📄 Loading: {pdf_path}...")
    document_text = read_pdf_simple(pdf_path)
    
    if not document_text:
        print("❌ Could not read PDF")
        return
    
    print("✅ Document loaded!\n")
    print("Type 'exit' to quit\n")
    
    # Chat loop
    while True:
        question = input("You: ").strip()
        
        if question.lower() == 'exit':
            print("\nGoodbye! 👋")
            break
        
        if not question:
            continue
        
        # Create prompt
        prompt = f"""Based on this document:

{document_text[:4000]}

Answer this question: {question}

Keep your answer concise and relevant."""
        
        try:
            print("\n🔍 Thinking...")
            
            response = model.generate_content(prompt)
            answer = response.text
            
            print(f"\nBot: {answer}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    create_chatbot()