from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("expenses.csv")

    total_spent = df["amount"].sum()
    avg_spent = df["amount"].mean()
    by_category = (
        df.groupby("category")["amount"]
        .sum()
        .reset_index()
        .to_dict(orient="records")
    )

    return render_template(
        "index.html",
        total=round(total_spent, 2),
        average=round(avg_spent, 2),
        categories=by_category
    )

if __name__ == "__main__":
    app.run(debug=True)
