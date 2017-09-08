from flask import Flask
from flask import request
app = Flask(__name__)
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from index import vectorizer, filename
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from goose import Goose
from requests import get

@app.route('/api/get_response', methods=["POST"])
def send_response():
	response = get(request.data)
	extractor = Goose()
	article = extractor.extract(raw_html=response.content)
	text = [article.cleaned_text]
	data_vector = vectorizer.transform(text)
	loaded_model = pickle.load(open(filename, 'rb'))
	if (loaded_model.predict(data_vector) == [0]):
		return "Left wing"
	if (loaded_model.predict(data_vector) == [1]):
		return "Right wing"
