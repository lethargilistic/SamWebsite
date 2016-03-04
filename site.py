from weppy import App, url
app = App(__name__)

@app.route("/(index)?")
def index():
    return dict()

@app.route("/writings")
def writings():
    return dict()

@app.route("/imagery")
def imagery():
    return dict()

@app.route("/videos")
def videos():
    return dict()

@app.route("/recent")
def recent():
    return dict()

@app.route("/stylesheets/<str:sheetname>")
def get_stylesheet(sheetname):
    if sheetname:
        return url('static', sheetname) 
    else:
        return None

if __name__ == "__main__":
    app.run()
