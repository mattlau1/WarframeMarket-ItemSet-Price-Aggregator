import asyncio
from dataclasses import dataclass
from typing import List
import tqdm.asyncio
from warframe_market.client import WarframeMarketClient
from warframe_market.api.item import Items, Item


@dataclass
class ItemWithPrice:
    name: str
    slug: str
    platinum: float

    def __str__(self):
        return f"{self.name}: {round(self.platinum, 2)}p"


async def fetch_price(
    client: WarframeMarketClient, item_name: str, item_slug: str, sem: asyncio.Semaphore
):
    async with sem:
        for attempt in range(5):
            try:
                await asyncio.sleep(0.35)

                top_orders = await client.get_top_orders_for_item(item_slug)
                buy_data = top_orders.data.buy

                if not buy_data:
                    return ItemWithPrice(item_name, item_slug, 0)

                avg_price = sum(data.platinum for data in buy_data) / len(buy_data)
                return ItemWithPrice(item_name, item_slug, avg_price)

            except Exception as e:
                if "429" in str(e):
                    wait_time = (attempt + 1) * 2
                    await asyncio.sleep(wait_time)
                    continue
                else:
                    print("WARNING: Results may be incomplete.")

        print("WARNING: Results may be incomplete.")


async def get_all_item_set_buy_prices(
    client: WarframeMarketClient,
) -> List[ItemWithPrice]:
    items = await client.get_all_items()
    targets = [
        (item.i18n["en"].name, item.slug)
        for item in items.data
        if "set" in item.slug.lower().split("_")
        or " set" in item.i18n["en"].name.lower()
    ]

    # Limit concurrent requests
    sem = asyncio.Semaphore(5)

    tasks = [fetch_price(client, name, slug, sem) for name, slug in targets]
    results = await tqdm.asyncio.tqdm.gather(*tasks)

    items_with_prices = [r for r in results if r is not None]

    items_with_prices.sort(key=lambda x: x.platinum, reverse=True)

    return items_with_prices


async def main():
    async with WarframeMarketClient() as client:
        itemSets = await get_all_item_set_buy_prices(client)

        with open("out.txt", "w", encoding="utf-8") as f:
            for item in itemSets:
                f.write(f"{item}\n")

        print(f"Saved {len(itemSets)} items to out.txt")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
