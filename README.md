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
**Last Updated:** 2026-01-02 17:09 UTC

| Item Set | Median Price |
| :--- | :--- |
| Braton Vandal Set | 261p |
| Lato Vandal Set | 255p |
| Vauban Prime Set | 126p |
| Akstiletto Prime Set | 116p |
| Dual Kamas Prime Set | 100p |
| Spira Prime Set | 97p |
| Arum Spinosa Set | 96p |
| Nami Skyla Prime Set | 92p |
| Sporothrix Set | 90p |
| Hespar Set | 90p |
| Akjagara Prime Set | 85p |
| Valkyr Prime Set | 80p |
| Kronen Prime Set | 80p |
| Dethcube Prime Set | 76p |
| Aksomati Prime Set | 75p |
| Akbolto Prime Set | 75p |
| Saryn Prime Set | 71p |
| Hydroid Prime Set | 70p |
| Limbo Prime Set | 70p |
| Nyx Prime Set | 70p |
| Mirage Prime Set | 70p |
| Nekros Prime Set | 70p |
| Afuris Prime Set | 70p |
| Nova Prime Set | 67p |
| Vectis Prime Set | 66p |
| Kogake Prime Set | 66p |
| Garuda Prime Set | 66p |
| Wukong Prime Set | 65p |
| Oberon Prime Set | 65p |
| Ballistica Prime Set | 65p |
| Carrier Prime Set | 65p |
| Titania Prime Set | 65p |
| Tekko Prime Set | 65p |
| Loki Prime Set | 65p |
| Frost Prime Set | 62p |
| Scourge Prime Set | 62p |
| Chroma Prime Set | 61p |
| Corinth Prime Set | 61p |
| Khora Prime Set | 61p |
| Bo Prime Set | 60p |
| Venka Prime Set | 60p |
| Sybaris Prime Set | 60p |
| Xiphos Set | 60p |
| Nikana Prime Set | 60p |
| Morgha Set | 60p |
| Boar Prime Set | 58p |
| Trinity Prime Set | 57p |
| Baza Prime Set | 56p |
| Carmine Penta Set | 56p |
| Nidus Prime Set | 56p |

*... (see out.txt for full list of 235 items)*

[//]: # (PRICE_END)