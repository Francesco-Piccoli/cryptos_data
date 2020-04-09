**Crypto open data

**Authors: **Francesco Piccoli, Carlos Nunez

**Problem**

Cryptocurrencies’ price has so far been highly volatile and unpredictable, leading to either large profits or large losses. Trading volume has often been correlated to price movements, but this superficial correlation can easily be biased by big players moving large quantities of money back and forth from their accounts. This trading volume is often referred to as “fake volume” and it is easy to understand how it is not significant in assessing cryptocurrencies’ value. Are there other signals that can be used to predict what the price of a particular cryptocurrency will be in the future? 

**Solution**

Gathering data related to different cryptocurrencies from different online sources, which could be used to study price correlations and build investment strategies.

**Value proposition**

Data is currently largely dispersed around the web, and valuable information has to be accessed from several different sources, cleaned, and organized before someone can analyze it. At present, some startups offer similar solutions, which require you to pay to access them. These datasets usually contain information about historical price and volume, but don’t put into consideration fake volume, social media interest, or search engine queries. While it’s very hard to accurately assess the size of fake volume, interest over time might signal the existence of some red flags. 

**Data sources** 

As previously mentioned, there is a lot of publicly available information online related to the cryptocurrency space. We decided to concentrate on the three main coins in terms of traded volume, namely Bitcoin, Ethereum, and XRP. The data we are collecting is either hourly or daily data. More specifically, we are collecting data from: 



*   XRP Data API (volume, fees, accounts created).
*   Bitcoin BigQuery open dataset (volume, fees, accounts created).
*   Ethereum BigQuery open dataset (volume, fees, accounts created).
*   Google Trends, using the pytrends API from GeneralMills (historical volume of queries for the following keywords: Ripple, XRP, Coinbase, cryptocurrencies, Ethereum, Bitcoin, Binance).
*   Reddit, using the pushshift API, and performing web scraping on redditmetrics.com (each crypto has its own subreddit, from which we get: number of posts per day, new subscribers, number of comments).
*   Twitter conversations on cryptos (number of ripple’s tweet per day, number of conversations with hashtags #XRP or #Bitcoin).
*   Wikipedia page views, using the mwviews API.
*   Cryptocompare API (historical aggregated prices across different exchanges).

Not all this data is available from the same starting date. As a common starting point, we picked January 1st, 2017, which will allow us to collect information before the explosion of the cryptocurrency bubble at the beginning of 2018. 

**Database creation and structure**

Considering the different data sources mentioned above, the first decision was where we would store all this data. Considering the different options available at local and cloud level, we decided to create a database instance in AWS DBS, mainly because of the power of integration with other AWS services, such as automation and execution of scripts in the cloud, and the convenient free offer from Amazon, among others.

The second step was to connect this instance to MySQL Workbench, a visual tool that allows easy database manipulation, and with which Carlos had already worked in past projects. However, the tool was only useful for the creation of the schema/tables to be used, since all the data loading and row modification was developed in python using the pymysql module.

That said, so far our tables look like this:

![alt_text](images/Midterm-report0.png "image_tooltip")


The table crypto_currency_hourly has an id composed of date + time + currency, to make each id unique in terms of name. The table contains data from the google queries for each currency and some exchange platforms. Besides that, it also contains information about the price of each cryptocurrency in different categories. Finally, the table stores information about the transaction volume for each coin.

![alt_text](images/Midterm-report1.png "image_tooltip")


The table crypto_currency_daily has the date as the id since it is unique for each row in this table. At this moment, the table has the number of Wikipedia views for each coin, platform and the cryptocurrency term per day. We expect to add the Reddit data during the next days.

**Visualization**

Our goal is to provide users different views of data and how correlated those are to help them to understand how data have changed over the time, and provide a tool to make predictions about whether the price of the XRP currency will rise or drop in the short term, using the data they consider most relevant. In fact, the project is a spin-off of Francesco’s capstone project with Ripple, the Blockchain company that created the XRP coin.

The first goal led us to make a visualization dashboard that provides the users the capability to play with data and visualize it as they wish. Using the BI tool PowerBI, we were able to connect our database to a bunch of different BI options to visualize price changes, Wikipedia views over time, etc. The following images show part of the work done so far.

![alt_text](images/Midterm-report2.png "image_tooltip")


Viz 1: Google queries breakdown per day and per coin/platform.


![alt_text](images/Midterm-report3.png "image_tooltip")


Viz 2: Average close price per day per coin.

**Next steps**
