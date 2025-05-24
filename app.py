from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

# Game state
called_numbers = []
available_numbers = list(range(1, 91))
current_number = None
paused = False

@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        current_number=current_number,
        called_numbers=called_numbers,
        paused=paused
    )

@app.route('/call', methods=['POST'])
def call_number():
    global current_number, called_numbers, available_numbers
    if not paused and available_numbers:
        current_number = random.choice(available_numbers)
        available_numbers.remove(current_number)
        called_numbers.append(current_number)
    return redirect('/')

@app.route('/pause', methods=['POST'])
def pause_game():
    global paused
    paused = not paused  # Toggles pause ON/OFF
    return redirect('/')

@app.route('/restart', methods=['POST'])
def restart_game():
    global called_numbers, available_numbers, current_number, paused
    called_numbers = []
    available_numbers = list(range(1, 91))
    current_number = None
    paused = False
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
