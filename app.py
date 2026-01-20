from flask import Flask, render_template, request
from careers import careers

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["interests"].lower()

        career_scores = {}

        for career, keywords in careers.items():
            score = 0
            for word in keywords.split():
                if word in user_input:
                    score += 1

            if score > 0:
                career_scores[career] = score

        # Sort careers by score (highest first)
        sorted_careers = sorted(
            career_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Take top 5 careers
        top_careers = [career for career, score in sorted_careers[:5]]

        # Fallback if nothing matches
        if not top_careers:
            top_careers = [
                "Software Developer",
                "Graphic Designer",
                "Content Writer / Blogger",
                "Digital Marketer",
                "Teacher / Professor"
            ]

        return render_template("result.html", careers=top_careers)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
