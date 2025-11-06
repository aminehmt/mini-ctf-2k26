from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

DB = "shellmates_fans.db"
app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        fan_code = request.form.get("fan_code", "")
        favorite_event = request.form.get("favorite_event", "")

        # Messages d'erreur amusants selon le contenu
        if "'" in fan_code or "'" in favorite_event:
            error = "🤔 Tiens tiens... des guillemets simples ? Tu as l'air de bien connaître les bases de données !"
        elif "=" in fan_code or "=" in favorite_event:
            error = "🎯 Le signe égal... Un grand classique ! Tu es sur la bonne voie..."
        elif "OR" in fan_code.upper() or "OR" in favorite_event.upper():
            error = "👀 OR... not OR ? That is the question !"
        
        # VULN: Injection SQL avec un petit twist sur le thème fan club
        query = f"""
            SELECT 
                CASE 
                    WHEN is_vip = 1 THEN 'Super Fan VIP'
                    ELSE 'Fan Standard'
                END as rang,
                nickname,
                is_vip
            FROM shellmates_fans 
            WHERE fan_code = '{fan_code}' 
            AND favorite_event = '{favorite_event}'
            -- Seuls les vrais fans connaissent la magie des bases de données !
        """
        
        conn = get_db()
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        conn.close()

        if row:
            nickname = row["nickname"]
            is_vip = row["is_vip"]
            if is_vip:
                with open("flag.txt", "r") as f:
                    flag = f.read().strip()
                return render_template("vip_lounge.html", flag=flag, nickname=nickname)
            else:
                return render_template("regular_fan.html", nickname=nickname)
        else:
            error = "Code de fan ou événement incorrect ! Es-tu vraiment un fan de Shellmates ? 🤔"

    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
