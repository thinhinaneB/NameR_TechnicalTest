from flask import Flask, request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/dataset"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
UPLOAD_DIRECTORY = "/files"



class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    latest = db.Column(db.String())
    

    def __init__(self, title, latest):
        self.title = title
        self.latest = latest

    def __repr__(self):
        return "<Item " +self.title


@app.route('/')
def hello():
	return {"hello": "world"}


@app.route('/items', methods=[ 'GET'])
def handle_items():

        items = ItemModel.query.all()
        results = [
            {
                "title": item.title,
                "model": item.latest
            } for item in items]

        return {"count": len(results), "items": results, "message": "success"}


@app.route("/items/<path:path>",methods=[ 'GET'])
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)