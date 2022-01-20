import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

st.title("Crpytocurrency Daily Prices")
st.header("Dashboard")
st.subheader("A site which shows the prices of various Crypto currencies from a particular date to a particular date")

Bitcoin = 'BTC-INR'
Ethereum = 'ETH-INR'
Ripple = 'XRP-INR'
BitcoinCash = 'BCH-INR'

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

BTC = yf.download(Bitcoin, start="2021-12-17", end="2021-12-17")
ETH = yf.download(Ethereum, start="2021-12-17", end="2021-12-17")
XRP = yf.download(Ripple, start="2021-12-17", end="2021-12-17")
BCH = yf.download(BitcoinCash, start="2021-12-17", end="2021-12-17")

#1
st.write("BITCOIN IN INR (₹)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)

st.table(BTC)

st.bar_chart(BTCHis.Close)

#2
st.write("ETHEREUM IN INR (₹)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH)

st.table(ETH)

st.bar_chart(ETHHis.Close)

#3
st.write("RIPPLE IN INR (₹)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP)

st.table(XRP)

st.bar_chart(XRPHis.Close)

#4
st.write("BITCOIN CASH IN INR (₹)")
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH)

st.table(BCH)

st.bar_chart(BCHHis.Close)