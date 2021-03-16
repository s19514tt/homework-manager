from flask_cors import CORS
from flask import *
from flask import request
import re
import threading


app = Flask(__name__)
CORS(app)

HW_JSON_PATH = "./data/savedhw.json"

@app.route("/parse")
def parse():
    content = request.args.get('parseTxt')
    pattern = r'((.)(曜日)(\n)(.*?)(月 )([0-9]*)(, )([0-9]*)|(\n課題 )(.*?)( は、完了とマークされていません。\n)(.*?)( / )([\s\S]*?)(\n期限：)([0-9]*)(:)([0-9]*))'
    result = []
    monthArray = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]

    result.append(re.findall(pattern, content))
    hwarray = []
    date = ''
    for data in result[0]:
        if data[17] == '':
            date = {'year': int(data[8]), 'month': monthArray.index(data[4]), 'day': int(data[6])}
        else:
            hwarray.append({})
            hwarray[-1]['className'] = data[12]
            hwarray[-1]['homeworkName'] = data[10]
            hwarray[-1]['dueM'] = str(date['month']).zfill(2)
            hwarray[-1]['dueD'] = str(date['day']).zfill(2)
            hwarray[-1]['dueh'] = str(data[16]).zfill(2)
            hwarray[-1]['duem'] = str(data[18]).zfill(2)
    return jsonify({'parsedHomeworks': hwarray})


@app.route("/addnew")
def addnew():
    returnedHW = json.loads(request.args.get('hws'))
    for item in returnedHW["hwl"]:
        item.update({"status": False})

    def isDup(hwName, className):
        if('hwl' in df):
            for item in df['hwl']:
                if item['homeworkName'] == hwName and item['className'] == className:
                    print(hwName + ' is a duplicate.')
                    returnedHW['hwl'] = list(filter(lambda i: not (i['className'] ==
                                                                   className and i['homeworkName']) == hwName, returnedHW['hwl']))
                    break
    with open(HW_JSON_PATH, mode='r') as f:
        df = json.load(f)
        for item in returnedHW['hwl']:
            thread = threading.Thread(target=isDup, args=(item['homeworkName'], item['className'],))
            thread.start()
        if 'hwl' in df:
            df['hwl'] += returnedHW['hwl']
        else:
            df = returnedHW
    with open(HW_JSON_PATH, mode='w') as f:
        json.dump(df, f, ensure_ascii=False, indent=4)
        return jsonify({'result': 'success'})


@app.route("/hwlist")
def hwlist():
    with open(HW_JSON_PATH, mode='r') as f:
        k = json.load(f)
        k['hwl'] = sorted(k['hwl'], key=lambda x: (x['dueM'] * 1000000 +
                                                   x['dueD'] * 10000 + x['dueh'] * 100 + x['duem']))
        k['hwl'] = list(filter(lambda x: (x['status'] == False), k['hwl']))
        return jsonify(k)


@app.route("/hwDoneList")
def hwdonelist():
    with open(HW_JSON_PATH, mode='r') as f:
        k = json.load(f)
        k['hwl'] = sorted(k['hwl'], key=lambda x: (x['dueM'] * 1000000 +
                                                   x['dueD'] * 10000 + x['dueh'] * 100 + x['duem']))
        k['hwl'] = list(filter(lambda x: (x['status'] == True), k['hwl']))
        return jsonify(k)


@app.route("/markAsDone")
def markAsDone():
    nameOfTask = request.args.get('nameOfTask')
    with open(HW_JSON_PATH, mode='r') as f:
        df = json.load(f)
        for item in df['hwl']:
            if item['homeworkName'] == nameOfTask:
                item['status'] = True
        print(df)
    with open(HW_JSON_PATH, mode='w') as f:
        print("df:" + str(df))
        json.dump(df, f, ensure_ascii=False, indent=4)
        return jsonify({'result': 'success'})


@app.route("/markAsUndone")
def markAsUndone():
    nameOfTask = request.args.get('nameOfTask')
    with open(HW_JSON_PATH, mode='r') as f:
        df = json.load(f)
        for item in df['hwl']:
            if item['homeworkName'] == nameOfTask:
                item['status'] = False
        print(df)
    with open(HW_JSON_PATH, mode='w') as f:
        print("df:" + str(df))
        json.dump(df, f, ensure_ascii=False, indent=4)
        return jsonify({'result': 'success'})


@app.route("/delete")
def deleteTask():
    nameOfTask = request.args.get('nameOfTask')
    with open(HW_JSON_PATH, mode='r') as f:
        df = json.load(f)
        df['hwl'] = [i for i in df['hwl'] if not (i['homeworkName'] == nameOfTask)]
        print(df)
    with open(HW_JSON_PATH, mode='w') as f:
        print("df:" + str(df))
        json.dump(df, f, ensure_ascii=False, indent=4)
        return jsonify({'result': 'success'})


if __name__ == "__main__":
    app.run(port=3000, host='0.0.0.0', debug=False)
