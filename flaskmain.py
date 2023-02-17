import json
import logging
import datetime
from flask_cors import CORS
from flask import Flask, url_for, redirect, request, jsonify, Response, render_template
from config import CONFIG_FLASK as FlaskConfig


# 创建一个logger
logger = logging.getLogger(FlaskConfig.FLASKPUBLISH_LOGGER_NAME)
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
suffix_log = datetime.datetime.now().strftime('%Y%m%d%H%M')
fh = logging.FileHandler(FlaskConfig.FLASKPUBLISH_LOGGER_FILENAME + "_" + suffix_log + ".log")
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter(FlaskConfig.FLASKPUBLISH_LOGGER_FORMATTER)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/test/post', methods=['POST'])
def test_post():
    if request.method == 'POST':
        try:
            params_data = request.json
            logger.info("请求参数如下：")
            logger.info(params_data)
            data1 = params_data['data1']
            data2 = params_data['data2']
            data3 = params_data['data3']

            response_data = {}
            response_data['data1'] = data1 + '||' + data1
            response_data['data2'] = data1 + '||' + data2
            response_data['data3'] = data1 + '||' + data3

            return Response(json.dumps(response_data, ensure_ascii=False),
                     mimetype=FlaskConfig.FLASKPUBLISH_CONTENT_TYPE_JSON)
            logger.info("返回数据如下：")
            loger.info(response_data)
        except Exception as e:
            logger.error("异常！")
            logger.error(e)
            return Response(json.dumps(FlaskConfig.FLASKPUBLISH_FAIL, ensure_ascii=False),
                            mimetype=FlaskConfig.FLASKPUBLISH_CONTENT_TYPE_JSON)
    else:
        return Response(json.dumps(FlaskConfig.FLASKPUBLISH_FAIL, ensure_ascii=False),
                        mimetype=FlaskConfig.FLASKPUBLISH_CONTENT_TYPE_JSON)


@app.route('/test/get', methods=['GET'])
def send():
    print(request.url)
    return "ERROR"


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(
        host='127.0.0.1',
        port=9911,
        debug=True
    )
