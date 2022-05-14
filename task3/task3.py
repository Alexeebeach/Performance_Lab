import sys
import json

def serarch_all_items(search_dict,field,dict_values):

    for key, value in search_dict.items():

        if key == field:
            for item in dict_values['values']:
                if item['id'] == search_dict['id']:
                    search_dict[key] = item[key]

        elif isinstance(value, dict):
            results = serarch_all_items(value, field, dict_values)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = serarch_all_items(item, field,dict_values)
    return search_dict


if __name__ == '__main__':
    if len(sys.argv) > 0:
        path_tests = sys.argv[1]

    if len(sys.argv) > 1:
        path_values = sys.argv[2]

    with open(path_tests,"r") as json_Tests:
        dict_Tests = json.load(json_Tests)

    with open(path_values,"r") as json_Values:
        dict_Values = json.load(json_Values)

    data = serarch_all_items(dict_Tests,'value',dict_Values)

    with open('report.json','w') as out_file:
        json.dump(data ,out_file,indent = 2)