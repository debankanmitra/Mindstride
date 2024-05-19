# Mindstride
🌟 Mindstride is a RAG-based chat assistant designed to support mental health, personal growth, and self-improvement. This project leverages advanced AI technologies to provide a personalized and insightful experience, drawing from the wisdom of over 70 books on mental well-being, personal development, and self-discovery.

## 🚀 Features
- Mental Health Support: Offers guidance and support for enhancing mental well-being.
- Personal Growth: Assists users on their journey towards personal development.
- Self-Improvement: Provides tools and insights for self-discovery and improvement.

## 🛠️ Tech Stack
- Backend: FastAPI
- Vector Database: Pinecone
- Embeddings: Generated from 70+ books on relevant topics
- Langchain: For managing and querying text chains
- APIs:
 - OpenAI API: Queries using GPT-3.5
 - Hugging Face Inference API: For creating embeddings
- Infrastructure: Hosted on AWS Lambda

## 📦 Installation
1. Clone the repository:
   ```
   git clone https://github.com/debankanmitra/GenaiAssistant.git
   cd backend
   ```
3. Set up a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
7. Configure environment variables for Pinecone, OpenAI API, and Hugging Face Inference API keys.
8. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

## 📄 License
Mindstride is licensed under the MIT License.
