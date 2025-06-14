from dataclasses import dataclass, field
from enum import Enum


class Weekday(Enum):
    """
    Class for having the days of the week.
    """
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"


@dataclass
class Item:
    """
    Data class for ontainable items.
    """
    name: str = ""
    link: str = ""


@dataclass
class Source:
    """
    Data class for the source of the obtainable item.
    """
    name: str = ""
    link: str = ""


@dataclass
class Drop:
    """
    Data class for the generating the message for an obtainable item.
    """
    item: Item
    source: Source = field(default_factory = Source)

    def to_use(self) -> str:
        return (
            f"""Use your <a href="{self.item.link}">{self.item.name}</a> for"""
        )

    def to_claim(self) -> str:
        return (
            f"""Do not forget to claim your <a href="{self.item.link}">{self.item.name}</a> """
            f"""from <a href="{self.source.link}">{self.source.name}</a>"""
        )

    def to_make(self) -> str:
        return (
            f"""Making <a href="{self.item.link}">{self.item.name}</a> for future usage"""
        )

    def to_obtain(self) -> str:
        return (
            f"""Obtaining <a href="{self.item.link}">{self.item.name}</a> """
            f"""from <a href="{self.source.link}">{self.source.name}</a>"""
        )


@dataclass
class Resin:
    """
    Data class for resins.
    """
    original_resin: Drop = field(
        default_factory = lambda: Drop(
            item = Item("Original Resin", "https://genshin-impact.fandom.com/wiki/Original_Resin")
        )
    )
    transient_resin: Drop = field(
        default_factory = lambda: Drop(
            item = Item("Transient Resin", "https://genshin-impact.fandom.com/wiki/Transient_Resin"),
            source = Source("Realm Depot", "https://genshin-impact.fandom.com/wiki/Serenitea_Pot/Realm_Depot")
        )
    )
    condensed_resin: Drop = field(
        default_factory = lambda: Drop(
            item = Item("Condensed Resin", "https://genshin-impact.fandom.com/wiki/Condensed_Resin")
        )
    )


@dataclass
class ConstantResource:
    """
    Dataclass for the constant resource.
    """
    experience: Drop = field(
        default_factory = lambda: Drop(
            item = Item("Experience", "https://genshin-impact.fandom.com/wiki/Experience"),
            source = Source("Ley Line Outcrop - Blossom of Revelation", "https://genshin-impact.fandom.com/wiki/Ley_Line_Outcrop")
        )
    )
    mora: Drop = field(
        default_factory = lambda: Drop(
            item = Item("Mora", "https://genshin-impact.fandom.com/wiki/Mora"),
            source = Source("Ley Line Outcrop - Blossom of Wealth", "https://genshin-impact.fandom.com/wiki/Ley_Line_Outcrop")
        )
    )
    resin: Resin = field(default_factory = Resin)


@dataclass
class MaterialGroup:
    drop: Drop
    available_on: list[Weekday]
