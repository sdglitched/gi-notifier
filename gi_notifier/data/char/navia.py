from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.equity import Equity


class Navia(CharacterBase):
    @property
    def name(self) -> str:
        return "Navia"

    @property
    def talent_book(self):
        return Equity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Artificed Spare Clockwork Component — Coppelius", "https://genshin-impact.fandom.com/wiki/Artificed_Spare_Clockwork_Component_—_Coppelius"),
            source = Source("Icewind Suite: Nemesis of Coppelius", "https://genshin-impact.fandom.com/wiki/Icewind_Suite:_Nemesis_of_Coppelius")
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
