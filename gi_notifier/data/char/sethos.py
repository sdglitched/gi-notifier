from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.praxis import Praxis


class Sethos(CharacterBase):
    @property
    def name(self) -> str:
        return "Sethos"

    @property
    def talent_book(self):
        return Praxis().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('Cloudseam Scale', 'https://genshin-impact.fandom.com/wiki/Cloudseam_Scale'),
            source = Source("Solitary Suanni", "https://genshin-impact.fandom.com/wiki/Solitary_Suanni")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Daka's Bell", "https://genshin-impact.fandom.com/wiki/Daka's_Bell"),
            source = Source("Joururi Workshop", "https://genshin-impact.fandom.com/wiki/Joururi_Workshop")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
