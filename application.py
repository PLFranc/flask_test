from flask import Flask, render_template
from get_data import get_match


application = Flask(__name__)
app = application


# class Match():
#     __tablename__ = 'match'
#     id = db.column(db.Integer,primary_key = True)
#     tournoi = db.column(db.VARCHAR, unique = False)
#     date = db.column(db.TIMESTAMP, unique = False)
#     player_1_name = db.column(db.VARCHAR, unique = False)
#     player_1_odd = db.column(db.REAL, unique = False)
#     player_1_rank = db.column(db.Integer, unique = False)
#     player_1_prediction = db.column(db.REAL, unique = False)
#     player_2_name = db.column(db.VARCHAR, unique = False)
#     player_2_odd = db.column(db.REAL, unique = False)
#     player_2_rank = db.column(db.Integer, unique = False)
#     player_2_prediction = db.column(db.REAL, unique = False)
#
#     def __init__(self, id, tournoi, date, player_1_name, player_1_odd, player_1_rank, player_1_prediction,
#                  player_2_name, player_2_odd, player_2_rank, player_2_prediction):
#         self.id = id
#         self.tournoi = tournoi
#         self.date = date
#         self.player_1_name = player_1_name
#         self.player_1_odd = player_1_odd
#         self.player_1_rank = player_1_rank
#         self.player_1_prediction = player_1_prediction
#         self.player_2_name = player_2_name
#         self.player_2_odd = player_2_odd
#         self.player_2_rank = player_2_rank
#         self.player_2_prediction = player_2_prediction



@application.route('/')
def index():
    return render_template('index.html')

@application.route('/pronoo')
def pronoo():
    matchs = get_match()
    return render_template('pronoo.html', matchs = matchs)


if __name__ == '__main__':

    application.run(debug=True)
