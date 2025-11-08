from flask import Flask, request, redirect, render_template

app = Flask(__name__)
workouts = []

@app.route('/')
def index():
    return render_template('index.html', workouts=workouts)

@app.route('/add', methods=['POST'])
def add_workout():
    workout = request.form['workout']
    duration = request.form['duration']
    if workout and duration.isdigit():
        workouts.append({'workout': workout, 'duration': int(duration)})
    return redirect('/')

