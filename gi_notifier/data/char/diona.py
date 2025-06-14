from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Diona(CharacterBase):
    @property
    def name(self) -> str:
        return "Diona"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hoarfrost Core", "https://genshin-impact.fandom.com/wiki/Hoarfrost_Core"),
            source = Source("Cryo Regisvine", "https://genshin-impact.fandom.com/wiki/Cryo_Regisvine")
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
