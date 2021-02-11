from flask import Flask, render_template
from get_data import get_match
import pandas as pd


application = Flask(__name__)
app = application


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/pronoo')
def pronoo():
    matchs = get_match()
    df = pd.DataFrame(matchs, columns=['id', 'date', 'tournament', 'player_1_name', 'player_1_rank', 'player_1_odd','player_1_prediction',

                                           'player_2_name', 'player_2_rank', 'player_2_odd', 'player_2_prediction'])
    df.drop(columns=['id'], inplace=True)
    df = df[['date', 'tournament', 'player_1_name','player_1_rank', 'player_1_odd',
                                           'player_1_prediction','player_2_prediction','player_2_odd','player_2_rank',
                                           'player_2_name']]
    list = df.values.tolist()
    print(list)

    return render_template('pronoo.html', matchs = list)



if __name__ == '__main__':

    application.run(debug=True)
