'''
returning the .generate() response as JSON
from your main app import this file.
if you are following the example on
https://github.com/acoomans/flask-autodoc
use split_string(auto.generate()) to get the json string which then
can by used in jsonify

author: https://github.com/hallborg
'''


def generate_json(generated_obj):
    '''obj['methods'] is of the type 'set' which isnt json serialized
    so in this function it's reworked to a list'''

    json_list = []
    set_item_list = []
    for obj in generated_obj:
        set_item_list = []
        for item in obj['methods']:
            set_item_list.append(item)
        obj['methods'] = set_item_list
        json_list.append(obj)

    return json_list
