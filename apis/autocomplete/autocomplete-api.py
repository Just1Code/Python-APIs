from english_words import get_english_words_set as words
from flask import Flask, jsonify

word_set = words(['web2'], lower=True)
app = Flask(__name__)

def autocomplete(prefix, limit=20):
    prefix = prefix.lower()
    suggestions = [word for word in word_set if word.startswith(prefix)]
    count = len(suggestions)
    truncated_result = count > limit
    suggestions = suggestions[:limit] if truncated_result else suggestions
    return jsonify(
        words=suggestions,
        count=count,
        truncated_result=truncated_result
    )

@app.route("/autocomplete/<prefix>")
def autocomp_api(prefix):
    return autocomplete(prefix)

if __name__ == "__main__":
    app.run(port=8080, debug=True)