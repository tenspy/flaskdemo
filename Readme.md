## 1. 安装flask依赖
+ pip install flask
+ pip install flask_cors

## 启动flask
+ 执行文件 flaskmain.py

## 示例接口
请求接口：
POST http://127.0.0.1:9911/test/post

请求Header: 
content-type: application/json; charset=utf-8

请求体：
``` json
{
  "data1": "json在线编辑器",
  "data2": "工具上线",
  "data3": "减法功能"
}
```

返回数据：
```json
{
  "data1": "json在线编辑器||json在线编辑器",
  "data2": "json在线编辑器||工具上线",
  "data3": "json在线编辑器||减法功能"
}
```
