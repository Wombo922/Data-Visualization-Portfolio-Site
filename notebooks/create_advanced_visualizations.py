"""
Create Advanced Interactive Visualizations
Additional polish - multi-chart dashboards and correlation matrices
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

print("Creating advanced interactive visualizations...\n")

# ==============================================================================
# 1. MULTI-ASSET PERFORMANCE DASHBOARD
# ==============================================================================

print("1. Creating multi-asset performance dashboard...")

# Load stock and crypto data
stock_data = pd.read_csv('../data/processed/stock_market_processed.csv')
stock_data['date'] = pd.to_datetime(stock_data['date'])

crypto_data = pd.read_csv('../data/processed/crypto_processed.csv')
crypto_data['date'] = pd.to_datetime(crypto_data['date'])

# Create subplots dashboard
fig_dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Tech Stocks Price Trends', 'Crypto Price Trends',
                   'Stock Daily Returns Distribution', 'Crypto Volatility'),
    specs=[[{"secondary_y": False}, {"secondary_y": False}],
           [{"type": "histogram"}, {"secondary_y": False}]],
    vertical_spacing=0.12,
    horizontal_spacing=0.1
)

# Subplot 1: Stock prices
tickers = ['AAPL', 'MSFT', 'GOOGL']
colors_stock = {'AAPL': '#2E86AB', 'MSFT': '#A23B72', 'GOOGL': '#F18F01'}

for ticker in tickers:
    data = stock_data[stock_data['ticker'] == ticker]
    fig_dashboard.add_trace(
        go.Scatter(x=data['date'], y=data['close'], name=ticker,
                  line=dict(color=colors_stock[ticker], width=2)),
        row=1, col=1
    )

# Subplot 2: Crypto prices
cryptos = ['BTC', 'ETH']
colors_crypto = {'BTC': '#F7931A', 'ETH': '#627EEA'}

for coin in cryptos:
    data = crypto_data[crypto_data['coin'] == coin]
    fig_dashboard.add_trace(
        go.Scatter(x=data['date'], y=data['price'], name=coin,
                  line=dict(color=colors_crypto[coin], width=2)),
        row=1, col=2
    )

# Subplot 3: Stock returns histogram
for ticker in tickers:
    data = stock_data[stock_data['ticker'] == ticker]['daily_return'].dropna() * 100
    fig_dashboard.add_trace(
        go.Histogram(x=data, name=f'{ticker} Returns', opacity=0.6,
                    marker=dict(color=colors_stock[ticker])),
        row=2, col=1
    )

# Subplot 4: Crypto volatility
for coin in cryptos:
    data = crypto_data[crypto_data['coin'] == coin].dropna(subset=['volatility_30d'])
    fig_dashboard.add_trace(
        go.Scatter(x=data['date'], y=data['volatility_30d'], name=f'{coin} Vol',
                  line=dict(color=colors_crypto[coin], width=2)),
        row=2, col=2
    )

# Update layout
fig_dashboard.update_layout(
    title_text="Multi-Asset Market Dashboard: Stocks vs Crypto",
    title_font_size=22,
    height=800,
    showlegend=True,
    template='plotly_white',
    hovermode='x unified'
)

fig_dashboard.update_xaxes(title_text="Date", row=1, col=1)
fig_dashboard.update_xaxes(title_text="Date", row=1, col=2)
fig_dashboard.update_xaxes(title_text="Daily Return (%)", row=2, col=1)
fig_dashboard.update_xaxes(title_text="Date", row=2, col=2)

fig_dashboard.update_yaxes(title_text="Price (USD)", row=1, col=1)
fig_dashboard.update_yaxes(title_text="Price (USD)", row=1, col=2)
fig_dashboard.update_yaxes(title_text="Frequency", row=2, col=1)
fig_dashboard.update_yaxes(title_text="Volatility (%)", row=2, col=2)

fig_dashboard.write_html('../visualizations/interactive/multi_asset_dashboard.html')
print("  [OK] Multi-asset dashboard created")

# ==============================================================================
# 2. CORRELATION MATRIX HEATMAP (Interactive)
# ==============================================================================

print("\n2. Creating interactive correlation matrix...")

# Load stock correlation data
stock_corr = pd.read_csv('../data/processed/stock_correlations.csv', index_col=0)

# Create interactive heatmap
fig_corr = go.Figure(data=go.Heatmap(
    z=stock_corr.values,
    x=stock_corr.columns,
    y=stock_corr.index,
    colorscale='RdBu',
    zmid=0,
    text=stock_corr.values,
    texttemplate='%{text:.2f}',
    textfont={"size": 14, "family": "Arial Black"},
    hovertemplate='%{x} vs %{y}<br>Correlation: %{z:.3f}<extra></extra>',
    colorbar=dict(title="Correlation")
))

fig_corr.update_layout(
    title={
        'text': 'Tech Stock Correlation Matrix: How Tech Giants Move Together',
        'font': {'size': 22, 'family': 'Arial Black'}
    },
    xaxis_title='Stock Ticker',
    yaxis_title='Stock Ticker',
    height=600,
    width=700,
    template='plotly_white'
)

fig_corr.write_html('../visualizations/interactive/stock_correlation_matrix.html')
print("  [OK] Correlation matrix heatmap created")

# ==============================================================================
# 3. ANIMATED CRYPTO PRICE TRENDS
# ==============================================================================

print("\n3. Creating animated crypto price visualization...")

# Prepare data for animation
crypto_anim_data = crypto_data[crypto_data['coin'].isin(['BTC', 'ETH', 'SOL'])].copy()
crypto_anim_data['date_str'] = crypto_anim_data['date'].dt.strftime('%Y-%m-%d')

# Create animated scatter plot
fig_anim = px.scatter(
    crypto_anim_data,
    x='date',
    y='price',
    color='coin',
    size='volume',
    animation_frame='date_str',
    animation_group='coin',
    color_discrete_map={'BTC': '#F7931A', 'ETH': '#627EEA', 'SOL': '#14F195'},
    labels={'price': 'Price (USD)', 'date': 'Date', 'volume': 'Volume'},
    title='Animated Crypto Price Evolution with Volume',
    range_y=[0, crypto_anim_data['price'].max() * 1.1]
)

fig_anim.update_layout(
    height=600,
    template='plotly_white',
    title_font_size=22
)

fig_anim.write_html('../visualizations/interactive/crypto_animated_prices.html')
print("  [OK] Animated crypto visualization created")

# ==============================================================================
# 4. DEFI TVL COMPARISON WITH DROPDOWN
# ==============================================================================

print("\n4. Creating DeFi protocol comparison with dropdown selector...")

defi_data = pd.read_csv('../data/processed/defi_historical_processed.csv')
defi_data['date'] = pd.to_datetime(defi_data['date'])

# Create figure with all protocols
fig_defi_dropdown = go.Figure()

protocols = defi_data['protocol'].unique()
colors_defi = {
    'Uniswap': '#FF007A',
    'Aave': '#B6509E',
    'Compound': '#00D395',
    'Curve': '#0445FF',
    'Lido': '#73CBFF'
}

# Add all traces
for protocol in protocols:
    data = defi_data[defi_data['protocol'] == protocol]
    fig_defi_dropdown.add_trace(go.Scatter(
        x=data['date'],
        y=data['tvl_millions'],
        name=protocol,
        line=dict(color=colors_defi.get(protocol, '#333'), width=3),
        visible=True
    ))

# Create dropdown buttons for metrics
buttons = [
    dict(label="TVL (Millions)",
         method="update",
         args=[{"y": [defi_data[defi_data['protocol'] == p]['tvl_millions'].values for p in protocols]},
               {"yaxis.title.text": "TVL (Millions USD)"}]),
    dict(label="Daily Volume",
         method="update",
         args=[{"y": [defi_data[defi_data['protocol'] == p]['daily_volume'].values for p in protocols]},
               {"yaxis.title.text": "Daily Volume (Millions USD)"}]),
    dict(label="User Count",
         method="update",
         args=[{"y": [defi_data[defi_data['protocol'] == p]['users_count'].values for p in protocols]},
               {"yaxis.title.text": "Active Users"}])
]

fig_defi_dropdown.update_layout(
    title={
        'text': 'DeFi Protocol Metrics: Interactive Comparison',
        'font': {'size': 22, 'family': 'Arial Black'}
    },
    xaxis_title='Date',
    yaxis_title='TVL (Millions USD)',
    hovermode='x unified',
    template='plotly_white',
    height=600,
    updatemenus=[dict(
        active=0,
        buttons=buttons,
        direction="down",
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.15,
        xanchor="left",
        y=1.15,
        yanchor="top"
    )]
)

fig_defi_dropdown.write_html('../visualizations/interactive/defi_comparison_dropdown.html')
print("  [OK] DeFi dropdown comparison created")

# ==============================================================================
# 5. SENTIMENT VS PRICE CORRELATION
# ==============================================================================

print("\n5. Creating sentiment vs price correlation chart...")

sentiment_data = pd.read_csv('../data/processed/social_sentiment_processed.csv')
sentiment_data['date'] = pd.to_datetime(sentiment_data['date'])

# Merge sentiment with crypto prices
sentiment_crypto = sentiment_data.merge(
    crypto_data[['date', 'coin', 'price']],
    on=['date', 'coin'],
    how='inner'
)

# Create scatter with trendline
fig_sent_price = px.scatter(
    sentiment_crypto,
    x='sentiment_score',
    y='price',
    color='coin',
    trendline='ols',
    title='Social Sentiment vs Price: Does Buzz Drive Value?',
    labels={'sentiment_score': 'Sentiment Score (0-100)', 'price': 'Price (USD)'},
    height=600
)

fig_sent_price.update_layout(
    template='plotly_white',
    title_font_size=22
)

fig_sent_price.write_html('../visualizations/interactive/sentiment_price_correlation.html')
print("  [OK] Sentiment vs price correlation created")

print("\n[SUCCESS] All advanced visualizations created!")
print("\nNew files created:")
print("  - multi_asset_dashboard.html")
print("  - stock_correlation_matrix.html")
print("  - crypto_animated_prices.html")
print("  - defi_comparison_dropdown.html")
print("  - sentiment_price_correlation.html")
