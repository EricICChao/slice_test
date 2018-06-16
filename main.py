import json, io



json_file = 'user_data_json_middle.json'

f = open(json_file, 'rt', encoding='utf-8' )
data = json.load(f)
#Line的json被設定為list性質
var = data['events']  #取出'event'對應的值，是一組list
"""
[{'replyToken': '00000000000000000000000000000000', 'type': 'message', 'timestamp': 1529115030647, 'source': {'type': 'user', 'userId': 'Udeadbeefdeadbeefdeadbeefdeadbeef'}, 'message': {'id': '100001', 'type': 'text', 'text': 'Hello, world'}}, {'replyToken': 'ffffffffffffffffffffffffffffffff', 'type': 'message', 'timestamp': 1529115030647, 'source': {'type': 'user', 'userId': 'Udeadbeefdeadbeefdeadbeefdeadbeef'}, 'message': {'id': '100002', 'type': 'sticker', 'packageId': '1', 'stickerId': '1'}}]
"""

var1 = data           #取出全部的json，但是值還是list
"""
{'events': [{'replyToken': '00000000000000000000000000000000', 'type': 'message', 'timestamp': 1529115030647, 'source': {'type': 'user', 'userId': 'Udeadbeefdeadbeefdeadbeefdeadbeef'}, 'message': {'id': '100001', 'type': 'text', 'text': 'Hello, world'}}, {'replyToken': 'ffffffffffffffffffffffffffffffff', 'type': 'message', 'timestamp': 1529115030647, 'source': {'type': 'user', 'userId': 'Udeadbeefdeadbeefdeadbeefdeadbeef'}, 'message': {'id': '100002', 'type': 'sticker', 'packageId': '1', 'stickerId': '1'}}]}
"""

#var1 = var['source']['userId']

#Traceback (most recent call last):
#  File "C:\Users\hp200\Desktop\程式完裝\slice_test\main.py", line 12, in <module>
#    var1 = data['source']['userId']
#KeyError: 'source'

#Traceback (most recent call last):
#  File "C:\Users\hp200\Desktop\程式完裝\slice_test\main.py", line 14, in <module>
#    var1 = var['source']['userId']
#TypeError: list indices must be integers or slices, not str



take_value = var[0]
"""
result:
{'replyToken': '00000000000000000000000000000000', 'type': 'message', 'timestamp': 1529115030647, 'source': {'type': 'user', 'userId': 'Udeadbeefdeadbeefdeadbeefdeadbeef'}, 'message': {'id': '100001', 'type': 'text', 'text': 'Hello, world'}}
"""

take_value_1 = var[0]['source']
"""
result:
{'type': 'user', 'userId': 'Udeadbeefdeadbeefdeadbeefdeadbeef'}
"""
take_value_2 = var[0]['source']['userId']
"""
result:
Udeadbeefdeadbeefdeadbeefdeadbeef
"""

print(take_value_2)
f.close()


