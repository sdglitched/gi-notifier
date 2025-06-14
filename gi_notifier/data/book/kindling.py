from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Kindling(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Kindling Books", "https://genshin-impact.fandom.com/wiki/Kindling_Book"),
            source=Source("Blazing Ruins", "https://genshin-impact.fandom.com/wiki/Blazing_Ruins")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.TUE, Weekday.FRI, Weekday.SUN]
