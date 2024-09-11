import argparse
import json
from math import sin, cos
from typing import Tuple, List, Callable


def target_function(x: float, a: float, b: float, c: float) -> float:
    return sin(a * x) * cos(b * x) / (sin(x) + cos(x)) + c


def write_result(mass_y):
    with open('output.txt', 'w') as file:
        for i, y in enumerate(mass_y):
            print(f"{i:<3}|{y}")
            print(f"{i:<3}|{y}", file=file)


def parse_args_json(file_name: str) -> Tuple[Tuple[int, ...], Tuple[float, ...]]:
    with open(file_name, 'rt') as file:
        data = json.load(file)
        try:
            return (int(data['n0']), int(data['nk']), int(data['h'])),\
                (float(data['a']), float(data['b']), float(data['c']))
        except KeyError as er:
            print(f"KeyError: {er.args}")
        except ValueError as er:
            print(f"ValueError: {er.args}")

    return (0, 1, 10), (1.0, 1.0, 1.0)


def calculate_json(func: Callable[[float, ...], float]):
    range_args, func_args = parse_args_json('data.json')
    write_result(eval_target_function(func, range_args, func_args))


def calculate_argv(func: Callable[[float, ...], float]):
    parser = argparse.ArgumentParser(description='Программа для вычисления значений функции.')
    parser.add_argument('--n0', type=int, help='Начальное значение')
    parser.add_argument('--nk', type=int, help='Конечное значение')
    parser.add_argument('--h', type=int, help='Шаг')
    parser.add_argument('--a', type=float, help='Первый параметр')
    parser.add_argument('--b', type=float, help='Второй параметр')
    parser.add_argument('--c', type=float, help='Третий параметр')
    args = parser.parse_args().__dict__
    range_args = (args['n0'], args['nk'], args['h'])
    func_args = (args['a'], args['b'], args['c'])

    write_result(eval_target_function(func, range_args, func_args))


def eval_target_function(func: Callable[[float, ...], float],
                         range_args: Tuple[int, ...], func_args: Tuple[float, ...]) -> Tuple[float, ...]:
    return tuple(func(x, *func_args) for x in range(*range_args))


if __name__ == '__main__':
    calculate_argv(target_function)
