from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Nahida(CharacterBase):
    @property
    def name(self) -> str:
        return "Nahida"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Quelled Creeper", "https://genshin-impact.fandom.com/wiki/Quelled_Creeper"),
            source = Source("Dendro Hypostasis", "https://genshin-impact.fandom.com/wiki/Dendro_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Puppet Strings", "https://genshin-impact.fandom.com/wiki/Puppet_Strings"),
            source = Source("Joururi Workshop", "https://genshin-impact.fandom.com/wiki/Joururi_Workshop")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
