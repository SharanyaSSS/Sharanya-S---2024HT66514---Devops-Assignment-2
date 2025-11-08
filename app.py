from flask import Flask, render_template, request, redirect

app = Flask(__name__)
workouts = []

@app.route('/')
def index():
    return '''
        <h2>Add Workout</h2>
        <form method="post" action="/add">
            Workout: <input name="workout"><br>
            Duration: <input name="duration"><br>
            <input type="submit" value="Add Workout">
        </form>
        <a href="/workouts">View Workouts</a>
    '''

@app.route('/add', methods=['POST'])
def add_workout():
    workout = request.form['workout']
    duration = request.form['duration']
    if workout and duration.isdigit():
        workouts.append({'workout': workout, 'duration': int(duration)})
    return redirect('/workouts')

@app.route('/workouts')
def view_workouts():
    html = '<h2>Logged Workouts</h2><ul>'
    for w in workouts:
        html += f"<li>{w['workout']} - {w['duration']} minutes</li>"
    html += '</ul><a href="/">Back</a>'
    return html

if __name__ == '__main__':
    app.run(debug=True)
