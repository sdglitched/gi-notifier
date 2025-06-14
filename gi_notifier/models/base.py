from abc import ABC, abstractmethod
from functools import cached_property

from .models import ConstantResource, Drop, MaterialGroup, Weekday


class MaterialGroupBase(ABC):
    @property
    @abstractmethod
    def drop(self) -> Drop:
        ...

    @property
    @abstractmethod
    def available_on(self) -> list[Weekday]:
        ...

    def is_available_today(self, today: Weekday) -> bool:
        return today in self.available_on

    def as_material_group(self) -> MaterialGroup:
        return MaterialGroup(
            drop=self.drop,
            available_on=self.available_on
        )


class CharacterBase(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @cached_property
    def constant_resource(self) -> ConstantResource:
        return ConstantResource()

    @property
    @abstractmethod
    def talent_book(self) -> MaterialGroup:
        ...

    @property
    @abstractmethod
    def normal_boss_drop(self) -> Drop:
        ...

    @property
    @abstractmethod
    def weekly_boss_drop(self) -> Drop:
        ...

    @property
    @abstractmethod
    def in_current_banner(self) -> bool:
        ...

    def is_talent_book_available_today(self, today: Weekday) -> bool:
        return today in self.talent_book.available_on
