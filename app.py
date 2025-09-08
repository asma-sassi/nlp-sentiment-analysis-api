
from flask import Flask, request, jsonify 
import spacy 

#load NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)


@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
	text = request.json.get('text')
	if not text:
		return jsonify({"error": "No text provided"}), 400 


	doc = nlp(text)

	entities = [(ent.text, ent.label_) for ent in doc.ents]
	
	sentiment = "neutral" 
	for sent in doc.sents: 
		if "good" in sent.text.lower():
			sentiment = "positive"
		elif "bad" in sent.text.lower():
			sentiment = "negative"

	return jsonify({
		"sentiment": sentiment,
		"entities": entities,
		 "text": text
	})

if __name__ == '__main__':
	app.run(debug=True)		