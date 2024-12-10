Project Proposal
1. Name of Project:

Tesla Attention Analysis


2. Type of Project:

Type: Data Project (B1)


3. Brief Description of the Purpose:

The purpose of this project is to analyze the relationship between public attention, as measured by Google Trends data, and the weekly percentage change in Tesla's stock price. The analysis aims to explore patterns and potential correlations between public interest and stock market fluctuations.


4. Links to Data Sources / API:

Data sources used in this project include:
- Google Trends API (via the Pytrends Python package) to obtain historical weekly search interest data for Tesla.
- Yahoo Finance API (via the yfinance Python package) to fetch Tesla's historical stock price data.


5. Outline the Technical Steps / Challenges:

The project involves the following technical steps:
- Using the Pytrends Python package to retrieve weekly Google Trends data for Tesla.
- Using the yfinance Python package to fetch Tesla's weekly stock price data.
- Merging the datasets on a common time index (week).
- Calculating weekly percentage changes in Tesla's stock price.
- Visualizing the combined dataset with dual y-axes, displaying public attention and stock price percentage changes.
- Packaging the project as a Python package using Poetry, including the datasets, analysis functions, and visualization tools.
- Challenges include handling rate limits while fetching data from Google Trends, aligning weekly data, and ensuring proper scaling in visualizations.


6. Significant Hurdles and Their Impact

The following hurdles could impact the project's completion:
- **Rate Limits**: Google Trends imposes rate limits, which may delay data retrieval. If unresolved, the project may lack comprehensive attention data.
- **Data Alignment**: Discrepancies in time indices between datasets could lead to misaligned data. Resolving this is critical to meaningful analysis.
- **PyPI Publishing**: Issues in packaging and publishing the project to PyPI could hinder the final deliverable.
