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
**Last Updated:** 2026-07-06 02:37 UTC

| Item Set | Median Price |
| :--- | :--- |
| Vectis Prime Set | 100p |
| Ballistica Prime Set | 100p |
| Hespar Set | 93p |
| Vauban Prime Set | 91p |
| Destreza Prime Set | 90p |
| Kronen Prime Set | 82p |
| Hydroid Prime Set | 80p |
| Limbo Prime Set | 80p |
| Spira Prime Set | 80p |
| Nekros Prime Set | 80p |
| Carmine Penta Set | 76p |
| Nidus Prime Set | 76p |
| Kogake Prime Set | 75p |
| Afuris Prime Set | 75p |
| Chroma Prime Set | 71p |
| Mirage Prime Set | 71p |
| Boar Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Athodai Set | 70p |
| Khora Prime Set | 70p |
| Saryn Prime Set | 66p |
| Octavia Prime Set | 66p |
| Frost Prime Set | 65p |
| Oberon Prime Set | 65p |
| Banshee Prime Set | 65p |
| Loki Prime Set | 65p |
| Corinth Prime Set | 65p |
| Scourge Prime Set | 65p |
| Garuda Prime Set | 65p |
| Cortege Set | 61p |
| Dual Kamas Prime Set | 60p |
| Mag Prime Set | 60p |
| Bo Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Titania Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Akstiletto Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Bonewidow Set | 60p |
| Nova Prime Set | 60p |
| Gara Prime Set | 60p |
| Wukong Prime Set | 59p |
| Nezha Prime Set | 56p |
| Nautilus Set | 56p |
| Afentis Prime Set | 56p |
| Latron Prime Set | 55p |
| Carrier Prime Set | 55p |
| Panthera Prime Set | 55p |
| Zephyr Prime Set | 55p |
| Wisp Prime Set | 55p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
