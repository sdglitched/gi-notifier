from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.admonition import Admonition


class Tighnari(CharacterBase):
    @property
    def name(self) -> str:
        return "Tighnari"

    @property
    def talent_book(self):
        return Admonition().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Majestic Hooked Beak", "https://genshin-impact.fandom.com/wiki/Majestic_Hooked_Beak"),
            source = Source("Jadeplume Terrorshroom", "https://genshin-impact.fandom.com/wiki/Jadeplume_Terrorshroom")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("The Meaning of Aeons", "https://genshin-impact.fandom.com/wiki/The_Meaning_of_Aeons"),
            source = Source("End of the Oneiric Euthymia", "https://genshin-impact.fandom.com/wiki/End_of_the_Oneiric_Euthymia")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
