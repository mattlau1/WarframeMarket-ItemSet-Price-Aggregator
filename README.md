# 📊 WarframeMarket-ItemSet-Price-Aggregator

A Python script that pulls median buy-order prices for all tradeable item sets by interfacing with the [Warframe Market](https://warframe.market/) API (v2).

This is helpful for finding rare items to potentially sell or to find rare relics in your inventory.

## Output
The program will spit out a file in the same directory called `out.txt` after it finishes running.

Sample Output:
```text
Braton Vandal Set: 227p
Lato Vandal Set: 200p
Vauban Prime Set: 120p
Akstiletto Prime Set: 113p
Arum Spinosa Set: 100p
Nami Skyla Prime Set: 91p
Dual Kamas Prime Set: 90p
...
```

## Key Features
- **Set Filtering**: Finds all tradable item sets by checking slugs and item names.
- **Rate Limit Handling**: Uses a semaphore and sleep timers to stay under the API limit.
- **Async**: Fetches multiple prices concurrently to save time.
- **Resilient Scraping**: Implemented with asyncio semaphores and exponential backoff to handle rate limits gracefully.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/mattlau1/WarframeMarket-ItemSet-Price-Aggregator.git
cd WarframeMarket-ItemSet-Price-Aggregator
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
