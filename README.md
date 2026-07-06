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
**Last Updated:** 2026-07-06 21:24 UTC

| Item Set | Median Price |
| :--- | :--- |
| Ballistica Prime Set | 100p |
| Hespar Set | 91p |
| Vectis Prime Set | 90p |
| Vauban Prime Set | 82p |
| Limbo Prime Set | 80p |
| Nidus Prime Set | 80p |
| Kronen Prime Set | 78p |
| Carmine Penta Set | 74p |
| Spira Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Destreza Prime Set | 70p |
| Boar Prime Set | 70p |
| Mirage Prime Set | 70p |
| Nekros Prime Set | 70p |
| Octavia Prime Set | 70p |
| Athodai Set | 70p |
| Garuda Prime Set | 70p |
| Afuris Prime Set | 70p |
| Khora Prime Set | 69p |
| Nami Skyla Prime Set | 66p |
| Loki Prime Set | 61p |
| Scourge Prime Set | 61p |
| Frost Prime Set | 60p |
| Saryn Prime Set | 60p |
| Latron Prime Set | 60p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Carrier Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Bonewidow Set | 60p |
| Chroma Prime Set | 60p |
| Gara Prime Set | 60p |
| Nova Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Nautilus Set | 55p |
| Phantasma Prime Set | 55p |
| Afentis Prime Set | 55p |
| Akvasto Prime Set | 53p |
| Wisp Prime Set | 53p |
| Wukong Prime Set | 51p |
| Dethcube Prime Set | 51p |
| Corinth Prime Set | 51p |
| Tenora Prime Set | 51p |
| Dual Kamas Prime Set | 50p |
| Ember Prime Set | 50p |
| Kogake Prime Set | 50p |
| Volt Prime Set | 50p |
| Titania Prime Set | 50p |
| Glaive Prime Set | 50p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
