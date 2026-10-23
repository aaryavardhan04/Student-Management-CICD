from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Aarya Vardhan", "roll_no": "192", "course": "CSE-AIML"},
    {"id": 2, "name": "Sahil Waghe", "roll_no": "193", "course": "CSE-AIML"}
]

@app.route("/")
def get_students():
    return jsonify({"status": "success", "students": students}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)