import yfinance as yf
import pandas as pd
from datetime import datetime

class Stock:
    def __init__(self, ticker, purchaseDate, competitors = []):
        self.ticker = ticker
        self.purchaseDate = purchaseDate
        self.competitors = competitors

        self.stockData = yf.download(ticker, start=purchaseDate, end = datetime.today().strftime('%Y-%m-%d'))
        self.tickerInfo = yf.Ticker(ticker)

        self.currentPrice = round(self.stockData['Close'].iloc[-1][ticker], 2)
        self.purchasePrice = round(self.stockData.loc[purchaseDate]['Open'].item(), 2)
        self.percentageDif = round((self.currentPrice - self.purchasePrice) / self.purchasePrice, 2) * 100
        self.profitOrLoss = '+' if self.currentPrice - self.purchasePrice >= 0 else '-'
        self.trailingPEratio = round(self.tickerInfo.info.get('trailingPE'), 2)
        self.forwardPERatio = round(self.tickerInfo.info.get('forwardPE'), 2)
    
    def averagePEofCompetitors(self):
        if len(self.competitors) == 0:
            return 0
        totalPE = 0.0
        validCount = 0
        for ticker in self.competitors:
            currentPE = yf.Ticker(ticker).info.get('trailingPE')
            if currentPE != None:
                totalPE += currentPE
                validCount += 1
        averagePE = round((totalPE / validCount), 2)
        return averagePE

if __name__ == "__main__":
    Valeura = Stock(
        'VLE.TO',
        '2025-03-10',
        ['FRU.TO', 'VET.TO', 'IPCO.TO', 'AAV.TO', 'BIR.TO', 'HWX.TO', 'KEL.TO', 'CJ.TO', 'PXT.TO']
    )

    print(f'--------------Valeura Energy Inc--------------')
    print(f'Purchase Price: {Valeura.purchasePrice}')
    print(f'Current Price: {Valeura.currentPrice}')
    print(f'Purchase Date: {Valeura.purchaseDate}')
    print(f'Return: {Valeura.profitOrLoss}{Valeura.percentageDif}%')
    print(f'Valeura PE: {Valeura.trailingPEratio}')
    print(f'Competitor PE Avg: {Valeura.averagePEofCompetitors()}')