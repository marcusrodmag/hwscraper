# coding: utf-8
from dataclasses import dataclass, field, asdict, astuple, replace
from typing import Dict

# @dataclass
# class Market():
#     id: int
#     nome: str
#     paths: List[str]

# @dataclass
# class Produto():
#     id: int
#     nome: str
#     uri: Dict[int, str]

# MOC
@dataclass
class CelularSamsung():
    id: int = 1
    nome: str = "Galaxy A10s"
    uri = {
        1: "https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=107341"
    }

# MOC
@dataclass
class CelularXiaomi():
    id: int = 2
    nome: str = "Xiaomi Mi 9T"
    uri = {
        1: "https://www.kabum.com.br/produto/103897/smartphone-xiaomi-mi-9t-128gb-48mp-tela-6-39-azul-capa-e-pelicula-cx277azu"
    }