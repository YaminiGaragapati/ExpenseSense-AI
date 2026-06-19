from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

def get_category(name):
    name = name.lower()

    if name in ["pizza", "burger", "food"]:
        return "Food"

    elif name in ["petrol", "fuel", "bus"]:
        return "Transport"

    elif name in ["netflix", "movie", "game"]:
        return "Entertainment"

    elif name in ["book", "course"]:
        return "Education"

    return "Other"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():

    name = request.form["name"]
    amount = float(request.form["amount"])

    category = get_category(name)

    expenses.append((name, amount, category))

    total = sum(x[1] for x in expenses)

    category_total = {}

    for e in expenses:
        category_total[e[2]] = category_total.get(e[2], 0) + e[1]

    highest = max(category_total, key=category_total.get)

    recommendation = (
        f"Most spending is on {highest}. Consider reducing expenses in this category."
    )

    result = {
        "name": name,
        "category": category,
        "amount": amount,
        "total": total,
        "recommendation": recommendation
    }

    return render_template("index.html", result=result)


if __name__ == "__main__":
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)