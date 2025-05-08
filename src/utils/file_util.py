import json
import typing
from os import PathLike

from lxml import html  # nosec: https://github.com/TUM-Dev/eat-api/issues/19

from utils import json_util


def load_html(path: str) -> html.Element:
    with open(path, encoding="utf-8") as f:
        html_element = html.fromstring(f.read())
    # suppress warning about "unnecessary variable assignment before return statement".
    # reason: file closing could otherwise have side effects
    return html_element  # noqa: R504


def load_json(path: str | PathLike[str]) -> typing.Any:
    with open(path, encoding="utf-8") as f:
        json_obj = json.load(f)
    # suppress warning about "unnecessary variable assignment before return statement".
    # reason: file closing could otherwise have side effects
    return json_obj  # noqa: R504


def load_ordered_json(path: str | PathLike[str]) -> typing.Any:
    return json_util.order_json_objects(load_json(path))


def load_txt(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    # suppress warning about "unnecessary variable assignment before return statement".
    # reason: file closing could otherwise have side effects
    return text  # noqa: R504


def write(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def write_json(path: str, obj: object) -> None:
    write(path, json_util.to_json_str(obj))
