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
**Last Updated:** 2026-07-02 17:40 UTC

| Item Set | Median Price |
| :--- | :--- |
| Ballistica Prime Set | 120p |
| Vectis Prime Set | 100p |
| Hespar Set | 99p |
| Spira Prime Set | 90p |
| Vauban Prime Set | 90p |
| Destreza Prime Set | 88p |
| Nami Skyla Prime Set | 85p |
| Kronen Prime Set | 82p |
| Akstiletto Prime Set | 80p |
| Limbo Prime Set | 80p |
| Morgha Set | 80p |
| Nidus Prime Set | 80p |
| Hydroid Prime Set | 77p |
| Mirage Prime Set | 75p |
| Carmine Penta Set | 75p |
| Garuda Prime Set | 71p |
| Saryn Prime Set | 70p |
| Boar Prime Set | 70p |
| Carrier Prime Set | 70p |
| Loki Prime Set | 70p |
| Nekros Prime Set | 70p |
| Afuris Prime Set | 70p |
| Banshee Prime Set | 69p |
| Titania Prime Set | 67p |
| Chroma Prime Set | 66p |
| Khora Prime Set | 66p |
| Frost Prime Set | 65p |
| Oberon Prime Set | 65p |
| Bo Prime Set | 65p |
| Aksomati Prime Set | 65p |
| Wyrm Prime Set | 65p |
| Corinth Prime Set | 65p |
| Octavia Prime Set | 65p |
| Zephyr Prime Set | 63p |
| Valkyr Prime Set | 61p |
| Dual Kamas Prime Set | 60p |
| Mag Prime Set | 60p |
| Latron Wraith Set | 60p |
| Dethcube Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Tekko Prime Set | 60p |
| Bonewidow Set | 60p |
| Athodai Set | 60p |
| Scourge Prime Set | 60p |
| Aeolak Set | 60p |
| Cinta Set | 60p |
| Helios Prime Set | 59p |
| Panthera Prime Set | 58p |
| Wukong Prime Set | 56p |
| Glaive Prime Set | 56p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
