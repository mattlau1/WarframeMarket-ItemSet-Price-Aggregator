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
**Last Updated:** 2026-07-11 01:43 UTC

| Item Set | Median Price |
| :--- | :--- |
| Vectis Prime Set | 100p |
| Xiphos Set | 100p |
| Hespar Set | 93p |
| Vauban Prime Set | 92p |
| Ballistica Prime Set | 90p |
| Nami Skyla Prime Set | 87p |
| Spira Prime Set | 85p |
| Kronen Prime Set | 85p |
| Destreza Prime Set | 80p |
| Limbo Prime Set | 80p |
| Nekros Prime Set | 76p |
| Nidus Prime Set | 76p |
| Hydroid Prime Set | 75p |
| Carrier Prime Set | 75p |
| Afuris Prime Set | 75p |
| Aksomati Prime Set | 71p |
| Loki Prime Set | 71p |
| Mirage Prime Set | 71p |
| Dual Kamas Prime Set | 70p |
| Boar Prime Set | 70p |
| Kogake Prime Set | 70p |
| Akstiletto Prime Set | 70p |
| Akbolto Prime Set | 70p |
| Garuda Prime Set | 70p |
| Khora Prime Set | 70p |
| Octavia Prime Set | 67p |
| Chroma Prime Set | 66p |
| Frost Prime Set | 65p |
| Saryn Prime Set | 65p |
| Wyrm Prime Set | 65p |
| Zephyr Prime Set | 65p |
| Scourge Prime Set | 65p |
| Banshee Prime Set | 64p |
| Sybaris Prime Set | 61p |
| Latron Prime Set | 60p |
| Mag Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Tekko Prime Set | 60p |
| Nezha Prime Set | 60p |
| Tenora Prime Set | 60p |
| Nautilus Set | 60p |
| Athodai Set | 60p |
| Gara Prime Set | 60p |
| Akjagara Prime Set | 56p |
| Wukong Prime Set | 55p |
| Baza Prime Set | 55p |
| Valkyr Prime Set | 55p |
| Harrow Prime Set | 55p |
| Cinta Set | 55p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
