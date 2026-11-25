from flask import Flask, render_template, request
import pyautogui as auto
import webview

from datetime import date
import os
import sys


if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'teplates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__,template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)



def abrir_terminal(repositorio):
    auto.hotkey('win','r')
    auto.write('cmd')
    auto.press('enter')
    auto.write(f'cd {repositorio}')
    auto.press('enter')

def commitar(hoje):
    auto.write("git add .")
    auto.press('enter')
    auto.write(f'git commit -m "Commit do dia: {hoje}"')
    auto.press('enter')
    auto.write('git push')
    auto.press('enter')
    auto.sleep(3)
    auto.write('exit')
    auto.press('enter')

@app.route("/", methods = ['GET', 'POST'])
def index():
    hoje = date.today().strftime("%d/%m/%Y")
    repositorio = None
    if request.method == 'POST':
        repositorio = request.form.get("repositorio","")
        auto.PAUSE = 1
        abrir_terminal(repositorio)
        commitar(hoje)
    return render_template("index.html")


if __name__ == "__main__":
    window = webview.create_window(
        title="Vagner's Gitergeist v2.0",
        url=app,
        width=1000,
        height=700
    )

    webview.start()
    