# ---- state_NewsG.py ----
from typing import List
from typing_extensions import Annotated, TypedDict


class SearchState(TypedDict):
    query: str
    sources: list[str]
    web_results: list[str]
    summarized_results: list[str]
    response: str

class SearchStateInput(TypedDict):
    query: str

class SearchStateOutput(TypedDict):
    sources: list[str]
    response: str

