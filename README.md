# 📊 WarframeMarket-ItemSet-Price-Aggregator

A Python script that pulls average buy-order prices for all tradeable item sets by interfacing with the [Warframe Market](https://warframe.market/) API (v2).

This is helpful for finding rare items to potentially sell or to find rare relics in your inventory.


## Sample Output
The output is sorted by price (highest to lowest). Example:

```text
Braton Vandal Set: 226.4p
Lato Vandal Set: 195.2p
Vauban Prime Set: 120.0p
Akstiletto Prime Set: 113.0p
Hespar Set: 94.6p
Dual Kamas Prime Set: 86.0p
...
```

## Key Features
- **Set Filtering**: Finds Prime and non-Prime sets by checking slugs and item names.
- **Rate Limit Handling**: Uses a semaphore and sleep timers to stay under the API limit.
- **Async**: Fetches multiple prices concurrently to save time.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/mattlau1/WarframeMarket-ItemSet-Price-Aggregator.git
cd WarframeMarket-ItemSet-Price-Aggregator
```

### 2. Set up a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
This project uses a specific Git-based version of the Warframe Market API client.
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

Note: Due to the scraping speed, a full scan of ~400+ total items takes approximately 1 minute.

As of late 2025, the script analyses approximately 240+ tradeable item sets.
