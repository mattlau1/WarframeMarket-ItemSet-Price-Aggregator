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
**Last Updated:** 2026-07-02 20:58 UTC

| Item Set | Median Price |
| :--- | :--- |
| Ballistica Prime Set | 113p |
| Vectis Prime Set | 99p |
| Hespar Set | 91p |
| Vauban Prime Set | 85p |
| Nekros Prime Set | 85p |
| Destreza Prime Set | 80p |
| Limbo Prime Set | 80p |
| Nidus Prime Set | 80p |
| Carmine Penta Set | 75p |
| Khora Prime Set | 75p |
| Akstiletto Prime Set | 72p |
| Hydroid Prime Set | 71p |
| Boar Prime Set | 70p |
| Kogake Prime Set | 70p |
| Aksomati Prime Set | 70p |
| Spira Prime Set | 70p |
| Nami Skyla Prime Set | 70p |
| Kronen Prime Set | 70p |
| Garuda Prime Set | 70p |
| Carrier Prime Set | 65p |
| Loki Prime Set | 65p |
| Mirage Prime Set | 65p |
| Octavia Prime Set | 65p |
| Athodai Set | 65p |
| Chroma Prime Set | 63p |
| Frost Prime Set | 60p |
| Saryn Prime Set | 60p |
| Oberon Prime Set | 60p |
| Bo Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Bonewidow Set | 60p |
| Cortege Set | 60p |
| Corinth Prime Set | 60p |
| Scourge Prime Set | 60p |
| Cinta Set | 60p |
| Corufell Set | 59p |
| Zephyr Prime Set | 57p |
| Afentis Prime Set | 56p |
| Dual Kamas Prime Set | 55p |
| Wukong Prime Set | 55p |
| Mag Prime Set | 55p |
| Baza Prime Set | 55p |
| Sybaris Prime Set | 55p |
| Titania Prime Set | 55p |
| Panthera Prime Set | 55p |
| Nikana Prime Set | 55p |
| Phantasma Prime Set | 55p |
| Latron Prime Set | 50p |
| Glaive Prime Set | 50p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
