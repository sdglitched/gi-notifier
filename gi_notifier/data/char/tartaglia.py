from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Tartaglia(CharacterBase):
    @property
    def name(self) -> str:
        return "Tartaglia"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Cleansing Heart", "https://genshin-impact.fandom.com/wiki/Cleansing_Heart"),
            source = Source("Rhodeia of Loch", "https://genshin-impact.fandom.com/wiki/Rhodeia_of_Loch")
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
