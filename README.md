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
**Last Updated:** 2026-01-01 20:12 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 256p |
| Lato Vandal Set | 253p |
| Vauban Prime Set | 116p |
| Akstiletto Prime Set | 110p |
| Dual Kamas Prime Set | 100p |
| Arum Spinosa Set | 96p |
| Spira Prime Set | 90p |
| Nami Skyla Prime Set | 90p |
| Hespar Set | 90p |
| Sporothrix Set | 82p |
| Valkyr Prime Set | 79p |
| Kronen Prime Set | 75p |
| Saryn Prime Set | 71p |
| Limbo Prime Set | 71p |
| Akjagara Prime Set | 71p |
| Nekros Prime Set | 71p |
| Vectis Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Nikana Prime Set | 70p |
| Scourge Prime Set | 70p |
| Garuda Prime Set | 70p |
| Khora Prime Set | 70p |
| Hydroid Prime Set | 65p |
| Wukong Prime Set | 65p |
| Ballistica Prime Set | 65p |
| Dethcube Prime Set | 65p |
| Tekko Prime Set | 65p |
| Loki Prime Set | 65p |
| Nyx Prime Set | 65p |
| Mirage Prime Set | 65p |
| Carmine Penta Set | 62p |
| Akbolto Prime Set | 61p |
| Afuris Prime Set | 61p |
| Bo Prime Set | 60p |
| Carrier Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Xiphos Set | 60p |
| Chroma Prime Set | 60p |
| Gyre Prime Set | 58p |
| Venka Prime Set | 56p |
| Latron Prime Set | 55p |
| Rhino Prime Set | 55p |
| Mag Prime Set | 55p |
| Oberon Prime Set | 55p |
| Titania Prime Set | 55p |
| Inaros Prime Set | 55p |
| Nova Prime Set | 55p |
| Corinth Prime Set | 55p |
| Octavia Prime Set | 55p |
| Gara Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)