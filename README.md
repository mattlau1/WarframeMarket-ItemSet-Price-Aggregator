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
**Last Updated:** 2026-01-03 16:11 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 269p |
| Lato Vandal Set | 256p |
| Vauban Prime Set | 125p |
| Akstiletto Prime Set | 120p |
| Dual Kamas Prime Set | 100p |
| Spira Prime Set | 100p |
| Nami Skyla Prime Set | 91p |
| Hespar Set | 90p |
| Arum Spinosa Set | 89p |
| Akjagara Prime Set | 85p |
| Aksomati Prime Set | 80p |
| Valkyr Prime Set | 80p |
| Limbo Prime Set | 80p |
| Dethcube Prime Set | 76p |
| Nyx Prime Set | 76p |
| Akbolto Prime Set | 75p |
| Kronen Prime Set | 75p |
| Hydroid Prime Set | 72p |
| Nekros Prime Set | 72p |
| Saryn Prime Set | 70p |
| Mirage Prime Set | 68p |
| Garuda Prime Set | 68p |
| Afuris Prime Set | 68p |
| Loki Prime Set | 67p |
| Nova Prime Set | 67p |
| Kogake Prime Set | 66p |
| Vectis Prime Set | 65p |
| Wukong Prime Set | 65p |
| Carrier Prime Set | 65p |
| Nikana Prime Set | 65p |
| Carmine Penta Set | 65p |
| Frost Prime Set | 63p |
| Titania Prime Set | 63p |
| Sporothrix Set | 63p |
| Scourge Prime Set | 63p |
| Oberon Prime Set | 62p |
| Rhino Prime Set | 61p |
| Gara Prime Set | 61p |
| Khora Prime Set | 61p |
| Bo Prime Set | 60p |
| Ballistica Prime Set | 60p |
| Atlas Prime Set | 60p |
| Tekko Prime Set | 60p |
| Nidus Prime Set | 60p |
| Wyrm Prime Set | 57p |
| Latron Prime Set | 55p |
| Boar Prime Set | 55p |
| Glaive Prime Set | 55p |
| Chroma Prime Set | 55p |
| Corinth Prime Set | 55p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)