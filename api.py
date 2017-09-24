import pickle
from flask import Flask
from flask import request
from index import vectorizer, filename
from goose import Goose
from requests import get

app = Flask(__name__)


@app.route('/api/get_response', methods=["POST"])
def send_response():
    response = get(request.data)
    extractor = Goose()
    article = extractor.extract(raw_html=response.content)
    text = [article.cleaned_text]
    data_vector = vectorizer.transform(text)
    loaded_model = pickle.load(open(filename, 'rb'))
    if loaded_model.predict(data_vector) == [0]:
        return "Left wing"
    if loaded_model.predict(data_vector) == [1]:
        return "Right wing"

if __name__ == "__main__":
    app.run(host='0.0.0.0')        
