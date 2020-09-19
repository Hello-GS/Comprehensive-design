import configparser
import os

path = ''
year_map_0 = {}
year_map_1 = {}


def read_config():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    global path
    path = config.get('data', 'data_path')


def get_year(file_name):
    return file_name[3:7]


def write_map(map_to_write):
    out = ''
    for key in sorted(map_to_write.keys()):
        out += str(key) + ':' + str(map_to_write[key]) + '\n'
    return out


if __name__ == '__main__':
    read_config()
    output = open('./output.txt', 'r+')
    flies = os.listdir(path + '0/')
    for file in flies:
        if file == '.DS_Store':
            continue
        incident_number = len(os.listdir(path + '0/' + file))
        year = int(get_year(file))
        if year in year_map_0:
            year_map_0[year] = year_map_0[year] + incident_number
        else:
            year_map_0[year] = incident_number
    output.write('年份：图片数 类型0:\n')
    output.write(write_map(year_map_0))
    flies = os.listdir(path + '1/')
    for file in flies:
        if file == '.DS_Store':
            continue
        incident_number = len(os.listdir(path + '1/' + file))
        year = int(get_year(file))
        if year in year_map_1:
            year_map_1[year] = year_map_1[year] + incident_number
        else:
            year_map_1[year] = incident_number
    output.write('年份：图片数 类型 1:\n')
    output.write(write_map(year_map_1))
