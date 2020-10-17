from yamlinclude import YamlIncludeConstructor
import yaml
from dacite import from_dict
from typing import List
from dataclasses import dataclass


@dataclass
class Config:
    window_sizes: List[int]


def load_config():
    YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)

    with open("config.yaml", "r") as file:
        yaml_as_dictionary = yaml.load(file, Loader=yaml.FullLoader)

    return from_dict(data_class=Config, data=yaml_as_dictionary)


cubeviz_config = load_config()
