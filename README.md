# 📊 Data Visualization Portfolio

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live-green.svg)](https://github.com/DirtyWombo/data-viz-portfolio)

> A comprehensive collection of financial market and cryptocurrency data analysis projects demonstrating end-to-end data science capabilities—from API data collection to interactive web-based visualizations.

**👨‍💻 Author:** Anthony Galindo
**🎓 Background:** Mathematics Graduate | Computer Science Student
**📧 Contact:** [anthonygalindo922@gmail.com](mailto:anthonygalindo922@gmail.com) | [LinkedIn](https://linkedin.com/in/anthony-galindo) | [GitHub](https://github.com/DirtyWombo)

---

## 🎯 Overview

This portfolio showcases proficiency in data analysis, statistical modeling, and professional data visualization through four comprehensive projects analyzing **financial markets**, **cryptocurrency ecosystems**, **social sentiment trends**, and **DeFi protocols**.

## 📁 Projects

### 1. 📈 Tech Stock Market Correlation Analysis

**Objective:** Identify correlation patterns and diversification opportunities among FAANG stocks (AAPL, MSFT, GOOGL, META, NVDA)

**Key Findings:**
- MSFT & META exhibit strongest correlation (0.62), indicating synchronized movement
- NVDA demonstrates highest independence, offering superior diversification value
- All stocks positively correlated (0.37-0.62), suggesting sector-wide cohesion
- Diversification benefits within tech sector are lower than expected

**Technologies:** Python, pandas, matplotlib, seaborn, Polygon.io API
**Analysis Period:** 2-year historical data | **Notebook:** [`1_stock_market_analysis.ipynb`](notebooks/1_stock_market_analysis.ipynb)

---

### 2. 💹 Cryptocurrency Volatility & Risk Analysis

**Objective:** Quantify risk-return profiles and volatility patterns across major cryptocurrencies (BTC, ETH, SOL, MATIC)

**Key Findings:**
- ETH delivered 88.6% returns but with 74.6% volatility—high risk, high reward
- BTC offers superior risk-adjusted performance: 76.7% returns at 42.8% volatility
- SOL exhibits extreme volatility: 81.6% returns with 83.9% volatility
- MATIC demonstrates downside risk with -8.0% returns
- Critical insight: Higher volatility does not guarantee proportional returns

**Technologies:** Python, pandas, matplotlib, seaborn, CoinGecko API
**Metrics:** 30-day rolling volatility, Sharpe ratios, annualized returns | **Notebook:** [`2_crypto_volatility_analysis.ipynb`](notebooks/2_crypto_volatility_analysis.ipynb)

---

### 3. 🗣️ Crypto Social Sentiment Analysis

**Objective:** Track social media buzz and sentiment to identify market perception trends

**Key Findings:**
- SOL leads with 73.0 sentiment score, indicating strong community support
- DOGE maintains highest social volume (119K mentions) despite price volatility
- ETH shows consistent institutional backing with 66.8 sentiment score
- Critical insight: Social sentiment does not always correlate with price performance
- Social volume and sentiment provide complementary market signals

**Technologies:** Python, pandas, matplotlib, LunarCrush API, CoinGecko API
**Data Sources:** Sentiment scores (0-100), social volume, trending rankings | **Notebook:** [`3_crypto_social_sentiment.ipynb`](notebooks/3_crypto_social_sentiment.ipynb)

---

### 4. 🏦 DeFi Protocol Market Intelligence

**Objective:** Analyze Total Value Locked (TVL) trends and market share dynamics across leading DeFi protocols

**Key Findings:**
- Lido dominates liquid staking sector with ~$15B TVL (45% market share)
- Uniswap demonstrates strongest growth at 11.2% monthly increase
- Aave maintains stability at $6B TVL despite competitive pressure
- Curve experienced slight decline (-0.1%), indicating market maturation
- Market concentration risk: Top protocol controls 45% of analyzed TVL

**Technologies:** Python, pandas, matplotlib, seaborn, Messari API
**Analysis Period:** 180-day trend analysis | **Protocols:** Uniswap, Aave, Compound, Curve, Lido | **Notebook:** [`4_market_intelligence_analysis.ipynb`](notebooks/4_market_intelligence_analysis.ipynb)

## Project Structure
```
data-viz-portfolio/
├── data/
│   ├── raw/              # Original datasets from APIs
│   └── processed/        # Cleaned and processed data
├── notebooks/
│   ├── 1_stock_market_analysis.ipynb
│   ├── 2_crypto_volatility_analysis.ipynb
│   ├── 3_crypto_social_sentiment.ipynb
│   ├── 4_market_intelligence_analysis.ipynb
│   ├── create_interactive_visualizations.py
│   └── create_advanced_visualizations.py
├── visualizations/
│   ├── static/           # PNG/JPG charts for portfolio
│   └── interactive/      # Interactive Plotly HTML charts
├── site/
│   ├── index.html        # Main portfolio page
│   ├── style.css         # Global styling
│   ├── resume.html       # Interactive resume (print to PDF)
│   ├── playground.html   # Data exploration playground
│   └── assets/
│       └── Anthony_Galindo_Resume.pdf
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies Used

### Data Analysis & Visualization
- **Python 3.13** - Primary programming language
- **pandas** - Data manipulation and analysis
- **matplotlib** - Static visualizations
- **seaborn** - Statistical data visualization
- **plotly** - Interactive visualizations
- **Jupyter** - Notebook environment
- **requests** - API data collection

### Web Technologies
- **HTML5/CSS3** - Portfolio website structure and styling
- **JavaScript (ES6+)** - Interactive features and data playground
- **Chart.js** - Dynamic charting in data playground
- **PapaParse** - CSV parsing for client-side data loading

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
git clone https://github.com/DirtyWombo/data-viz-portfolio.git
cd data-viz-portfolio
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. **Set up API Keys** (Required for data collection):
   - Get free API keys from:
     - [Polygon.io](https://polygon.io/) - Stock market data
     - [CoinGecko](https://www.coingecko.com/) - Cryptocurrency data
     - [LunarCrush](https://lunarcrush.com/) - Social sentiment (optional)
     - [Messari](https://messari.io/) - DeFi data (optional)
   - Replace placeholders in notebooks:
     - `YOUR_POLYGON_API_KEY` in `1_stock_market_analysis.ipynb`
     - `YOUR_API_KEY` in other notebooks

4. Launch Jupyter Notebook:
```bash
jupyter notebook
```

5. Open any notebook in the `notebooks/` folder to run the analysis

## Running the Analysis
1. Open the desired notebook (e.g., `1_stock_market_analysis.ipynb`)
2. Run all cells in order (Cell → Run All)
3. Visualizations will be saved to `visualizations/static/`
4. Processed data will be saved to `data/processed/`

## Portfolio Features
- **Interactive Search & Filtering** - Real-time project search and category filters
- **Code Snippets** - Collapsible Python code examples with copy-to-clipboard functionality
- **Chart Lightbox** - Click any chart for fullscreen viewing with zoom capabilities
- **Data Playground** - Interactive data exploration with Chart.js (switch datasets, chart types, and filters)
- **Downloadable Resume** - PDF resume available for download
- **Dark Mode** - Smooth toggle between light and dark themes with localStorage persistence
- **Modern Gradient Design** - Professional purple-to-violet gradient buttons with hover animations
- **Back-to-Top Button** - Convenient scrolling for long project lists
- **Responsive Design** - Mobile-first layout that works seamlessly on all devices
- **Scroll Progress Indicator** - Visual feedback showing reading progress

## Live Portfolio Site

### 🌐 Viewing the Portfolio Locally

**IMPORTANT:** The server must run from the **project root directory**, not from `site/`

```bash
# Navigate to project root
cd data-viz-portfolio

# Start the server
python -m http.server 8000
```

Then open your browser and visit:
- **Main Portfolio:** http://localhost:8000/site/index.html
- **Data Playground:** http://localhost:8000/site/playground.html
- **Resume:** http://localhost:8000/site/resume.html

**Why from project root?** The HTML files use relative paths (`../visualizations/`) to access images and interactive charts in the parent directory. Running the server from `site/` will cause 404 errors.

### 🚀 Deployment

**Coming Soon** - Portfolio will be deployed to GitHub Pages

For deployment instructions, see [QUICK_START.md](QUICK_START.md)

## Troubleshooting

### Interactive Charts Show 404 Errors
**Problem:** Interactive visualizations or static images not loading
**Solution:** Ensure the server is running from the **project root**, not from `site/` directory

### Playground Charts Not Loading
**Problem:** Data playground shows "Error loading data"
**Solution:**
1. Verify server is running from project root
2. Access via `http://localhost:8000/site/playground.html` (not `file://`)
3. Check browser console for CORS errors

### Images Not Displaying
**Problem:** Chart images broken or showing 404
**Solution:** Check that you're accessing the site via `http://localhost:8000/site/index.html`

### Port Already in Use
**Problem:** Error "Address already in use"
**Solution:**
```bash
# Use a different port
python -m http.server 8001

# Then visit http://localhost:8001/site/index.html
```

For more help, see [QUICK_START.md](QUICK_START.md)

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
- **Email:** anthonygalindo922@gmail.com
- **GitHub:** [DirtyWombo](https://github.com/DirtyWombo)
- **LinkedIn:** [anthony-galindo](https://linkedin.com/in/anthony-galindo)
- **Portfolio:** View live site once deployed to GitHub Pages

---

## Development Timeline
- **Week 1:** Data collection, cleaning, and exploratory analysis ✅
- **Week 2:** Interactive visualizations and website development ✅

## Project Stats
- **4 Complete Projects** with analysis notebooks
- **16 Static Visualizations** (matplotlib/seaborn)
- **11 Interactive Charts** (Plotly)
- **2+ Years** of market data analyzed
- **15+ APIs** utilized for data collection
- **Professional Portfolio Site** with responsive design
- **27 Total Visualizations** across all projects

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Last Updated:** January 2025

---

<div align="center">

**⭐ If you found this portfolio helpful, please consider starring the repository!**

Made with 💜 by [Anthony Galindo](https://github.com/DirtyWombo)

</div>
