from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>NovaSpace | My Digital World</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #101322;
            color: #f5f6ff;
        }
		
        header {
            padding: 22px;
            text-align: center;
            background: #191e36;
            border-bottom: 2px solid #8b5cf6;
        }

        header h1 {
            margin: 0;
            color: #bda5ff;
            letter-spacing: 2px;
        }

        header p {
            color: #c5c9df;
        }

        main {
            max-width: 850px;
            margin: auto;
            padding: 25px 18px;
        }

        .hero {
            padding: 35px 22px;
            text-align: center;
            background: linear-gradient(
                135deg, #242c52, #45246a
            );
            border-radius: 20px;
        }

        .hero h2 {
            font-size: 30px;
            margin-top: 0;
        }

        .hero p {
            line-height: 1.7;
            color: #e0def8;
        }

        button {
            padding: 13px 20px;
            margin-top: 12px;
            border: none;
            border-radius: 10px;
            background: #b49aff;
            color: #171126;
            font-weight: bold;
            font-size: 15px;
        }

        button:active {
            transform: scale(0.97);
        }

        .section-title {
            margin-top: 30px;
            color: #bda5ff;
        }

        .cards {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(210px, 1fr));
            gap: 15px;
        }

        .card {
            padding: 20px;
            background: #1b2038;
            border: 1px solid #353c60;
            border-radius: 15px;
        }

        .card h3 {
            color: #c9b8ff;
        }

        .card p {
            color: #c5c9df;
            line-height: 1.6;
        }

        #message {
            min-height: 25px;
            color: #d7c9ff;
            font-weight: bold;
        }

        footer {
            padding: 25px;
            text-align: center;
            color: #aeb4ce;
            font-size: 13px;
        }
    </style>
</head>

<body>

<header>
    <h1>NOVASPACE</h1>
    <p>A little corner of the internet</p>
</header>

<main>

    <section class="hero">
        <h2>Welcome to My World 🚀</h2>

        <p>
            This is my own digital space, built with
            Python, HTML, CSS and creativity.
            New ideas begin here.
        </p>

        <button onclick="welcomeMessage()">
            Explore My Website
        </button>

        <p id="message"></p>
    </section>

    <h2 class="section-title">Explore NovaSpace</h2>

    <section class="cards">

        <article class="card">
            <h3>💡 My Ideas</h3>
            <p>
                A place for interesting thoughts,
                creative projects and future plans.
            </p>
        </article>

        <article class="card">
            <h3>💻 My Coding</h3>
            <p>
                Learning to build digital experiences
                one line of code at a time.
            </p>
        </article>

        <article class="card">
            <h3>🌟 My Goals</h3>
            <p>
                Growing my skills, learning new things
                and turning ideas into reality.
            </p>
        </article>

    </section>

</main>

<footer>
    Created with Python Flask · NovaSpace
</footer>

<script>
    function welcomeMessage() {
        document.getElementById("message").textContent =
            "Welcome, explorer! Your journey starts here.";
    }
</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

@app.route('/study-guides')
def study_guides():
    return render_template('study_guides.html')