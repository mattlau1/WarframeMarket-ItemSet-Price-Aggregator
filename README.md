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
**Last Updated:** 2026-01-01 16:13 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 251p |
| Lato Vandal Set | 249p |
| Vauban Prime Set | 120p |
| Akstiletto Prime Set | 110p |
| Dual Kamas Prime Set | 100p |
| Arum Spinosa Set | 100p |
| Hespar Set | 100p |
| Sporothrix Set | 95p |
| Spira Prime Set | 90p |
| Nami Skyla Prime Set | 90p |
| Akjagara Prime Set | 82p |
| Saryn Prime Set | 75p |
| Limbo Prime Set | 75p |
| Kronen Prime Set | 75p |
| Nyx Prime Set | 75p |
| Vectis Prime Set | 72p |
| Hydroid Prime Set | 70p |
| Wukong Prime Set | 70p |
| Carrier Prime Set | 70p |
| Dethcube Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Loki Prime Set | 70p |
| Nekros Prime Set | 70p |
| Khora Prime Set | 70p |
| Frost Prime Set | 65p |
| Kogake Prime Set | 65p |
| Ballistica Prime Set | 65p |
| Valkyr Prime Set | 65p |
| Nova Prime Set | 65p |
| Mirage Prime Set | 65p |
| Garuda Prime Set | 65p |
| Afuris Prime Set | 65p |
| Nikana Prime Set | 62p |
| Akbolto Prime Set | 61p |
| Bo Prime Set | 60p |
| Baza Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Titania Prime Set | 60p |
| Xiphos Set | 60p |
| Tekko Prime Set | 60p |
| Chroma Prime Set | 60p |
| Morgha Set | 60p |
| Carmine Penta Set | 60p |
| Gara Prime Set | 60p |
| Nidus Prime Set | 60p |
| Cinta Set | 60p |
| Gyre Prime Set | 60p |
| Mag Prime Set | 59p |
| Venka Prime Set | 56p |
| Latron Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)