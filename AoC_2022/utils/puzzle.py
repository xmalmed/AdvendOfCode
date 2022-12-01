# Puzzle runner for Advent of Code
# version 2021

from parse import parse
import requests
from pathlib import Path
from re import match
from os import getcwd, getenv
from dotenv import load_dotenv


class Puzzle:
    def __init__(self, day=None, year=None, filename='input.txt'):
        load_dotenv()
        self.aoc_session = getenv('AOC_SESSION')
        self.filename = filename
        self.day = day if day else match(r'.*_([0-9]{1,2})', getcwd()).group(1)
        self.year = year if year else match(r'.*(20[0-9]{2})', getcwd()).group(1)
        self.download_input()
        self.prepare_test_input()

    def download_input(self):
        p = Path(self.filename)
        if p.is_file():
            return True
        headers = {'session': self.aoc_session}
        url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'
        r = requests.get(url, cookies=headers)
        p.write_text(r.text.rstrip())

    def prepare_test_input(self):
        with open('input_test.txt', 'a'):
            pass

    def load_input(self, filename='input.txt', string=False) -> list:
        data = []

        with open(filename, "r") as f:
            raw = f.readlines()

        data = list(map(str.strip, raw))
        if not string:
            try:
                data = list(map(int, data))
            except ValueError:
                pass

        return data
