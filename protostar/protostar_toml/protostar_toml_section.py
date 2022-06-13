from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Union

from protostar.protostar_toml.protostar_toml_exceptions import (
    InvalidProtostarTOMLException,
)
from protostar.utils.protostar_directory import VersionManager, VersionType


class ProtostarTOMLSection(ABC):
    TOMLCompatibleDict = Dict[str, Union[str, int, bool, List[str]]]

    @staticmethod
    @abstractmethod
    def get_section_name() -> str:
        ...

    @abstractmethod
    def to_dict(self) -> "ProtostarTOMLSection.TOMLCompatibleDict":
        ...

    @classmethod
    def _load_version_from_raw_dict(
        cls, raw_dict: Dict[str, Any], attribute_name: str
    ) -> VersionType:
        try:
            return VersionManager.parse(raw_dict[attribute_name])
        except TypeError as err:
            raise InvalidProtostarTOMLException(
                cls.get_section_name(), attribute_name
            ) from err

    @classmethod
    def _load_path_from_raw_dict(
        cls, raw_dict: Dict[str, Any], attribute_name: str
    ) -> Path:
        try:
            return Path(raw_dict[attribute_name])
        except TypeError as err:
            raise InvalidProtostarTOMLException(
                cls.get_section_name(), attribute_name
            ) from err
