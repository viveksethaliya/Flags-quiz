# import os
# import random
# from flask import Flask, render_template, request, jsonify

# # app = Flask(__name__)
# app =Flask(__name__,template_folder="templates", static_folder='static')
# FLAGS_FOLDER = "static/img"

# def get_country_list(folder):
#     return [filename.split('.')[0] for filename in os.listdir(folder) if filename.endswith('.png')]

# countries = get_country_list(FLAGS_FOLDER)
# remaining_flags = countries.copy()

# @app.route('/')
# def index():
#     return render_template('index.html', total_rounds=min(40, len(countries)))

# @app.route('/next_round', methods=['POST'])
# def next_round():
#     if len(countries) < 4:
#         return jsonify({"error": "Not enough flags available."})

#     current_country = random.choice(countries)

#     options = random.sample(countries, 3)

#     if current_country not in options:
#         options.append(current_country)

#     random.shuffle(options)

#     return jsonify({
#         "flag": f"{FLAGS_FOLDER}/{current_country}.png",
#         "options": options,
#         "answer": current_country
#     })

# @app.route('/submit_answer', methods=['POST'])
# def submit_answer():
#     data = request.json
#     user_answer = data.get('answer')
#     correct_answer = data.get('correct_answer')

#     if not user_answer or not correct_answer:
#         return jsonify({"error": "Invalid input."})

#     is_correct = (user_answer == correct_answer)
#     return jsonify({"is_correct": is_correct})

# if __name__ == "__main__":
#     app.run(debug=True)
import os
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates", static_folder='static')
FLAGS_FOLDER = "static/img"

# Load the list of countries (flags)
def get_country_list(folder):
    return [filename.split('.')[0] for filename in os.listdir(folder) if filename.endswith('.png')]

countries = get_country_list(FLAGS_FOLDER)
remaining_flags = countries.copy()  # Create a copy for tracking unused flags

@app.route('/')
def index():
    return render_template('index.html', total_rounds=min(40, len(countries)))

@app.route('/next_round', methods=['POST'])
def next_round():
    global remaining_flags

    # Reset the remaining flags if all have been used
    if not remaining_flags:
        remaining_flags = countries.copy()

    if len(remaining_flags) < 4:
        return jsonify({"error": "Not enough flags available."})

    # Pick a current country and remove it from remaining flags
    current_country = random.choice(remaining_flags)
    remaining_flags.remove(current_country)

    # Pick 3 random options
    options = random.sample([c for c in countries if c != current_country], 3)

    # Add the correct answer to the options and shuffle
    options.append(current_country)
    random.shuffle(options)

    return jsonify({
        "flag": f"{FLAGS_FOLDER}/{current_country}.png",
        "options": options,
        "answer": current_country
    })

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    user_answer = data.get('answer')
    correct_answer = data.get('correct_answer')

    if not user_answer or not correct_answer:
        return jsonify({"error": "Invalid input."})

    is_correct = (user_answer == correct_answer)
    return jsonify({"is_correct": is_correct})

if __name__ == "__main__":
    app.run(debug=True)
