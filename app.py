from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan")
def scan():
    return render_template("scan.html")



@app.route("/scan_result", methods=["POST"])
def scan_result():
    scores = [82, 65, 90, 74, 58]
    advices = [
        "食物繊維をもう少し増やすと、腸がもっと元気になります！",
        "水分をしっかりとって、腸の動きをサポートしましょう！",
        "発酵食品を取り入れて、善玉菌を増やしましょう！",
        "運動不足に注意！腸の動きにも影響します。",
        "ヤーコンを食べると腸内環境が改善されますよ！",
    ]
    comments = [
        "おおっ、なかなかの腸元気度だね！",
        "うーん、もう少し頑張れるかも？",
        "素晴らしい！腸内環境が整ってるよ！",
        "ちょっと悪玉菌が元気すぎるかも…",
        "ヤーコンパワーで腸を元気にしよう！",
    ]

    index = random.randint(0, len(scores) - 1)
    session["score"] = scores[index]
    session["advice"] = advices[index]
    session["comment"] = comments[index]

    return redirect(url_for("battle"))


@app.route("/battle")
def battle():
    score = session.get("score", "未スキャン")
    advice = session.get("advice", "アドバイスなし")
    comment = session.get("comment", "コメントなし")

    result = {
        "status": "victory",
        "enemy": "悪玉菌Z",
        "strategy": "ヤーコンファイバーで包囲攻撃！",
        "outcome": "腸内環境が改善されました！",
        "character": "YAKONMAN",
    }

    return render_template("battle.html", score=score, advice=advice, comment=comment, result=result)


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


if __name__ == "__main__":
    app.run(debug=True)
