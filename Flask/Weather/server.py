from flask import Flask, render_template

from py_news import get_news
from weather import weather_by_city

app = Flask(__name__)

@app.route("/")
def index():
    title = "Новости Python"
    news_list = get_news()
    weather = weather_by_city('Krasny Luch,Ukraine')
    return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

if __name__ == "__main__":
    app.run(debug=True)