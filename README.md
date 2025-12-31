# 📊 WarframeMarket-ItemSet-Price-Aggregator

A Python script that pulls median buy-order prices for all tradeable item sets by interfacing with the [Warframe Market](https://warframe.market/) API (v2).

This is helpful for finding rare items to potentially sell or to find rare relics in your inventory.

## Output
The program will spit out a file in the same directory called `out.txt` after it finishes running.

Sample Output:
```text
Braton Vandal Set: 227p
Lato Vandal Set: 200p
Vauban Prime Set: 120p
Akstiletto Prime Set: 113p
Arum Spinosa Set: 100p
Nami Skyla Prime Set: 91p
Dual Kamas Prime Set: 90p
...
```

## Key Features
- **Set Filtering**: Finds all tradable item sets by checking slugs and item names.
- **Rate Limit Handling**: Uses a semaphore and sleep timers to stay under the API limit.
- **Async**: Fetches multiple prices concurrently to save time.
- **Resilient Scraping**: Implemented with asyncio semaphores and exponential backoff to handle rate limits gracefully.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/mattlau1/WarframeMarket-ItemSet-Price-Aggregator.git
cd WarframeMarket-ItemSet-Price-Aggregator
```

### 2. Set up a Virtual Environment (Recommended)
**macOS / Linux (Bash):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (Command Prompt):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
python3 -m venv .venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
This project uses a specific Git-based version of the Warframe Market API client.
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

Note: Due to the scraping speed, a full scan of ~400+ total items takes approximately 1 minute.

As of late 2025, the script analyses approximately 240+ tradeable item sets.

## 📈 Live Market Prices
[//]: # (PRICE_START)
**Last Updated:** 2025-12-31 11:22 UTC

```text
Braton Vandal Set: 256p
Lato Vandal Set: 250p
Akstiletto Prime Set: 120p
Vauban Prime Set: 119p
Hespar Set: 101p
Dual Kamas Prime Set: 100p
Nami Skyla Prime Set: 100p
Spira Prime Set: 89p
Limbo Prime Set: 81p
Valkyr Prime Set: 80p
Arum Spinosa Set: 80p
Sporothrix Set: 80p
Akjagara Prime Set: 80p
Hydroid Prime Set: 76p
Dethcube Prime Set: 75p
Kronen Prime Set: 75p
Nyx Prime Set: 72p
Nekros Prime Set: 71p
Saryn Prime Set: 70p
Vectis Prime Set: 70p
Ballistica Prime Set: 70p
Carrier Prime Set: 70p
Akbolto Prime Set: 70p
Mirage Prime Set: 70p
Frost Prime Set: 69p
Aksomati Prime Set: 68p
Garuda Prime Set: 66p
Wukong Prime Set: 65p
Titania Prime Set: 65p
Loki Prime Set: 65p
Nova Prime Set: 65p
Chroma Prime Set: 63p
Bo Prime Set: 61p
Nikana Prime Set: 61p
Atlas Prime Set: 61p
Afuris Prime Set: 61p
Kogake Prime Set: 60p
Wyrm Prime Set: 60p
Xiphos Set: 60p
Tekko Prime Set: 60p
Corinth Prime Set: 60p
Khora Prime Set: 60p
Latron Prime Set: 58p
Rhino Prime Set: 58p
Trinity Prime Set: 58p
Morgha Set: 58p
Nidus Prime Set: 58p
Gyre Prime Set: 57p
Boar Prime Set: 56p
Carmine Penta Set: 56p
... (see out.txt for full list)
```
[//]: # (PRICE_END)