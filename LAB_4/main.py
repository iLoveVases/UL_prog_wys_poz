# save this as app.py
from flask import Flask, render_template

users = {
1: {"name": "Ala", "age": 22},
2: {"name": "Bartek", "age": 25},
3: {"name": "Celina", "age": 30}
}
app = Flask(__name__)

@app.route("/")
def home():
    return """SIEMANO KOLANO<br>
       <a href='/about'>http://127.0.0.1:5000/about</a><br>
       <a href='/users'>http://127.0.0.1:5000/users</a>
    """

@app.route("/about")
def about():
    return "To jest prosty portal demo.<br><a href='/'>Powrót</a>"

@app.route("/users")
def user_list():
    text = "Lista użytkowników:<br>"
    for uid, user in users.items():
        text += f"<a href='/user/{uid}'>{user['name']}</a><br>"
    text += "<br><a href='/'>Powrót</a>"
    return text

@app.route("/user/<int:user_id>")
def user_profile(user_id):
    user = users.get(user_id)
    if user:
        return f"{user['name']}, {user['age']} lat<br><a href='/users'>Powrót</a>"
    else:
        return "Użytkownik nie istnieje<br><a href='/users'>Powrót</a>", 404

if __name__ == "__main__":
    app.run(debug=True)
