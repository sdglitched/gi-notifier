from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Beidou(CharacterBase):
    @property
    def name(self) -> str:
        return "Beidou"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Lightning Prism", "https://genshin-impact.fandom.com/wiki/Lightning_Prism"),
            source = Source("Electro Hypostasis", "https://genshin-impact.fandom.com/wiki/Electro_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Sigh", "https://genshin-impact.fandom.com/wiki/Dvalin's_Sigh"),
            source = Source("Confront Stormterror", "https://genshin-impact.fandom.com/wiki/Confront_Stormterror")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
