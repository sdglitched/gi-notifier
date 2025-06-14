from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Aloy(CharacterBase):
    @property
    def name(self) -> str:
        return "Aloy"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Crystalline Bloom", "https://genshin-impact.fandom.com/wiki/Crystalline_Bloom"),
            source = Source("Cryo Hypostasis", "https://genshin-impact.fandom.com/wiki/Cryo_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Molten Moment", "https://genshin-impact.fandom.com/wiki/Molten_Moment"),
            source = Source("Narukami Island: Tenshukaku", "https://genshin-impact.fandom.com/wiki/Narukami_Island:_Tenshukaku")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
