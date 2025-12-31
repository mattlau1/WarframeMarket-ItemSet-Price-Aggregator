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
**Last Updated:** 2025-12-31 23:10 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 240p |
| Lato Vandal Set | 150p |
| Vauban Prime Set | 117p |
| Akstiletto Prime Set | 110p |
| Dual Kamas Prime Set | 105p |
| Arum Spinosa Set | 93p |
| Spira Prime Set | 81p |
| Hespar Set | 81p |
| Limbo Prime Set | 80p |
| Nami Skyla Prime Set | 80p |
| Kronen Prime Set | 80p |
| Saryn Prime Set | 77p |
| Sporothrix Set | 77p |
| Hydroid Prime Set | 71p |
| Vectis Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Nyx Prime Set | 70p |
| Dethcube Prime Set | 69p |
| Atlas Prime Set | 68p |
| Mirage Prime Set | 66p |
| Oberon Prime Set | 65p |
| Carrier Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Tekko Prime Set | 65p |
| Loki Prime Set | 65p |
| Nidus Prime Set | 65p |
| Afuris Prime Set | 65p |
| Titania Prime Set | 64p |
| Twin Vipers Wraith Set | 62p |
| Nekros Prime Set | 62p |
| Frost Prime Set | 61p |
| Akbolto Prime Set | 61p |
| Mag Prime Set | 60p |
| Kogake Prime Set | 60p |
| Xiphos Set | 60p |
| Nova Prime Set | 60p |
| Akjagara Prime Set | 60p |
| Gara Prime Set | 60p |
| Scourge Prime Set | 60p |
| Garuda Prime Set | 60p |
| Khora Prime Set | 60p |
| Cinta Set | 60p |
| Gyre Prime Set | 60p |
| Trinity Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Baza Prime Set | 52p |
| Glaive Prime Set | 52p |
| Ballistica Prime Set | 51p |
| Equinox Prime Set | 51p |
| Carmine Penta Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)