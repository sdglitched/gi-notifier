from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.light import Light


class Sayu(CharacterBase):
    @property
    def name(self) -> str:
        return "Sayu"

    @property
    def talent_book(self):
        return Light().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Marionette Core", "https://genshin-impact.fandom.com/wiki/Marionette_Core"),
            source = Source("Maguu Kenki", "https://genshin-impact.fandom.com/wiki/Maguu_Kenki")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Gilded Scale", "https://genshin-impact.fandom.com/wiki/Gilded_Scale"),
            source = Source("Beneath the Dragon-Queller", "https://genshin-impact.fandom.com/wiki/Beneath_the_Dragon-Queller")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
