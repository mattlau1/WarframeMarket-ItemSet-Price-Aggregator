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
**Last Updated:** 2026-01-01 01:00 UTC

| Item Set | Median Price |
| :--- | :--- |
| Lato Vandal Set | 242p |
| Braton Vandal Set | 240p |
| Akstiletto Prime Set | 120p |
| Vauban Prime Set | 120p |
| Arum Spinosa Set | 100p |
| Spira Prime Set | 96p |
| Dual Kamas Prime Set | 95p |
| Nami Skyla Prime Set | 90p |
| Xiphos Set | 85p |
| Hespar Set | 85p |
| Limbo Prime Set | 81p |
| Kronen Prime Set | 80p |
| Sporothrix Set | 80p |
| Valkyr Prime Set | 77p |
| Saryn Prime Set | 75p |
| Dethcube Prime Set | 75p |
| Nyx Prime Set | 75p |
| Nekros Prime Set | 75p |
| Hydroid Prime Set | 71p |
| Vectis Prime Set | 71p |
| Akjagara Prime Set | 71p |
| Aksomati Prime Set | 70p |
| Tekko Prime Set | 70p |
| Nova Prime Set | 66p |
| Nidus Prime Set | 66p |
| Frost Prime Set | 65p |
| Wukong Prime Set | 65p |
| Oberon Prime Set | 65p |
| Atlas Prime Set | 65p |
| Loki Prime Set | 65p |
| Garuda Prime Set | 65p |
| Khora Prime Set | 65p |
| Afuris Prime Set | 65p |
| Titania Prime Set | 61p |
| Akbolto Prime Set | 61p |
| Bo Prime Set | 60p |
| Boar Prime Set | 60p |
| Ballistica Prime Set | 60p |
| Carrier Prime Set | 60p |
| Nikana Prime Set | 60p |
| Chroma Prime Set | 60p |
| Zephyr Prime Set | 60p |
| Mirage Prime Set | 60p |
| Scourge Prime Set | 60p |
| Cinta Set | 60p |
| Gyre Prime Set | 60p |
| Mag Prime Set | 59p |
| Rhino Prime Set | 55p |
| Wyrm Prime Set | 55p |
| Inaros Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)