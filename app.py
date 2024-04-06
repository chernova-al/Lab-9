from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('game_task')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    played = db.Column(db.String(100))
    release = db.Column(db.String(20))
    ready = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Game {self.id} / {self.release}> {self.played}'

@app.route('/')
def main():
    games = Game.query.all()
    print(games)
    return render_template('index.html', game_list=games)

@app.route('/ready/<int:game_id>', methods=['PATCH'])
def modify(game_id):
    game = Game.query.get(game_id)
    game.ready = request.json['ready']
    db.session.commit()
    return 'Ok'

@app.route('/play', methods=['POST'])
def create_game():
    data = request.json
    game = Game(**data)
    db.session.add(game)
    db.session.commit()
    return 'Ok'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
