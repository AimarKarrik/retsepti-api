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

recipe_file_path = 'recipes.json'
recipes = read_json_file(recipe_file_path)

app = Flask(__name__)

@app.route("/")
def get_all_recipes():
    return recipes

@app.route("/recipe/<int:recipe_id>")
def get_recipe_by_id(recipe_id):
    for recipe in recipes:
        if recipe.get('id') == recipe_id:
            return recipe
    return {"error": "Retsepti ei leitud"}, 404