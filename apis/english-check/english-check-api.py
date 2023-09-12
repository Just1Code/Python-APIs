from english_words import get_english_words_set as words
from flask import Flask, jsonify

word_set = words(['web2'], lower=True)
app = Flask(__name__)

def is_english(word):
    return True if word in word_set else False

@app.route("/<word>")
def engcheck_api(word):
    word = word.lower()
    return jsonify(
        found = is_english(word),
        word = word,
        length = len(word)
    )

if __name__ == "__main__":
    app.run(port=8080, debug=True)