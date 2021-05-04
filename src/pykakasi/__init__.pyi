from typing import Dict, List, Optional, Union

class PyKakasiException(Exception): ...
class UnknownCharacterException(PyKakasiException): ...
class UnsupportedRomanRulesException(PyKakasiException): ...
class UnknownOptionsException(PyKakasiException): ...
class InvalidModeValueException(PyKakasiException): ...
class InvalidFlagValueException(PyKakasiException): ...

class kakasi:
    def __init__(self) -> None: ...
    def convert(self, text: str) -> List[Dict[str, str]]: ...
    def setMode(self, fr: str, to: Optional[Union[bool, str]]) -> None: ...
    def getConverter(self): ...
    def do(self, text: str) -> str: ...

class wakati(kakasi):
    def __init__(self) -> None: ...
    def getConverter(self): ...
    def setMode(self, fr: str, to: Optional[Union[bool, str]]) -> None: ...
    def do(self, text: str) -> str: ...

# Names in __all__ with no definition:
#   exceptions
