from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json, random, os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

DATA_FILE = "participants.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/add", response_class=HTMLResponse)
def add_participant(name: str = Form(...)):
    data = load_data()
    data.append(name.strip())
    save_data(data)
    return f"""
    <html>
    <head>
        <title>INOVACIV - Confirmação</title>
        <style>
            body {{
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                text-align: center;
            }}
            a {{
                color: #fff;
                background: rgba(255, 255, 255, 0.2);
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
                transition: 0.3s;
            }}
            a:hover {{
                background: rgba(255, 255, 255, 0.4);
            }}
        </style>
    </head>
    <body>
        <h2>{name} foi adicionado com sucesso!</h2>
        <a href="/">Voltar</a>
    </body>
    </html>
    """

@app.get("/draw", response_class=HTMLResponse)
def draw_names():
    data = load_data()
    if not data:
         return """
        <html>
        <head>
            <title>INOVACIV - Erro</title>
            <style>
                body {
                    background: linear-gradient(135deg, #6a11cb, #2575fc);
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    text-align: center;
                }
                a {
                    color: #fff;
                    background: rgba(255, 255, 255, 0.2);
                    padding: 10px 20px;
                    border-radius: 8px;
                    text-decoration: none;
                    transition: 0.3s;
                }
                a:hover {
                    background: rgba(255, 255, 255, 0.4);
                }
            </style>
        </head>
        <body>
            <h2>Nenhum participante cadastrado.</h2>
            <a href="/">Voltar</a>
        </body>
        </html>
        """

    random.shuffle(data)
    result = """
    <html>
    <head>
        <title>INOVACIV - Resultado</title>
        <style>
            body {
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                text-align: center;
            }
            ol {
                list-style: none;
                padding: 0;
            }
            li {
                background: rgba(255, 255, 255, 0.2);
                margin: 8px 0;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 1.2em;
            }
            a {
                color: #fff;
                background: rgba(255, 255, 255, 0.2);
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
                transition: 0.3s;
                margin-top: 20px;
            }
            a:hover {
                background: rgba(255, 255, 255, 0.4);
            }
        </style>
    </head>
    <body>
        <h2>Ordem do sorteio 🎉</h2>
        <ol>
    """
    for i, name in enumerate(data, start=1):
        result += f"<li>{i}º — {name}</li>"
    result += """
        </ol>
    </body>
    </html>
    """
    return result
