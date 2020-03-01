# coding: utf-8
from dataclasses import dataclass, field, asdict, astuple, replace
from typing import List

@dataclass
class Market():
    id: int
    nome: str
    # paths: List[str]

@dataclass
class Kabum(Market):
    id: int = 1
    nome: str = 'Kabum'
    paths = [
            '//*[@id="pag-detalhes"]/div/div[2]/div[2]/div[1]/div[3]/div[4]/span[1]/span/text()', 
            '//*[@id="pag-detalhes"]/div/div[2]/div[2]/div[2]/div[1]/span/span/span/strong/text()'
        ]