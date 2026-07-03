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
**Last Updated:** 2026-07-03 20:57 UTC

| Item Set | Median Price |
| :--- | :--- |
| Vectis Prime Set | 115p |
| Ballistica Prime Set | 115p |
| Hespar Set | 91p |
| Kronen Prime Set | 85p |
| Vauban Prime Set | 85p |
| Destreza Prime Set | 80p |
| Limbo Prime Set | 80p |
| Spira Prime Set | 80p |
| Nekros Prime Set | 80p |
| Chroma Prime Set | 76p |
| Aksomati Prime Set | 75p |
| Akstiletto Prime Set | 75p |
| Nami Skyla Prime Set | 75p |
| Nidus Prime Set | 75p |
| Khora Prime Set | 75p |
| Hydroid Prime Set | 70p |
| Kogake Prime Set | 70p |
| Titania Prime Set | 70p |
| Corinth Prime Set | 70p |
| Scourge Prime Set | 70p |
| Garuda Prime Set | 70p |
| Carmine Penta Set | 66p |
| Phantasma Prime Set | 66p |
| Saryn Prime Set | 65p |
| Oberon Prime Set | 65p |
| Boar Prime Set | 65p |
| Mirage Prime Set | 65p |
| Octavia Prime Set | 65p |
| Frost Prime Set | 62p |
| Bo Prime Set | 61p |
| Loki Prime Set | 61p |
| Carrier Prime Set | 60p |
| Dethcube Prime Set | 60p |
| Wyrm Prime Set | 60p |
| Valkyr Prime Set | 60p |
| Nova Prime Set | 60p |
| Gara Prime Set | 60p |
| Latron Prime Set | 56p |
| Inaros Prime Set | 56p |
| Nezha Prime Set | 56p |
| Dual Kamas Prime Set | 55p |
| Helios Prime Set | 55p |
| Wukong Prime Set | 55p |
| Mag Prime Set | 55p |
| Baza Prime Set | 55p |
| Mesa Prime Set | 55p |
| Wisp Prime Set | 55p |
| Glaive Prime Set | 52p |
| Volt Prime Set | 51p |
| Atlas Prime Set | 51p |

*... (see out.txt for full list of 241 items)*

[//]: # (PRICE_END)
