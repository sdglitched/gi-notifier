from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class Chongyun(CharacterBase):
    @property
    def name(self) -> str:
        return "Chongyun"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hoarfrost Core", "https://genshin-impact.fandom.com/wiki/Hoarfrost_Core"),
            source = Source("Cryo Regisvine", "https://genshin-impact.fandom.com/wiki/Cryo_Regisvine")
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
