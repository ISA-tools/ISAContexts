from os import walk, path

from isacontexts.constants import VOCAB_PATH, SCHEMAS_PATH


def get_vocabularies_path() -> dict[str, str]:
    i = 0
    for directory in walk(VOCAB_PATH):
        if i == 0:
            return {vocab: path.join(directory[0], vocab) for vocab in directory[1]}


def get_schemas_path() -> dict[str, str]:
    for directory in walk(SCHEMAS_PATH):
        return {schema.replace('_schema.json', ''): path.join(SCHEMAS_PATH, schema) for schema in directory[2]}


def capitalize(string: str) -> str:
    return string[0].upper() + string[1:]
