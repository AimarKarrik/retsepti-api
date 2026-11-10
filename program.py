from flask import Flask
import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False
    return True

recepie_file_path = 'recepies.json'
recepies = read_json_file(recepie_file_path)

app = Flask(__name__)

@app.route("/")
def get_all_recepies():
    return recepies

@app.route("/recepie/<int:recepie_id>")
def get_recepie_by_id(recepie_id):
    for recepie in recepies:
        if recepie.get('id') == recepie_id:
            return recepie
    return None