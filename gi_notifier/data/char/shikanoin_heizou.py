from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class ShikanoinHeizou(CharacterBase):
    @property
    def name(self) -> str:
        return "Shikanoin Heizou"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('Runic Fang', 'https://genshin-impact.fandom.com/wiki/Runic_Fang'),
            source = Source("Ruin Serpent", "https://genshin-impact.fandom.com/wiki/Ruin_Serpent")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("The Meaning of Aeons", "https://genshin-impact.fandom.com/wiki/The_Meaning_of_Aeons"),
            source = Source("End of the Oneiric Euthymia", "https://genshin-impact.fandom.com/wiki/End_of_the_Oneiric_Euthymia")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
