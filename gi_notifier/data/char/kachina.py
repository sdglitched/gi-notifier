from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.conflict import Conflict


class Kachina(CharacterBase):
    @property
    def name(self) -> str:
        return "Kachina"

    @property
    def talent_book(self):
        return Conflict().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Overripe Flamegranate", "https://genshin-impact.fandom.com/wiki/Overripe_Flamegranate"),
            source = Source("Gluttonous Yumkasaur Mountain King", "https://genshin-impact.fandom.com/wiki/Gluttonous_Yumkasaur_Mountain_King")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Fading Candle", "https://genshin-impact.fandom.com/wiki/Fading_Candle"),
            source = Source("The Knave", "https://genshin-impact.fandom.com/wiki/The_Knave")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
