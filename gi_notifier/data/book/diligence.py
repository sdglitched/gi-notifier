from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Diligence(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Diligence Books", "https://genshin-impact.fandom.com/wiki/Diligence_Book"),
            source=Source("Taishan Mansion", "https://genshin-impact.fandom.com/wiki/Taishan_Mansion")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.TUE, Weekday.FRI, Weekday.SUN]
