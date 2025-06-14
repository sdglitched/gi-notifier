from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Lynette(CharacterBase):
    @property
    def name(self) -> str:
        return "Lynette"

    @property
    def talent_book(self):
        return Order().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Artificed Spare Clockwork Component — Coppelia", "https://genshin-impact.fandom.com/wiki/Artificed_Spare_Clockwork_Component_—_Coppelia"),
            source = Source("Icewind Suite: Dirge of Coppelia", "https://genshin-impact.fandom.com/wiki/Icewind_Suite:_Dirge_of_Coppelia")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Everamber", "https://genshin-impact.fandom.com/wiki/Everamber"),
            source = Source("The Realm of Beginnings", "https://genshin-impact.fandom.com/wiki/The_Realm_of_Beginnings")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
