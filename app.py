from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Name Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .form-container {
            background: white;
            padding: 20px 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        input[type="text"] {
            padding: 10px;
            width: 100%;
            margin-top: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        input[type="submit"] {
            padding: 10px 15px;
            background-color: #007BFF;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

    <div class="form-container">
        <form action="/greet" method="POST">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" placeholder="Your name" required>

            <input type="submit" value="Submit">
        </form>
    </div>

</body>
</html>
"""

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['name']
    return f"Welcome {username} to our flask application"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)