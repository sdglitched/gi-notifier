from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Equity(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Equity Books", "https://genshin-impact.fandom.com/wiki/Equity_Book"),
            source=Source("Pale Forgotten Glory", "https://genshin-impact.fandom.com/wiki/Pale_Forgotten_Glory")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.MON, Weekday.THU, Weekday.SUN]
