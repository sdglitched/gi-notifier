from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.elegance import Elegance


class KamisatoAyaka(CharacterBase):
    @property
    def name(self) -> str:
        return "Kamisato Ayaka"

    @property
    def talent_book(self):
        return Elegance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Perpetual Heart", "https://genshin-impact.fandom.com/wiki/Perpetual_Heart"),
            source = Source("Perpetual Mechanical Array", "https://genshin-impact.fandom.com/wiki/Perpetual_Mechanical_Array")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Bloodjade Branch", "https://genshin-impact.fandom.com/wiki/Bloodjade_Branch"),
            source = Source("Beneath the Dragon-Queller", "https://genshin-impact.fandom.com/wiki/Beneath_the_Dragon-Queller")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
