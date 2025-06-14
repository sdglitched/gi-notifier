from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Xianyun(CharacterBase):
    @property
    def name(self) -> str:
        return "Xianyun"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('Cloudseam Scale', 'https://genshin-impact.fandom.com/wiki/Cloudseam_Scale'),
            source = Source("Solitary Suanni", "https://genshin-impact.fandom.com/wiki/Solitary_Suanni")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Eye of the Maelstrom", "https://genshin-impact.fandom.com/wiki/Lightless_Eye_of_the_Maelstrom"),
            source = Source("All-Devouring Narwhal", "https://genshin-impact.fandom.com/wiki/All-Devouring_Narwhal")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
