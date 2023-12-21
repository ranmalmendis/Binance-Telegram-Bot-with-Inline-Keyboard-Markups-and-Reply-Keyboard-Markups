
# Binance-Telegram Bot with Inline and Markup Keyboards

## Description
This Telegram bot provides an interface for querying cryptocurrency prices and statistics from Binance. Users can interact with the bot through Telegram, selecting from a variety of cryptocurrencies to receive up-to-date information and visualizations of market trends.

## Features
- Inline and markup keyboards for easy interaction.
- Real-time cryptocurrency data from Binance.
- Graphical representation of price changes.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Telegram account

### Setup

#### Step 1: Clone the Repository
Clone the repository to your local machine.

#### Step 2: Create a Python Virtual Environment
Navigate to the cloned directory and create a virtual environment. This keeps dependencies required by the project separate from your global Python installation.
```bash
python -m venv venv
```

#### Step 3: Activate the Virtual Environment
For Windows:
```bash
venv\Scripts\activate
```
For macOS/Linux:
```bash
source venv/bin/activate
```

#### Step 4: Install Dependencies
Install all the required dependencies using pip.
```bash
pip install -r requirements.txt
```

### Configuration
Replace the Binance API Token, Binance API secret, and Telegram bot token in the `cred.py` file with your credentials.

### Running the Bot
Run `bot.py` to start the bot.
```bash
python bot.py
```

### Usage
Open the Telegram app on your PC or mobile device. Search for your bot and send the `/start` command to interact with it.

## Additional Resources
- Loom video walkthrough: https://www.loom.com/share/0520a9ff16564adbaf00b5e24b6fc321
- Binance API Documentation: https://binance-docs.github.io/apidocs/
- aiogram Documentation: https://docs.aiogram.dev/en/latest/



