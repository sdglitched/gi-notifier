from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.light import Light


class Gorou(CharacterBase):
    @property
    def name(self) -> str:
        return "Gorou"

    @property
    def talent_book(self):
        return Light().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Perpetual Heart", "https://genshin-impact.fandom.com/wiki/Perpetual_Heart"),
            source = Source("Perpetual Mechanical Array", "https://genshin-impact.fandom.com/wiki/Perpetual_Mechanical_Array")
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
