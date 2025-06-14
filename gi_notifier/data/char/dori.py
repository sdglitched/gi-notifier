from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Dori(CharacterBase):
    @property
    def name(self) -> str:
        return "Dori"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Thunderclap Fruitcore", "https://genshin-impact.fandom.com/wiki/Thunderclap_Fruitcore"),
            source = Source("Electro Regisvines", "https://genshin-impact.fandom.com/wiki/Electro_Regisvines")
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
