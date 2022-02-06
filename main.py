import pickle
from flask import Flask, render_template

from ResultVO import ResultVO
from gacha import single_gacha, eleven_gacha

app = Flask(__name__, static_url_path="/static")


def init_result():
    return ResultVO()


"""
複数人数での利用は考慮していません
"""


def load_rireki():
    try:
        with open('./rireki.pickle', 'rb') as f:
            result = pickle.load(f)
    except:
        result = init_result()

    return result


"""複数人数での利用は考慮していません"""


def save_rireki(rireki):
    with open('./rireki.pickle', 'wb') as f:
        pickle.dump(rireki, f)

    return rireki


# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    result = load_rireki()
    save_rireki(result)
    return render_template("index.html", result=result)


@app.route('/gacha-one', methods=["GET", "POST"])
def gacha_single():
    result = load_rireki()
    gacha_results = single_gacha()
    for gacha_result in gacha_results:
        result.gacha_rireki[gacha_result["rarity"]].append(
            gacha_result["item"])
    result.total_count += 1
    result.price += 100
    result.single_gacha_count += 1
    save_rireki(result)

    return render_template("index.html",
                           result=result,
                           gacha_results=gacha_results)


@app.route('/gacha-eleven', methods=["GET", "POST"])
def gacha_eleven():
    result = load_rireki()
    gacha_results = eleven_gacha()
    for gacha_result in gacha_results:
        result.gacha_rireki[gacha_result["rarity"]].append(
            gacha_result["item"])
    result.total_count += 11
    result.price += 1000
    result.eleven_gacha_count += 1
    save_rireki(result)

    return render_template("index.html",
                           result=result,
                           gacha_results=gacha_results)


@app.route('/srplus-endless-11', methods=["GET", "POST"])
def srplus_complete_eleven():
    result = load_rireki()
    is_complete = False
    gacha_results = []
    count = 0
    while not is_complete:
        gacha_results.extend(eleven_gacha())
        for gacha_result in gacha_results:
            result.gacha_rireki[gacha_result["rarity"]].append(
                gacha_result["item"])
        result.total_count += 11
        result.price += 1000
        result.eleven_gacha_count += 1
        is_complete = len(list(set(result.gacha_rireki["SR+"]))) == 10
        count += 1
        # 最悪のケースに備えて10000回で試行回数を止める
        if count >= 10000:
            break
    save_rireki(result)

    return render_template("index.html",
                           result=result,
                           gacha_results=gacha_results)


@app.route('/srplus-endless-1', methods=["GET", "POST"])
def srplus_complete_single():
    result = load_rireki()
    is_complete = False
    gacha_results = []
    count = 0
    while not is_complete:
        gacha_results.extend(single_gacha())
        for gacha_result in gacha_results:
            result.gacha_rireki[gacha_result["rarity"]].append(
                gacha_result["item"])
        result.total_count += 1
        result.price += 100
        result.single_gacha_count += 1
        is_complete = len(list(set(result.gacha_rireki["SR+"]))) == 10
        count += 1
        # 最悪のケースに備えて10000回で試行回数を止める
        if count >= 10000:
            break
    save_rireki(result)

    return render_template("index.html",
                           result=result,
                           gacha_results=gacha_results)


@app.route('/reset', methods=["GET", "POST"])
def reset():
    result = save_rireki(init_result())
    return render_template("index.html", result=result)


app.run(host='0.0.0.0', debug=True)
