from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class YunJin(CharacterBase):
    @property
    def name(self) -> str:
        return "Yun Jin"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('Riftborn Regalia', 'https://genshin-impact.fandom.com/wiki/Riftborn_Regalia'),
            source = Source("Golden Wolflord", "https://genshin-impact.fandom.com/wiki/Golden_Wolflord")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Ashen Heart", "https://genshin-impact.fandom.com/wiki/Ashen_Heart"),
            source = Source("Narukami Island: Tenshukaku", "https://genshin-impact.fandom.com/wiki/Narukami_Island:_Tenshukaku")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
