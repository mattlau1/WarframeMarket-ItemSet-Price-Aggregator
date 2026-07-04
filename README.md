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
**Last Updated:** 2026-07-04 10:03 UTC

| Item Set | Median Price |
| :--- | :--- |
| Ballistica Prime Set | 110p |
| Vectis Prime Set | 100p |
| Xiphos Set | 100p |
| Spira Prime Set | 90p |
| Kronen Prime Set | 90p |
| Vauban Prime Set | 90p |
| Hespar Set | 90p |
| Destreza Prime Set | 86p |
| Limbo Prime Set | 81p |
| Nami Skyla Prime Set | 80p |
| Nekros Prime Set | 80p |
| Nidus Prime Set | 80p |
| Akstiletto Prime Set | 77p |
| Hydroid Prime Set | 76p |
| Kogake Prime Set | 76p |
| Carrier Prime Set | 75p |
| Boar Prime Set | 72p |
| Aksomati Prime Set | 70p |
| Mirage Prime Set | 70p |
| Octavia Prime Set | 70p |
| Athodai Set | 70p |
| Loki Prime Set | 68p |
| Garuda Prime Set | 67p |
| Khora Prime Set | 67p |
| Bo Prime Set | 65p |
| Wyrm Prime Set | 65p |
| Corinth Prime Set | 65p |
| Cinta Set | 65p |
| Frost Prime Set | 63p |
| Wukong Prime Set | 62p |
| Dethcube Prime Set | 61p |
| Chroma Prime Set | 61p |
| Saryn Prime Set | 60p |
| Latron Prime Set | 60p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Titania Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Banshee Prime Set | 60p |
| Nova Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Akjagara Prime Set | 60p |
| Gara Prime Set | 60p |
| Scourge Prime Set | 60p |
| Styanax Prime Set | 60p |
| Afentis Prime Set | 60p |
| Nezha Prime Set | 57p |
| Dual Kamas Prime Set | 55p |
| Helios Prime Set | 55p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
