from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Baizhu(CharacterBase):
    @property
    def name(self) -> str:
        return "Baizhu"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Evergloom Ring", "https://genshin-impact.fandom.com/wiki/Evergloom_Ring"),
            source = Source("Iniquitous Baptist", "https://genshin-impact.fandom.com/wiki/Iniquitous_Baptist")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Worldspan Fern", "https://genshin-impact.fandom.com/wiki/Worldspan_Fern"),
            source = Source("The Realm of Beginnings", "https://genshin-impact.fandom.com/wiki/The_Realm_of_Beginnings")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
