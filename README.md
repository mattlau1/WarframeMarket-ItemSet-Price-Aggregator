# 📊 Warframe-ItemSet-Price-Aggregator
![Hourly Price Update](https://github.com/mattlau1/Warframe-ItemSet-Price-Aggregator/actions/workflows/hourly_scan.yml/badge.svg)

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
**Last Updated:** 2026-01-03 10:10 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 270p |
| Lato Vandal Set | 256p |
| Vauban Prime Set | 120p |
| Dual Kamas Prime Set | 100p |
| Akstiletto Prime Set | 100p |
| Nami Skyla Prime Set | 90p |
| Arum Spinosa Set | 89p |
| Valkyr Prime Set | 80p |
| Akjagara Prime Set | 80p |
| Limbo Prime Set | 77p |
| Kronen Prime Set | 75p |
| Nekros Prime Set | 75p |
| Nyx Prime Set | 72p |
| Hydroid Prime Set | 70p |
| Saryn Prime Set | 70p |
| Wukong Prime Set | 70p |
| Dethcube Prime Set | 70p |
| Spira Prime Set | 70p |
| Mirage Prime Set | 70p |
| Khora Prime Set | 70p |
| Carrier Prime Set | 69p |
| Titania Prime Set | 66p |
| Sporothrix Set | 66p |
| Frost Prime Set | 65p |
| Vectis Prime Set | 65p |
| Oberon Prime Set | 65p |
| Nikana Prime Set | 65p |
| Loki Prime Set | 65p |
| Garuda Prime Set | 65p |
| Gara Prime Set | 61p |
| Ballistica Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Tekko Prime Set | 60p |
| Nova Prime Set | 60p |
| Scourge Prime Set | 60p |
| Hespar Set | 60p |
| Aksomati Prime Set | 58p |
| Latron Prime Set | 55p |
| Mag Prime Set | 55p |
| Bo Prime Set | 55p |
| Glaive Prime Set | 55p |
| Chroma Prime Set | 55p |
| Banshee Prime Set | 55p |
| Carmine Penta Set | 55p |
| Nidus Prime Set | 55p |
| Kogake Prime Set | 52p |
| Inaros Prime Set | 52p |
| Morgha Set | 52p |
| Cinta Set | 52p |
| Trinity Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)