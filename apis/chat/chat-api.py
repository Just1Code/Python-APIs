from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

def timestamp():
    utc = datetime.now(pytz.UTC)
    return utc.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

messages = [
    {
        "id": 1,
        "author": "Eduard",
        "content": "Good evening dear sir",
        "channel": "general",
        "created_at": "2023-09-06T14:23:26.104Z",
        "updated_at": "2023-09-06T14:23:26.104Z",
    },
    {
        "id": 2,
        "author": "Smith",
        "content": "Hey",
        "channel": "general",
        "created_at": "2023-09-06T14:23:49.323Z",
        "updated_at": "2023-09-06T14:23:49.323Z",
    },
]

@app.route('/<channel>/messages', methods=['GET'])
def get_messages(channel):
    channel_messages = [message for message in messages if message["channel"] == channel]
    response_data = {
        "channel": channel,
        "messages": channel_messages,
    }
    return jsonify(response_data)

@app.route('/<channel>/messages', methods=['POST'])
def post_comment(channel):
    data = request.get_json()
    if not data or "author" not in data or "content" not in data:
        return jsonify({"error": "Invalid request data"}), 400

    new_message = {
        "id": len(messages) + 1,
        "author": data["author"],
        "content": data["content"],
        "channel": channel,
        "created_at": timestamp(),
        "updated_at": timestamp(),
    }
    messages.append(new_message)

    return jsonify(new_message), 201

if __name__ == '__main__':
    app.run(port=8080, debug=True)

# curl command for testing:
#  curl -X POST -H "Content-Type: application/json" -d '{
#     "author": "Seb",
#     "content": "Yo Yo Yo"
# }' http://pc:8080/general/messages
