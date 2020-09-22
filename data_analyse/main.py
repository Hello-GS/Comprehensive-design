import configparser
import os
import yagmail

input_path = ''
output_path = ''
user, password, receiver, host = '', '', [], ''
year_map_0 = {}
year_map_1 = {}
year_event_0 = {}
year_event_1 = {}
event_graph_0 = {}
event_graph_1 = {}


def read_config():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    global user, password, receiver, input_path, output_path, host
    input_path = config.get('data', 'data_path')
    output_path = config.get('data', 'output_path')
    user = config.get('email', 'user')
    password = config.get('email', 'password')
    receiver = config.get('email', 'receiver').split(',')
    host = config.get('email', 'host')


def get_year(file_name):
    return file_name[3:7]


def write_map(map_to_write):
    out = ''
    for key in sorted(map_to_write.keys()):
        out += str(key) + ':' + str(map_to_write[key]) + '\n'
    return out


def send_email(title, content):
    yagmail.SMTP(user=user, password=password, host=host).send(receiver, title, content)


if __name__ == '__main__':
    read_config()
    output = open(output_path, 'r+')
    flies = os.listdir(input_path + '0/')
    for file in flies:
        if file == '.DS_Store':
            continue
        incident_number = len(os.listdir(input_path + '0/' + file))
        year = int(get_year(file))
        event_graph_0[file] = incident_number
        if year in year_event_0:
            year_event_0[year] += 1
        else:
            year_event_0[year] = 1
        if year in year_map_0:
            year_map_0[year] += incident_number
        else:
            year_map_0[year] = incident_number

    flies = os.listdir(input_path + '1/')
    for file in flies:
        if file == '.DS_Store':
            continue
        incident_number = len(os.listdir(input_path + '1/' + file))
        year = int(get_year(file))
        event_graph_1[file] = incident_number
        if year in year_event_1:
            year_event_1[year] += 1
        else:
            year_event_1[year] = 1
        if year in year_map_1:
            year_map_1[year] += incident_number
        else:
            year_map_1[year] = incident_number
    output.write('年份：图片数 类型0:\n')
    output.write(write_map(year_map_0))
    output.write('年份：图片数 类型1:\n')
    output.write(write_map(year_map_1))
    output.write('年份：事件数 类型0：\n')
    output.write(write_map(year_event_0))
    output.write('年份：事件数 类型1：\n')
    output.write(write_map(year_event_1))
    output.write('事件：图片数 类型0：\n')
    output.write(write_map(event_graph_0))
    output.write('事件：图片数 类型1：\n')
    output.write(write_map(event_graph_1))
    send_email('分析结果', output_path)
