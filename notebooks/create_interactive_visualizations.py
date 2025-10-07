"""
Create Interactive Plotly Visualizations for Portfolio
Week 2 - Day 1-3: Interactive visualizations
"""

import pandas as pd
import plotly.graph_objects as go

# ==============================================================================
# 1. STOCK MARKET INTERACTIVE VISUALIZATION
# ==============================================================================

print("Creating interactive stock market visualization...")

# Load data
stock_data = pd.read_csv('../data/processed/stock_market_processed.csv')
stock_data['date'] = pd.to_datetime(stock_data['date'])

# Create interactive line chart with all stocks
fig_stocks = go.Figure()

tickers = stock_data['ticker'].unique()
colors = {'AAPL': '#2E86AB', 'MSFT': '#A23B72', 'GOOGL': '#F18F01',
          'META': '#C73E1D', 'NVDA': '#6A994E'}

for ticker in tickers:
    data = stock_data[stock_data['ticker'] == ticker]
    fig_stocks.add_trace(go.Scatter(
        x=data['date'],
        y=data['close'],
        mode='lines',
        name=ticker,
        line=dict(color=colors.get(ticker, '#333'), width=3),
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     'Date: %{x|%Y-%m-%d}<br>' +
                     'Price: $%{y:,.2f}<br>' +
                     '<extra></extra>'
    ))

fig_stocks.update_layout(
    title={
        'text': 'Tech Stock Price Trends: FAANG Performance Over 2 Years',
        'font': {'size': 24, 'family': 'Arial Black'}
    },
    xaxis_title='Date',
    yaxis_title='Stock Price (USD)',
    hovermode='x unified',
    template='plotly_white',
    height=600,
    font=dict(size=12),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(size=14)
    ),
    xaxis=dict(
        rangeslider=dict(visible=True),
        type='date'
    )
)

fig_stocks.write_html('../visualizations/interactive/stock_price_trends.html')
print("  [OK] Stock price trends interactive chart saved")

# ==============================================================================
# 2. CRYPTO VOLATILITY INTERACTIVE VISUALIZATION
# ==============================================================================

print("\nCreating interactive crypto volatility visualization...")

# Load data
crypto_data = pd.read_csv('../data/processed/crypto_processed.csv')
crypto_data['date'] = pd.to_datetime(crypto_data['date'])

# Create interactive volatility comparison
fig_crypto_vol = go.Figure()

crypto_colors = {'BTC': '#F7931A', 'ETH': '#627EEA', 'SOL': '#14F195', 'MATIC': '#8247E5'}

for coin in crypto_data['coin'].unique():
    data = crypto_data[crypto_data['coin'] == coin].dropna(subset=['volatility_30d'])
    fig_crypto_vol.add_trace(go.Scatter(
        x=data['date'],
        y=data['volatility_30d'],
        mode='lines',
        name=coin,
        line=dict(color=crypto_colors.get(coin, '#333'), width=3),
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     'Date: %{x|%Y-%m-%d}<br>' +
                     'Volatility: %{y:.2f}%<br>' +
                     '<extra></extra>'
    ))

fig_crypto_vol.update_layout(
    title={
        'text': 'Cryptocurrency 30-Day Rolling Volatility: Risk Comparison',
        'font': {'size': 24, 'family': 'Arial Black'}
    },
    xaxis_title='Date',
    yaxis_title='Annualized Volatility (%)',
    hovermode='x unified',
    template='plotly_white',
    height=600,
    font=dict(size=12),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(size=14)
    )
)

fig_crypto_vol.write_html('../visualizations/interactive/crypto_volatility.html')
print("  [OK] Crypto volatility interactive chart saved")

# Risk vs Return scatter
risk_return = pd.read_csv('../data/processed/crypto_risk_return.csv')

fig_risk_return = go.Figure()

fig_risk_return.add_trace(go.Scatter(
    x=risk_return['avg_volatility'],
    y=risk_return['annualized_return'],
    mode='markers+text',
    text=risk_return['coin'],
    textposition='top center',
    textfont=dict(size=16, family='Arial Black'),
    marker=dict(
        size=30,
        color=risk_return['annualized_return'],
        colorscale='RdYlGn',
        showscale=True,
        colorbar=dict(title="Return %"),
        line=dict(width=2, color='white')
    ),
    hovertemplate='<b>%{text}</b><br>' +
                 'Volatility: %{x:.2f}%<br>' +
                 'Return: %{y:.2f}%<br>' +
                 '<extra></extra>'
))

fig_risk_return.update_layout(
    title={
        'text': 'Crypto Risk vs Return: Find the Sweet Spot',
        'font': {'size': 24, 'family': 'Arial Black'}
    },
    xaxis_title='Average Volatility (% Annualized)',
    yaxis_title='Annualized Return (%)',
    template='plotly_white',
    height=600,
    font=dict(size=12),
    showlegend=False
)

fig_risk_return.add_hline(y=0, line_dash="dash", line_color="gray",
                         annotation_text="Break-even", annotation_position="right")

fig_risk_return.write_html('../visualizations/interactive/crypto_risk_return.html')
print("  [OK] Crypto risk-return interactive scatter saved")

# ==============================================================================
# 3. DEFI PROTOCOL INTERACTIVE VISUALIZATION
# ==============================================================================

print("\nCreating interactive DeFi protocol visualization...")

# Load data
defi_data = pd.read_csv('../data/processed/defi_historical_processed.csv')
defi_data['date'] = pd.to_datetime(defi_data['date'])

# Create interactive TVL trends
fig_defi = go.Figure()

protocol_colors = {
    'Uniswap': '#FF007A',
    'Aave': '#B6509E',
    'Compound': '#00D395',
    'Curve': '#0445FF',
    'Lido': '#73CBFF'
}

for protocol in defi_data['protocol'].unique():
    data = defi_data[defi_data['protocol'] == protocol]
    fig_defi.add_trace(go.Scatter(
        x=data['date'],
        y=data['tvl_millions'],
        mode='lines',
        name=protocol,
        line=dict(color=protocol_colors.get(protocol, '#333'), width=3),
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     'Date: %{x|%Y-%m-%d}<br>' +
                     'TVL: $%{y:,.0f}M<br>' +
                     '<extra></extra>'
    ))

fig_defi.update_layout(
    title={
        'text': 'DeFi Protocol Total Value Locked: 6-Month Battle for Dominance',
        'font': {'size': 24, 'family': 'Arial Black'}
    },
    xaxis_title='Date',
    yaxis_title='Total Value Locked (Millions USD)',
    hovermode='x unified',
    template='plotly_white',
    height=600,
    font=dict(size=12),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(size=14)
    )
)

fig_defi.write_html('../visualizations/interactive/defi_tvl_trends.html')
print("  [OK] DeFi TVL trends interactive chart saved")

# Growth rates bar chart
growth_data = pd.read_csv('../data/processed/defi_growth_rates.csv')
growth_data = growth_data.sort_values('growth_30d', ascending=True)

fig_growth = go.Figure()

colors_growth = ['#d62728' if x < 0 else '#2ca02c' for x in growth_data['growth_30d']]

fig_growth.add_trace(go.Bar(
    y=growth_data['protocol'],
    x=growth_data['growth_30d'],
    orientation='h',
    marker=dict(
        color=colors_growth,
        line=dict(color='white', width=2)
    ),
    text=[f"{val:.1f}%" for val in growth_data['growth_30d']],
    textposition='outside',
    hovertemplate='<b>%{y}</b><br>' +
                 '30-Day Growth: %{x:.2f}%<br>' +
                 '<extra></extra>'
))

fig_growth.update_layout(
    title={
        'text': 'DeFi 30-Day Growth Rates: Winners & Losers',
        'font': {'size': 24, 'family': 'Arial Black'}
    },
    xaxis_title='Growth Rate (%)',
    yaxis_title='Protocol',
    template='plotly_white',
    height=500,
    font=dict(size=12),
    showlegend=False
)

fig_growth.add_vline(x=0, line_dash="solid", line_color="black", line_width=1)

fig_growth.write_html('../visualizations/interactive/defi_growth_rates.html')
print("  [OK] DeFi growth rates interactive chart saved")

# ==============================================================================
# 4. SOCIAL SENTIMENT INTERACTIVE VISUALIZATION
# ==============================================================================

print("\nCreating interactive social sentiment visualization...")

# Load data
sentiment_data = pd.read_csv('../data/processed/social_sentiment_processed.csv')
sentiment_data['date'] = pd.to_datetime(sentiment_data['date'])

# Create interactive sentiment heatmap
fig_sentiment = go.Figure()

for coin in sentiment_data['coin'].unique():
    data = sentiment_data[sentiment_data['coin'] == coin]
    fig_sentiment.add_trace(go.Scatter(
        x=data['date'],
        y=data['sentiment_score'],
        mode='lines+markers',
        name=coin,
        line=dict(width=3),
        marker=dict(size=6),
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     'Date: %{x|%Y-%m-%d}<br>' +
                     'Sentiment: %{y:.1f}/100<br>' +
                     '<extra></extra>'
    ))

fig_sentiment.update_layout(
    title={
        'text': 'Crypto Social Sentiment Tracker: What\'s Buzzing?',
        'font': {'size': 24, 'family': 'Arial Black'}
    },
    xaxis_title='Date',
    yaxis_title='Sentiment Score (0-100)',
    hovermode='x unified',
    template='plotly_white',
    height=600,
    font=dict(size=12),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(size=14)
    ),
    yaxis=dict(range=[0, 100])
)

fig_sentiment.add_hline(y=50, line_dash="dash", line_color="gray",
                       annotation_text="Neutral", annotation_position="right")

fig_sentiment.write_html('../visualizations/interactive/social_sentiment.html')
print("  [OK] Social sentiment interactive chart saved")

print("\n[SUCCESS] All interactive visualizations created successfully!")
print("\nFiles saved to: visualizations/interactive/")
print("  - stock_price_trends.html")
print("  - crypto_volatility.html")
print("  - crypto_risk_return.html")
print("  - defi_tvl_trends.html")
print("  - defi_growth_rates.html")
print("  - social_sentiment.html")
