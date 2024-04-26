from flask import Flask, render_template, request

app = Flask(__name__, template_folder="C:\pythonProject1\site/templates/")

@app.route('/')
def index():
    return render_template('form.html')


@app.route('/result', methods=['GET'])
def result():
    year = request.args.get('year')

    murders = {'2020': 8722,
               '2021': 8174,
               '2022': 7626,
               '2023': 7078,
               '2024': 6530,
               '2025': 5981,
               '2026': 5433,
               '2027': 4885,
               '2028': 4337,
            '2009': 17681,
            '2010': 15563,
            '2011': 14305,
            '2012': 13265,
            '2013': 12361,
            '2014': 11933,
            '2015': 11496,
            '2016': 10444,
            '2017': 9738,
            '2018': 8574,
            '2019': 7948}

    if year in murders:
        return render_template('pred_murders.html', year=year, murder=murders[year])
    else:
        return render_template('error.html')



if __name__ == '__main__':
    app.run(debug=True)
