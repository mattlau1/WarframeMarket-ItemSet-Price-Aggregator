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
**Last Updated:** 2026-01-03 20:10 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 270p |
| Lato Vandal Set | 261p |
| Vauban Prime Set | 117p |
| Akstiletto Prime Set | 108p |
| Dual Kamas Prime Set | 100p |
| Spira Prime Set | 96p |
| Arum Spinosa Set | 96p |
| Nami Skyla Prime Set | 91p |
| Hespar Set | 90p |
| Valkyr Prime Set | 80p |
| Akjagara Prime Set | 80p |
| Limbo Prime Set | 76p |
| Kronen Prime Set | 76p |
| Saryn Prime Set | 75p |
| Nyx Prime Set | 75p |
| Carmine Penta Set | 75p |
| Nekros Prime Set | 72p |
| Carrier Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Nova Prime Set | 70p |
| Mirage Prime Set | 70p |
| Garuda Prime Set | 67p |
| Hydroid Prime Set | 66p |
| Tekko Prime Set | 66p |
| Wukong Prime Set | 65p |
| Nikana Prime Set | 65p |
| Khora Prime Set | 65p |
| Afuris Prime Set | 65p |
| Venka Prime Set | 64p |
| Frost Prime Set | 63p |
| Sporothrix Set | 63p |
| Scourge Prime Set | 63p |
| Loki Prime Set | 62p |
| Oberon Prime Set | 61p |
| Vectis Prime Set | 60p |
| Kogake Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Atlas Prime Set | 60p |
| Titania Prime Set | 58p |
| Octavia Prime Set | 58p |
| Rhino Prime Set | 56p |
| Boar Prime Set | 56p |
| Nidus Prime Set | 56p |
| Chroma Prime Set | 55p |
| Gyre Prime Set | 55p |
| Akbolto Prime Set | 54p |
| Nezha Prime Set | 52p |
| Cinta Set | 52p |
| Latron Prime Set | 51p |
| Wyrm Prime Set | 51p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)