from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.justice import Justice


class Charlotte(CharacterBase):
    @property
    def name(self) -> str:
        return "Charlotte"

    @property
    def talent_book(self):
        return Justice().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('"Tourbillon Device"', 'https://genshin-impact.fandom.com/wiki/"Tourbillon Device"'),
            source = Source("Experimental Field Generator", "https://genshin-impact.fandom.com/wiki/Experimental_Field_Generator")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Silk String", "https://genshin-impact.fandom.com/wiki/Lightless_Silk_String"),
            source = Source("All-Devouring Narwhal", "https://genshin-impact.fandom.com/wiki/All-Devouring_Narwhal")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
