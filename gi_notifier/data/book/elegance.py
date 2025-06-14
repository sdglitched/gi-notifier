from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Elegance(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Elegance Books", "https://genshin-impact.fandom.com/wiki/Elegance_Book"),
            source=Source("Violet Court", "https://genshin-impact.fandom.com/wiki/Violet_Court")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.TUE, Weekday.FRI, Weekday.SUN]
