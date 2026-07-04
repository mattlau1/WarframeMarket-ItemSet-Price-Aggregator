# 📊 Warframe-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator/actions/workflows/scan.yml/badge.svg)

A Python script that pulls median buy-order prices for all tradeable item sets by interfacing with the [Warframe Market](https://warframe.market/) API (v2).

This is helpful for finding rare items to potentially sell or to find rare relics in your inventory.

## Automation & Output
This script is set up to run automatically every hour via GitHub Actions.

It fetches the latest median prices and generates an `out.txt` file with the full dataset.

The top 50 results from that scan are injected directly into the [Live Market Prices](#-live-market-prices) section at the bottom of this page.

## Key Features
- **Set Filtering**: Finds all tradable item sets by checking slugs and item names.
- **Rate Limit Handling**: Uses a semaphore and sleep timers to stay under the API limit.
- **Async**: Fetches multiple prices concurrently to save time.
- **Resilient Scraping**: Implemented with asyncio semaphores and exponential backoff to handle rate limits gracefully.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator.git
cd Warframe-ItemSet-Price-Aggregator
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
**Last Updated:** 2026-07-04 06:43 UTC

| Item Set | Median Price |
| :--- | :--- |
| Vectis Prime Set | 120p |
| Xiphos Set | 114p |
| Ballistica Prime Set | 110p |
| Hespar Set | 95p |
| Kronen Prime Set | 90p |
| Vauban Prime Set | 90p |
| Nekros Prime Set | 85p |
| Afuris Prime Set | 85p |
| Destreza Prime Set | 81p |
| Limbo Prime Set | 80p |
| Nidus Prime Set | 80p |
| Kogake Prime Set | 79p |
| Hydroid Prime Set | 75p |
| Boar Prime Set | 72p |
| Spira Prime Set | 72p |
| Chroma Prime Set | 71p |
| Frost Prime Set | 70p |
| Carrier Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Akstiletto Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Mirage Prime Set | 70p |
| Octavia Prime Set | 70p |
| Saryn Prime Set | 68p |
| Banshee Prime Set | 68p |
| Khora Prime Set | 68p |
| Loki Prime Set | 67p |
| Bo Prime Set | 65p |
| Wyrm Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Corinth Prime Set | 65p |
| Wukong Prime Set | 61p |
| Akarius Prime Set | 61p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Titania Prime Set | 60p |
| Nova Prime Set | 60p |
| Carmine Penta Set | 60p |
| Gara Prime Set | 60p |
| Garuda Prime Set | 60p |
| Afentis Prime Set | 60p |
| Zephyr Prime Set | 57p |
| Helios Prime Set | 56p |
| Volt Prime Set | 56p |
| Wisp Prime Set | 56p |
| Dual Kamas Prime Set | 55p |
| Akvasto Prime Set | 55p |
| Dethcube Prime Set | 55p |
| Panthera Prime Set | 55p |
| Akjagara Prime Set | 55p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
