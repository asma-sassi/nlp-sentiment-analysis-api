# nlp-sentiment-analysis-api

# NLP API (Sentiment Analysis & NER)

Welcome to the NLP API! This simple API is built with **Flask** and **spaCy**, and it helps you analyze the sentiment of a text and identify named entities (NER). It’s perfect for understanding the vibe of a text or extracting key details like names, places, and more.

## Setup

**### 1. Clone the repository:**

```bash
git clone https://github.com/your-username/nlp-api.git
cd nlp-api

**### 2. Create and activate the virtual environment:**

For MacOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate

For Windows:
```bash
python -m venv venv
venv\Scripts\activate

**### 3. Install the dependencies:**

```bash
Copier le code
pip install -r requirements.txt

**### 4. Run the Flask API:**

```bash
python app.py

**Endpoints**
POST /analyze_sentiment
Request body:
Send a JSON object with the text you want to analyze.

json
{
  "text": "I am feeling good today!"
}

Response:
The API will return the sentiment (positive/negative/neutral) and entities (like people, places, or dates) found in the text.

json
{
  "sentiment": "positive",
  "entities": [["good", "ADJ"]],
  "text": "I am feeling good today!"
}

**Technologies Used**
**Flask**: A simple framework for building APIs
**spaCy:** A library for natural language processing (NLP)
**Transformers (Hugging Face):** Used for advanced NLP tasks like sentiment analysis
