from iqoptionlibrary import *
from smalibrary import *
import sys

# print("connecting to iq option")
# connect()
#
# getbalance()
#
# liveorpaper()

tickerlist = str(config['appstate']['ticker']).split(",")

print(tickerlist)

for tickers in tickerlist:
    ticker = tickers.replace("/", "")
    getsma(ticker, period=6, timeframe=2)


while True:
    if len(status) == 1 and status[0] == 1:
        status.clear()

        try:
            for tickers in tickerlist:
                ticker = tickers.replace("/", "")

                liveprice = smadict[ticker]['sma'][0]
                smadict[ticker]['sma'].clear()

                smacross(liveprice)
        except:
            print("cannot calc sma")
            traceback.print_exc()





