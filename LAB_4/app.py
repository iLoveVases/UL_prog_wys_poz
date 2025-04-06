from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks_page():
    global task_id
    if request.method == 'POST':
        content = request.form['content']
        if content:
            tasks.append({'id': task_id, 'content': content, 'done': False})
            task_id += 1
        return redirect(url_for('tasks_page'))

    return render_template('tasks.html', tasks=tasks)

@app.route('/done/<int:id>')
def mark_done(id):
    for task in tasks:
        if task['id'] == id:
            task['done'] = True
    return redirect(url_for('tasks_page'))

@app.route('/delete/<int:id>')
def delete(id):
    global tasks
    tasks = [t for t in tasks if t['id'] != id]
    return redirect(url_for('tasks_page'))

if __name__ == '__main__':
    app.run(debug=True)
