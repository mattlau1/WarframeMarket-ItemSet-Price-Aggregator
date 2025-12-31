# 📊 WarframeMarket-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/WarframeMarket-ItemSet-Price-Aggregator/actions/workflows/hourly_scan.yml/badge.svg)

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
**Last Updated:** 2025-12-31 12:19 UTC

```text
Braton Vandal Set: 251p
Lato Vandal Set: 250p
Akstiletto Prime Set: 120p
Vauban Prime Set: 111p
Nami Skyla Prime Set: 100p
Hespar Set: 100p
Dual Kamas Prime Set: 95p
Arum Spinosa Set: 92p
Sporothrix Set: 83p
Spira Prime Set: 80p
Akjagara Prime Set: 80p
Valkyr Prime Set: 77p
Carrier Prime Set: 75p
Kronen Prime Set: 75p
Nyx Prime Set: 72p
Hydroid Prime Set: 70p
Vectis Prime Set: 70p
Aksomati Prime Set: 70p
Mirage Prime Set: 70p
Nekros Prime Set: 69p
Akbolto Prime Set: 67p
Limbo Prime Set: 66p
Wukong Prime Set: 65p
Dethcube Prime Set: 65p
Afuris Prime Set: 65p
Frost Prime Set: 62p
Nikana Prime Set: 62p
Atlas Prime Set: 62p
Loki Prime Set: 62p
Saryn Prime Set: 61p
Ballistica Prime Set: 61p
Titania Prime Set: 61p
Xiphos Set: 61p
Bo Prime Set: 60p
Kogake Prime Set: 60p
Wyrm Prime Set: 60p
Tekko Prime Set: 60p
Nova Prime Set: 60p
Garuda Prime Set: 60p
Gyre Prime Set: 60p
Nidus Prime Set: 57p
Morgha Set: 56p
Rhino Prime Set: 55p
Boar Prime Set: 55p
Venka Prime Set: 55p
Baza Prime Set: 55p
Cortege Set: 55p
Corinth Prime Set: 55p
Khora Prime Set: 55p
Glaive Prime Set: 52p
... (see out.txt for full list)
```
[//]: # (PRICE_END)