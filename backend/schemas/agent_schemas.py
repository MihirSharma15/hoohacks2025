from typing import Optional
from pydantic import BaseModel, Field


class Transcription(BaseModel):
    """
    A simple transcription schema.
    """

    transcript: str = Field(description="The transcribed text from the audio file.")


class News(BaseModel):
    """A single news article."""

    title: str = Field(description="The title of the news article.")
    url: str = Field(description="The URL of the news article.")


class NewsCollections(BaseModel):
    """
    A collection of news articles.
    """

    summary: str = Field(description="Concise response to user's query")
    articles: list[News] = Field(description="List of news articles.")


class StockData(BaseModel):
    """General stock data."""

    ticker: Optional[str] = Field(None, description="")
    address1: Optional[str] = Field(
        None, description="This describes the stock's address1"
    )
    city: Optional[str] = Field(None, description="This describes the stock's city")
    state: Optional[str] = Field(None, description="This describes the stock's state")
    zip: Optional[str] = Field(None, description="This describes the stock's zip")
    country: Optional[str] = Field(
        None, description="This describes the stock's country"
    )
    phone: Optional[str] = Field(None, description="This describes the stock's phone")
    website: Optional[str] = Field(
        None, description="This describes the stock's website"
    )
    industry: Optional[str] = Field(
        None, description="This describes the stock's industry"
    )
    industryKey: Optional[str] = Field(
        None, description="This describes the stock's industryKey"
    )
    industryDisp: Optional[str] = Field(
        None, description="This describes the stock's industryDisp"
    )
    sector: Optional[str] = Field(None, description="This describes the stock's sector")
    sectorKey: Optional[str] = Field(
        None, description="This describes the stock's sectorKey"
    )
    sectorDisp: Optional[str] = Field(
        None, description="This describes the stock's sectorDisp"
    )
    longBusinessSummary: Optional[str] = Field(
        None, description="This describes the stock's longBusinessSummary"
    )
    fullTimeEmployees: Optional[str] = Field(
        None, description="This describes the stock's fullTimeEmployees"
    )
    companyOfficers: Optional[str] = Field(
        None, description="This describes the stock's companyOfficers"
    )
    auditRisk: Optional[str] = Field(
        None, description="This describes the stock's auditRisk"
    )
    boardRisk: Optional[str] = Field(
        None, description="This describes the stock's boardRisk"
    )
    compensationRisk: Optional[str] = Field(
        None, description="This describes the stock's compensationRisk"
    )
    shareHolderRightsRisk: Optional[str] = Field(
        None, description="This describes the stock's shareHolderRightsRisk"
    )
    overallRisk: Optional[str] = Field(
        None, description="This describes the stock's overallRisk"
    )
    governanceEpochDate: Optional[str] = Field(
        None, description="This describes the stock's governanceEpochDate"
    )
    compensationAsOfEpochDate: Optional[str] = Field(
        None, description="This describes the stock's compensationAsOfEpochDate"
    )
    executiveTeam: Optional[str] = Field(
        None, description="This describes the stock's executiveTeam"
    )
    maxAge: Optional[str] = Field(None, description="This describes the stock's maxAge")
    priceHint: Optional[str] = Field(
        None, description="This describes the stock's priceHint"
    )
    previousClose: Optional[str] = Field(
        None, description="This describes the stock's previousClose"
    )
    open: Optional[str] = Field(None, description="This describes the stock's open")
    dayLow: Optional[str] = Field(None, description="This describes the stock's dayLow")
    dayHigh: Optional[str] = Field(
        None, description="This describes the stock's dayHigh"
    )
    regularMarketPreviousClose: Optional[str] = Field(
        None, description="This describes the stock's regularMarketPreviousClose"
    )
    regularMarketOpen: Optional[str] = Field(
        None, description="This describes the stock's regularMarketOpen"
    )
    regularMarketDayLow: Optional[str] = Field(
        None, description="This describes the stock's regularMarketDayLow"
    )
    regularMarketDayHigh: Optional[str] = Field(
        None, description="This describes the stock's regularMarketDayHigh"
    )
    payoutRatio: Optional[str] = Field(
        None, description="This describes the stock's payoutRatio"
    )
    beta: Optional[str] = Field(None, description="This describes the stock's beta")
    trailingPE: Optional[str] = Field(
        None, description="This describes the stock's trailingPE"
    )
    forwardPE: Optional[str] = Field(
        None, description="This describes the stock's forwardPE"
    )
    volume: Optional[str] = Field(None, description="This describes the stock's volume")
    regularMarketVolume: Optional[str] = Field(
        None, description="This describes the stock's regularMarketVolume"
    )
    averageVolume: Optional[str] = Field(
        None, description="This describes the stock's averageVolume"
    )
    averageVolume10days: Optional[str] = Field(
        None, description="This describes the stock's averageVolume10days"
    )
    averageDailyVolume10Day: Optional[str] = Field(
        None, description="This describes the stock's averageDailyVolume10Day"
    )
    bid: Optional[str] = Field(None, description="This describes the stock's bid")
    ask: Optional[str] = Field(None, description="This describes the stock's ask")
    bidSize: Optional[str] = Field(
        None, description="This describes the stock's bidSize"
    )
    askSize: Optional[str] = Field(
        None, description="This describes the stock's askSize"
    )
    marketCap: Optional[str] = Field(
        None, description="This describes the stock's marketCap"
    )
    fiftyTwoWeekLow: Optional[str] = Field(
        None, description="This describes the stock's fiftyTwoWeekLow"
    )
    fiftyTwoWeekHigh: Optional[str] = Field(
        None, description="This describes the stock's fiftyTwoWeekHigh"
    )
    priceToSalesTrailing12Months: Optional[str] = Field(
        None, description="This describes the stock's priceToSalesTrailing12Months"
    )
    fiftyDayAverage: Optional[str] = Field(
        None, description="This describes the stock's fiftyDayAverage"
    )
    twoHundredDayAverage: Optional[str] = Field(
        None, description="This describes the stock's twoHundredDayAverage"
    )
    trailingAnnualDividendRate: Optional[str] = Field(
        None, description="This describes the stock's trailingAnnualDividendRate"
    )
    trailingAnnualDividendYield: Optional[str] = Field(
        None, description="This describes the stock's trailingAnnualDividendYield"
    )
    currency: Optional[str] = Field(
        None, description="This describes the stock's currency"
    )
    tradeable: Optional[str] = Field(
        None, description="This describes the stock's tradeable"
    )
    enterpriseValue: Optional[str] = Field(
        None, description="This describes the stock's enterpriseValue"
    )
    profitMargins: Optional[str] = Field(
        None, description="This describes the stock's profitMargins"
    )
    floatShares: Optional[str] = Field(
        None, description="This describes the stock's floatShares"
    )
    sharesOutstanding: Optional[str] = Field(
        None, description="This describes the stock's sharesOutstanding"
    )
    sharesShort: Optional[str] = Field(
        None, description="This describes the stock's sharesShort"
    )
    sharesShortPriorMonth: Optional[str] = Field(
        None, description="This describes the stock's sharesShortPriorMonth"
    )
    sharesShortPreviousMonthDate: Optional[str] = Field(
        None, description="This describes the stock's sharesShortPreviousMonthDate"
    )
    dateShortInterest: Optional[str] = Field(
        None, description="This describes the stock's dateShortInterest"
    )
    sharesPercentSharesOut: Optional[str] = Field(
        None, description="This describes the stock's sharesPercentSharesOut"
    )
    heldPercentInsiders: Optional[str] = Field(
        None, description="This describes the stock's heldPercentInsiders"
    )
    heldPercentInstitutions: Optional[str] = Field(
        None, description="This describes the stock's heldPercentInstitutions"
    )
    shortRatio: Optional[str] = Field(
        None, description="This describes the stock's shortRatio"
    )
    shortPercentOfFloat: Optional[str] = Field(
        None, description="This describes the stock's shortPercentOfFloat"
    )
    impliedSharesOutstanding: Optional[str] = Field(
        None, description="This describes the stock's impliedSharesOutstanding"
    )
    bookValue: Optional[str] = Field(
        None, description="This describes the stock's bookValue"
    )
    priceToBook: Optional[str] = Field(
        None, description="This describes the stock's priceToBook"
    )
    lastFiscalYearEnd: Optional[str] = Field(
        None, description="This describes the stock's lastFiscalYearEnd"
    )
    nextFiscalYearEnd: Optional[str] = Field(
        None, description="This describes the stock's nextFiscalYearEnd"
    )
    mostRecentQuarter: Optional[str] = Field(
        None, description="This describes the stock's mostRecentQuarter"
    )
    earningsQuarterlyGrowth: Optional[str] = Field(
        None, description="This describes the stock's earningsQuarterlyGrowth"
    )
    netIncomeToCommon: Optional[str] = Field(
        None, description="This describes the stock's netIncomeToCommon"
    )
    trailingEps: Optional[str] = Field(
        None, description="This describes the stock's trailingEps"
    )
    forwardEps: Optional[str] = Field(
        None, description="This describes the stock's forwardEps"
    )
    lastSplitFactor: Optional[str] = Field(
        None, description="This describes the stock's lastSplitFactor"
    )
    lastSplitDate: Optional[str] = Field(
        None, description="This describes the stock's lastSplitDate"
    )
    enterpriseToRevenue: Optional[str] = Field(
        None, description="This describes the stock's enterpriseToRevenue"
    )
    enterpriseToEbitda: Optional[str] = Field(
        None, description="This describes the stock's enterpriseToEbitda"
    )
    SandP52WeekChange: Optional[str] = Field(
        None, description="This describes the stock's SandP52WeekChange"
    )
    quoteType: Optional[str] = Field(
        None, description="This describes the stock's quoteType"
    )
    currentPrice: Optional[str] = Field(
        None, description="This describes the stock's currentPrice"
    )
    targetHighPrice: Optional[str] = Field(
        None, description="This describes the stock's targetHighPrice"
    )
    targetLowPrice: Optional[str] = Field(
        None, description="This describes the stock's targetLowPrice"
    )
    targetMeanPrice: Optional[str] = Field(
        None, description="This describes the stock's targetMeanPrice"
    )
    targetMedianPrice: Optional[str] = Field(
        None, description="This describes the stock's targetMedianPrice"
    )
    recommendationMean: Optional[str] = Field(
        None, description="This describes the stock's recommendationMean"
    )
    recommendationKey: Optional[str] = Field(
        None, description="This describes the stock's recommendationKey"
    )
    numberOfAnalystOpinions: Optional[str] = Field(
        None, description="This describes the stock's numberOfAnalystOpinions"
    )
    totalCash: Optional[str] = Field(
        None, description="This describes the stock's totalCash"
    )
    totalCashPerShare: Optional[str] = Field(
        None, description="This describes the stock's totalCashPerShare"
    )
    ebitda: Optional[str] = Field(None, description="This describes the stock's ebitda")
    totalDebt: Optional[str] = Field(
        None, description="This describes the stock's totalDebt"
    )
    quickRatio: Optional[str] = Field(
        None, description="This describes the stock's quickRatio"
    )
    currentRatio: Optional[str] = Field(
        None, description="This describes the stock's currentRatio"
    )
    totalRevenue: Optional[str] = Field(
        None, description="This describes the stock's totalRevenue"
    )
    debtToEquity: Optional[str] = Field(
        None, description="This describes the stock's debtToEquity"
    )
    revenuePerShare: Optional[str] = Field(
        None, description="This describes the stock's revenuePerShare"
    )
    returnOnAssets: Optional[str] = Field(
        None, description="This describes the stock's returnOnAssets"
    )
    returnOnEquity: Optional[str] = Field(
        None, description="This describes the stock's returnOnEquity"
    )
    grossProfits: Optional[str] = Field(
        None, description="This describes the stock's grossProfits"
    )
    freeCashflow: Optional[str] = Field(
        None, description="This describes the stock's freeCashflow"
    )
    operatingCashflow: Optional[str] = Field(
        None, description="This describes the stock's operatingCashflow"
    )
    earningsGrowth: Optional[str] = Field(
        None, description="This describes the stock's earningsGrowth"
    )
    revenueGrowth: Optional[str] = Field(
        None, description="This describes the stock's revenueGrowth"
    )
    grossMargins: Optional[str] = Field(
        None, description="This describes the stock's grossMargins"
    )
    ebitdaMargins: Optional[str] = Field(
        None, description="This describes the stock's ebitdaMargins"
    )
    operatingMargins: Optional[str] = Field(
        None, description="This describes the stock's operatingMargins"
    )
    financialCurrency: Optional[str] = Field(
        None, description="This describes the stock's financialCurrency"
    )
    symbol: Optional[str] = Field(None, description="This describes the stock's symbol")
    language: Optional[str] = Field(
        None, description="This describes the stock's language"
    )
    region: Optional[str] = Field(None, description="This describes the stock's region")
    typeDisp: Optional[str] = Field(
        None, description="This describes the stock's typeDisp"
    )
    quoteSourceName: Optional[str] = Field(
        None, description="This describes the stock's quoteSourceName"
    )
    triggerable: Optional[str] = Field(
        None, description="This describes the stock's triggerable"
    )
    customPriceAlertConfidence: Optional[str] = Field(
        None, description="This describes the stock's customPriceAlertConfidence"
    )
    shortName: Optional[str] = Field(
        None, description="This describes the stock's shortName"
    )
    longName: Optional[str] = Field(
        None, description="This describes the stock's longName"
    )
    marketState: Optional[str] = Field(
        None, description="This describes the stock's marketState"
    )
    regularMarketChangePercent: Optional[str] = Field(
        None, description="This describes the stock's regularMarketChangePercent"
    )
    regularMarketPrice: Optional[str] = Field(
        None, description="This describes the stock's regularMarketPrice"
    )
    postMarketTime: Optional[str] = Field(
        None, description="This describes the stock's postMarketTime"
    )
    regularMarketTime: Optional[str] = Field(
        None, description="This describes the stock's regularMarketTime"
    )
    exchange: Optional[str] = Field(
        None, description="This describes the stock's exchange"
    )
    messageBoardId: Optional[str] = Field(
        None, description="This describes the stock's messageBoardId"
    )
    exchangeTimezoneName: Optional[str] = Field(
        None, description="This describes the stock's exchangeTimezoneName"
    )
    exchangeTimezoneShortName: Optional[str] = Field(
        None, description="This describes the stock's exchangeTimezoneShortName"
    )
    gmtOffSetMilliseconds: Optional[str] = Field(
        None, description="This describes the stock's gmtOffSetMilliseconds"
    )
    market: Optional[str] = Field(None, description="This describes the stock's market")
    esgPopulated: Optional[str] = Field(
        None, description="This describes the stock's esgPopulated"
    )
    corporateActions: Optional[str] = Field(
        None, description="This describes the stock's corporateActions"
    )
    postMarketChangePercent: Optional[str] = Field(
        None, description="This describes the stock's postMarketChangePercent"
    )
    postMarketPrice: Optional[str] = Field(
        None, description="This describes the stock's postMarketPrice"
    )
    postMarketChange: Optional[str] = Field(
        None, description="This describes the stock's postMarketChange"
    )
    regularMarketChange: Optional[str] = Field(
        None, description="This describes the stock's regularMarketChange"
    )
    regularMarketDayRange: Optional[str] = Field(
        None, description="This describes the stock's regularMarketDayRange"
    )
    fullExchangeName: Optional[str] = Field(
        None, description="This describes the stock's fullExchangeName"
    )
    averageDailyVolume3Month: Optional[str] = Field(
        None, description="This describes the stock's averageDailyVolume3Month"
    )
    fiftyTwoWeekLowChange: Optional[str] = Field(
        None, description="This describes the stock's fiftyTwoWeekLowChange"
    )
    fiftyTwoWeekLowChangePercent: Optional[str] = Field(
        None, description="This describes the stock's fiftyTwoWeekLowChangePercent"
    )
    fiftyTwoWeekRange: Optional[str] = Field(
        None, description="This describes the stock's fiftyTwoWeekRange"
    )
    fiftyTwoWeekHighChange: Optional[str] = Field(
        None, description="This describes the stock's fiftyTwoWeekHighChange"
    )
    fiftyTwoWeekHighChangePercent: Optional[str] = Field(
        None, description="This describes the stock's fiftyTwoWeekHighChangePercent"
    )
    fiftyTwoWeekChangePercent: Optional[str] = Field(
        None, description="This describes the stock's fiftyTwoWeekChangePercent"
    )
    earningsTimestamp: Optional[str] = Field(
        None, description="This describes the stock's earningsTimestamp"
    )
    earningsTimestampStart: Optional[str] = Field(
        None, description="This describes the stock's earningsTimestampStart"
    )
    earningsTimestampEnd: Optional[str] = Field(
        None, description="This describes the stock's earningsTimestampEnd"
    )
    earningsCallTimestampStart: Optional[str] = Field(
        None, description="This describes the stock's earningsCallTimestampStart"
    )
    earningsCallTimestampEnd: Optional[str] = Field(
        None, description="This describes the stock's earningsCallTimestampEnd"
    )
    isEarningsDateEstimate: Optional[str] = Field(
        None, description="This describes the stock's isEarningsDateEstimate"
    )
    epsTrailingTwelveMonths: Optional[str] = Field(
        None, description="This describes the stock's epsTrailingTwelveMonths"
    )
    epsForward: Optional[str] = Field(
        None, description="This describes the stock's epsForward"
    )
    epsCurrentYear: Optional[str] = Field(
        None, description="This describes the stock's epsCurrentYear"
    )
    priceEpsCurrentYear: Optional[str] = Field(
        None, description="This describes the stock's priceEpsCurrentYear"
    )
    fiftyDayAverageChange: Optional[str] = Field(
        None, description="This describes the stock's fiftyDayAverageChange"
    )
    fiftyDayAverageChangePercent: Optional[str] = Field(
        None, description="This describes the stock's fiftyDayAverageChangePercent"
    )
    twoHundredDayAverageChange: Optional[str] = Field(
        None, description="This describes the stock's twoHundredDayAverageChange"
    )
    twoHundredDayAverageChangePercent: Optional[str] = Field(
        None, description="This describes the stock's twoHundredDayAverageChangePercent"
    )
    sourceInterval: Optional[str] = Field(
        None, description="This describes the stock's sourceInterval"
    )
    exchangeDataDelayedBy: Optional[str] = Field(
        None, description="This describes the stock's exchangeDataDelayedBy"
    )
    hasPrePostMarketData: Optional[str] = Field(
        None, description="This describes the stock's hasPrePostMarketData"
    )
    firstTradeDateMilliseconds: Optional[str] = Field(
        None, description="This describes the stock's firstTradeDateMilliseconds"
    )
    averageAnalystRating: Optional[str] = Field(
        None, description="This describes the stock's averageAnalystRating"
    )
    cryptoTradeable: Optional[str] = Field(
        None, description="This describes the stock's cryptoTradeable"
    )
    displayName: Optional[str] = Field(
        None, description="This describes the stock's displayName"
    )
    trailingPegRatio: Optional[str] = Field(
        None, description="This describes the stock's trailingPegRatio"
    )


class CommandParserDecisionTree(BaseModel):
    """
    A decision tree for parsing commands.
    """

    ticker: Optional[list[str]] = Field(
        description="A list of stock tickers associated with the command."
    )
    stockData: Optional[dict[str, list[str]]] = Field(
        default=None,
        description="A dictionary of relevant Yahoo Finance fields to extract, each set to true or false.",
    )
