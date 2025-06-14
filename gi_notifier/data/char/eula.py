from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.resistance import Resistance


class Eula(CharacterBase):
    @property
    def name(self) -> str:
        return "Eula"

    @property
    def talent_book(self):
        return Resistance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Crystalline Bloom", "https://genshin-impact.fandom.com/wiki/Crystalline_Bloom"),
            source = Source("Cryo Hypostasis", "https://genshin-impact.fandom.com/wiki/Cryo_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dragon Lord's Crown", "https://genshin-impact.fandom.com/wiki/Dragon_Lord's_Crown"),
            source = Source("Beneath the Dragon-Queller", "https://genshin-impact.fandom.com/wiki/Beneath_the_Dragon-Queller")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
