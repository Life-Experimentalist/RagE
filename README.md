# RagE - Insurance Policy Analysis Engine

## Overview
RagE (Retrieval Augmented Generation Engine) is an intelligent system designed specifically for the insurance industry. It leverages FastAPI and retrieval-augmented generation to help insurance professionals and customers quickly find, understand, and analyze insurance policies, claims procedures, and coverage details.

## Key Features
- **Policy Document Analysis**: Upload and analyze insurance policy documents
- **Natural Language Queries**: Ask questions about policies in plain English
- **Coverage Comparison**: Compare different policies and their coverage details
- **Claims Assistance**: Get guidance on claims procedures and requirements
- **Regulatory Compliance**: Stay updated with insurance regulations and compliance requirements

## Technical Architecture
- **FastAPI Backend**: High-performance API framework
- **RAG Pipeline**: Enhanced document retrieval and analysis
- **Vector Database**: Efficient semantic search for insurance-specific content
- **Multi-Database Support**: Works with PostgreSQL, MySQL, SQLite
- **Responsive UI**: Clean, modern interface for all devices

## Why RAG for Insurance?
Insurance documents are dense, complex, and filled with specialized terminology. Traditional search approaches often fail to capture the nuanced relationships between insurance concepts. Our RAG system:

- Understands insurance-specific terminology and concepts
- Provides accurate answers by retrieving relevant policy sections
- Reduces time spent searching through lengthy policy documents
- Ensures responses are grounded in actual policy language
- Helps both insurance professionals and customers understand complex coverage details

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Docker (optional, for containerization)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/RagE.git
   cd RagE
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables by copying the example:
   ```
   cp .env.example .env
   ```

4. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

5. In a separate terminal, run the Pathway pipeline:
   ```
   python pathway_pipeline.py
   ```

6. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## API Usage

### Query the RAG System