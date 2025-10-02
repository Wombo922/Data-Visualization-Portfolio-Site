# Data Visualization Portfolio

A collection of data analysis and visualization projects showcasing analytical thinking and storytelling with data.

## Author
**Anthony Galindo**
Mathematics Graduate | Computer Science Student
[anthonygalindo922@gmail.com](mailto:anthonygalindo922@gmail.com)

## Projects

### 1. Tech Stock Market Analysis
**Focus:** Correlation analysis of major tech stocks (AAPL, MSFT, GOOGL, META, NVDA)
**Key Insight:** MSFT & META show strongest correlation (0.62), while NVDA demonstrates most independence - diversification benefits lower than expected
**Tools:** Python, pandas, matplotlib, Polygon.io API
**Notebook:** `notebooks/1_stock_market_analysis.ipynb`

### 2. Cryptocurrency Volatility Analysis
**Focus:** Comparing volatility patterns and risk metrics across BTC, ETH, SOL, MATIC
**Key Insight:** ETH delivered 88.6% returns but with 74.6% volatility - BTC offers better risk-adjusted returns at 76.7% returns with only 42.8% volatility
**Tools:** Python, pandas, matplotlib, CoinGecko API
**Notebook:** `notebooks/2_crypto_volatility_analysis.ipynb`

### 3. Crypto Social Sentiment Analysis
**Focus:** Social media buzz tracking and sentiment scoring for cryptocurrencies
**Key Insight:** SOL leads sentiment (73.0 score) while DOGE has highest social volume (119K mentions) - sentiment doesn't always correlate with price performance
**Tools:** Python, pandas, matplotlib, LunarCrush API, CoinGecko API
**Notebook:** `notebooks/3_crypto_social_sentiment.ipynb`

### 4. DeFi Protocol Market Intelligence
**Focus:** Total Value Locked (TVL) trends across major DeFi protocols
**Key Insight:** Lido dominates with $15B TVL (45% market share), Uniswap showing strongest growth at 11.2% over 30 days
**Tools:** Python, pandas, matplotlib, Messari API
**Notebook:** `notebooks/4_market_intelligence_analysis.ipynb`

## Project Structure
```
data-viz-portfolio/
├── data/
│   ├── raw/              # Original datasets
│   └── processed/        # Cleaned data
├── notebooks/
│   ├── 1_stock_market_analysis.ipynb
│   ├── 2_crypto_volatility_analysis.ipynb
│   ├── 3_crypto_social_sentiment.ipynb
│   └── 4_market_intelligence_analysis.ipynb
├── visualizations/
│   ├── static/           # PNG/JPG images
│   └── interactive/      # HTML files with interactive charts
├── site/
│   ├── index.html
│   ├── style.css
│   └── projects/
└── README.md
```

## Technologies Used
- **Python 3.13**
- **pandas** - Data manipulation and analysis
- **matplotlib** - Static visualizations
- **seaborn** - Statistical data visualization
- **plotly** - Interactive visualizations
- **Jupyter** - Notebook environment

## Data Sources
- [Polygon.io](https://polygon.io/) - Stock market data
- [CoinGecko](https://www.coingecko.com/) - Cryptocurrency data and trending coins
- [LunarCrush](https://lunarcrush.com/) - Social sentiment analysis
- [Messari](https://messari.io/) - Crypto market intelligence

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/data-viz-portfolio.git
cd data-viz-portfolio
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

4. Open any notebook in the `notebooks/` folder to run the analysis

## Running the Analysis
1. Open the desired notebook (e.g., `1_stock_market_analysis.ipynb`)
2. Run all cells in order (Cell → Run All)
3. Visualizations will be saved to `visualizations/static/`
4. Processed data will be saved to `data/processed/`

## Live Portfolio Site
[Coming soon - Will be deployed on GitHub Pages]

## Skills Demonstrated
- Data collection from APIs
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Statistical analysis and correlation studies
- Time series analysis
- Data visualization design
- Interactive dashboard creation
- Storytelling with data

## Contact
- Email: anthonygalindo922@gmail.com
- GitHub: [DirtyWombo](https://github.com/DirtyWombo)
- LinkedIn: [Your LinkedIn Profile]

---

## Development Timeline
- **Week 1:** Data collection, cleaning, and exploratory analysis ✅
- **Week 2:** Interactive visualizations and website development ✅

## Project Stats
- **4 Complete Projects** with analysis notebooks
- **16 Static Visualizations** (matplotlib/seaborn)
- **6 Interactive Charts** (Plotly)
- **2+ Years** of market data analyzed
- **15+ APIs** utilized for data collection
- **Professional Portfolio Site** with responsive design

Last Updated: 2025-10-01
