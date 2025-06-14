from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class Yoimiya(CharacterBase):
    @property
    def name(self) -> str:
        return "Yoimiya"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('Smoldering Pearl', 'https://genshin-impact.fandom.com/wiki/Smoldering_Pearl'),
            source = Source("Pyro Hypostasis", "https://genshin-impact.fandom.com/wiki/Pyro_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Drag­on Lord's Crown", "https://genshin-impact.fandom.com/wiki/Dragon_Lord's_Crown"),
            source = Source("Beneath the Dragon-Queller", "https://genshin-impact.fandom.com/wiki/Beneath_the_Dragon-Queller")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
