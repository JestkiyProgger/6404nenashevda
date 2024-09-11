import json
from cmath import sin, cos


def parser_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


def calculate():
    data = parser_json()
    n0 = data['n0']
    h = data['h']
    nk = data['nk']
    a = data['a']
    b = data['b']
    c = data['c']
    with open('output.txt', 'w') as file:
        for x in range(n0, nk + 1, h):
            y = sin(a*x) * cos(b*x) / (sin(x)+cos(x)) + c
            file.write(f"{y}\n")


if __name__ == '__main__':
    calculate()
