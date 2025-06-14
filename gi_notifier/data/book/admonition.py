from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Admonition(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Admonition Books", "https://genshin-impact.fandom.com/wiki/Admonition_Book"),
            source=Source("Steeple of Ignorance", "https://genshin-impact.fandom.com/wiki/Steeple_of_Ignorance")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.MON, Weekday.THU, Weekday.SUN]
