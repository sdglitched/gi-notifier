from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.kindling import Kindling


class Xilonen(CharacterBase):
    @property
    def name(self) -> str:
        return "Xilonen"

    @property
    def talent_book(self):
        return Kindling().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Gold-Inscribed Secret Source Core", "https://genshin-impact.fandom.com/wiki/Gold-Inscribed_Secret_Source_Core"),
            source = Source("Secret Source Automaton: Configuration Device", "https://genshin-impact.fandom.com/wiki/Secret_Source_Automaton:_Configuration_Device")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Mirror of Mushin", "https://genshin-impact.fandom.com/wiki/Mirror_of_Mushin"),
            source = Source("Joururi Workshop", "https://genshin-impact.fandom.com/wiki/Joururi_Workshop")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
