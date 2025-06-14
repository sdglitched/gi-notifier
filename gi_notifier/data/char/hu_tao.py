from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class HuTao(CharacterBase):
    @property
    def name(self) -> str:
        return "Hu Tao"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Juvenile Jade", "https://genshin-impact.fandom.com/wiki/Juvenile_Jade"),
            source = Source("Primo Geovishap", "https://genshin-impact.fandom.com/wiki/Primo_Geovishap")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Shard of a Foul Legacy", "https://genshin-impact.fandom.com/wiki/Shard_of_a_Foul_Legacy"),
            source = Source("Enter the Golden House", "https://genshin-impact.fandom.com/wiki/Enter_the_Golden_House")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
