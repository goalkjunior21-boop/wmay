from flask import Flask, render_template, request, redirect, url_for, session
import secrets

from michel_quiz import QUESTIONS, empty_traits, add_traits, rank_michels, pick_punchlines


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def _init_quiz():
    session["q_idx"] = 0
    session["traits"] = empty_traits()
    session["answers"] = []  # store (question_id, option_key) if you want

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        _init_quiz()
        return redirect(url_for("question"))
    return render_template("home.html", total_questions=len(QUESTIONS))

@app.route("/question", methods=["GET", "POST"])
def question():
    # Safety init (if user refreshes / lands here directly)
    if "q_idx" not in session or "traits" not in session:
        _init_quiz()

    q_idx = session["q_idx"]

    # Finished?
    if q_idx >= len(QUESTIONS):
        return redirect(url_for("result"))

    q = QUESTIONS[q_idx]

    if request.method == "POST":
        chosen = request.form.get("option")  # expects "A"/"B"/"C"/"D"
        option = next((o for o in q.options if o.key == chosen), None)
        if option:
            session["traits"] = add_traits(session["traits"], option.delta)
            session["answers"] = session.get("answers", []) + [(q.id, option.key)]
            session["q_idx"] = q_idx + 1
        return redirect(url_for("question"))

    return render_template(
        "question.html",
        q_idx=q_idx,
        total=len(QUESTIONS),
        question=q
    )

@app.route("/result")
def result():
    if "traits" not in session:
        return redirect(url_for("home"))

    ranked = rank_michels(session["traits"])  # list[(Michel, score)] sorted desc
    winner, winner_score = ranked[0]

    punchlines = pick_punchlines(winner.id, session["traits"])


    # Convert scores to non-negative for percentage display
    scores = [s for _, s in ranked]
    min_score = min(scores)
    shifted = [s - min_score for s in scores]  # now min is 0

    total = sum(shifted) if sum(shifted) != 0 else 1
    all_percent = []
    for (m, s), sh in zip(ranked, shifted):
        pct = 100 * sh / total
        all_percent.append((m, s, pct))

    # Top 3 for quick list (rounded)
    top3 = [(m, s, round(p)) for (m, s, p) in all_percent[:3]]

    # Full list (rounded to 1 decimal; also include bar width)
    full = [(m, s, round(p, 1)) for (m, s, p) in all_percent]

    return render_template(
        "result.html",
        winner=winner,
        winner_score=winner_score,
        top3=top3,
        full=full,
        traits=session["traits"],
        punchlines=punchlines
    )

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
