from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_pdf():
    """Create a sample PDF for testing"""
    pdf_path = "data/sample.pdf"
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, height - 50, "AI & Machine Learning Guide")
    
    # Content
    c.setFont("Helvetica", 12)
    y = height - 100
    
    content = """
    Introduction to Machine Learning
    
    Machine Learning is a subset of Artificial Intelligence that enables 
    systems to learn and improve from experience without being explicitly programmed.
    
    Types of Machine Learning:
    
    1. Supervised Learning - Uses labeled data to train models. Examples include 
    classification and regression tasks.
    
    2. Unsupervised Learning - Works with unlabeled data to find patterns and 
    relationships. Examples include clustering and dimensionality reduction.
    
    3. Reinforcement Learning - Agents learn by interacting with an environment 
    and receiving rewards or penalties for actions.
    
    Key Technologies:
    
    Python is the most popular language for Machine Learning development. Libraries 
    like TensorFlow, PyTorch, and Scikit-learn provide powerful tools for building 
    ML models.
    
    Deep Learning uses neural networks with multiple layers to learn complex patterns 
    in data. It powers modern applications like:
    - Image Recognition
    - Natural Language Processing
    - Generative AI
    
    Applications of Machine Learning:
    
    Machine Learning is used in many industries:
    - Healthcare: Disease diagnosis and drug discovery
    - Finance: Fraud detection and risk assessment
    - Retail: Recommendation systems and demand forecasting
    - Transportation: Autonomous vehicles and traffic prediction
    
    Future of AI:
    
    The future of Artificial Intelligence is promising. With advances in deep learning, 
    generative AI, and large language models, we can expect more sophisticated AI 
    systems that can understand and generate human-like text, images, and other content.
    """
    
    for line in content.strip().split('\n'):
        if y < 40:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)
        
        c.drawString(50, y, line)
        y -= 20
    
    c.save()
    print(f"✅ Sample PDF created: {pdf_path}")

if __name__ == "__main__":
    create_sample_pdf()