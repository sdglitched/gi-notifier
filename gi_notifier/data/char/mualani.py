from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.contention import Contention


class Mualani(CharacterBase):
    @property
    def name(self) -> str:
        return "Mualani"

    @property
    def talent_book(self):
        return Contention().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Mark of the Binding Blessing", "https://genshin-impact.fandom.com/wiki/Mark_of_the_Binding_Blessing"),
            source = Source("Goldflame Qucusaur Tyrant", "https://genshin-impact.fandom.com/wiki/Goldflame_Qucusaur_Tyrant")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Mass", "https://genshin-impact.fandom.com/wiki/Lightless_Mass"),
            source = Source("All-Devouring Narwhal", "https://genshin-impact.fandom.com/wiki/All-Devouring_Narwhal")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
