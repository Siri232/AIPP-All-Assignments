from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        print("Username:", username)  # prints in terminal
        return "<h1>Welcome, " + username + "!</h1>"
    return """
    <form method="post">
      <input name="username" placeholder="Username" required>
      <input name="password" type="password" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
    """

if __name__ == "__main__":
    app.run()