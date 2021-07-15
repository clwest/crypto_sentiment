#sentiment_reddit_template.py
# use this template to generate the reddit sentiment config file which is used in the sentiment process
crypto = { 'BTC','ETH','USDT','BNB','ADA','DOGE','XRP','USDC','DOT','BUSD','BCH','UNI','SOL','LTC','LINK','MATIC','THETA','WBTC','XLM','ICP','ETC','VET','DAI','TRX','FIL','SHIB','XMR','EOS','CUSDC','BSV','AAVE','AMP','ATOM','CDAI','OKB','CRO','ALGO','CAKE','KLAY','CEL','CETH','NEO','TFUEL','LUNA','MIOTA','LEO','XTZ','FTT','MKR','AVAX','UST','KSM','SAFEMOON','HT','RUNE','DCR','BTT','GRT','HBAR','COMP','SUSHI','WAVES','TUSD','HBTC','DASH','CHZ','TEL','EGLD','ZEC','STETH','YFI','QNT','SNX','HOT','HNT','XEM','ZIL','ENJ','PAX','XDC','BAT','NEAR','MDX','NEXO','BTG','LUSD','STX','ZEN','BNT','MANA','ONE','QTUM','NANO','DGB','HUSD','CUSDT','SC','ZRX','FTM','KCS','BCHA','XSUSHI','CRV','ONT','ARRR','NXM','OMG','GT','UMA','WRX','ANKR','VGX','CHSB','RVN','ICX','LPT','TITAN','AR','IOST','CELO','1INCH','FLOW','OMI','HBC','UOS','USDN','BCD','XVG','RENBTC','FEI','TON','LRC','CKB','WOO','FEG','MIR','REN','RSR','BAKE','LSK','WIN','MAID','OXY','PAXG','XCH','NPXS','XPRT','ASD','TRIBE','GLM','KAVA','AKT','EWT','SETH','MINA','ALUSD','CUNI','ERG','VTHO','GNO','PUNDIX','SKL','DENT','CFX','AXS','KLV','GUSD','PERP','RLC','REEF','IOTX','BAL','IQ','XVS','PROM','ANC','SNT','AGIX','BAND','OCEAN','CTSI','AUDIO','INJ','RAY','KOBE','LOC','KIRO','ZKS','UQC','FUN','DAG','USDP','SXP','NMR','NMX','ORN','AMPL','WAXP','CELR','SEUR','TON','ALCX','FRAX','SRM','10SET','STMX','META','XAUT','UBT','OGN','OXT','OHM','HXRO','SUSD','MATH','FORTH','NKN','SAND','FET','SAPP','EVN','RPL','BTCST','KNC','CVC','STRAX','EXRD','NU','KNCL','HYDRA','POLY','ORBS','MED','KEEP','ZMT','STETH','LEND','ANT','ALPHA','TOMO','ARDR','ARK','PHA','DODO','BTS','AVA','WNXM','MONA','RUNE','COL','TWT','SUN','RIF','ETN','CREAM','STEEM','CSPR','DPI','EURS','GTC','VLX','NWC','BTM','TKO','PAC','HIVE','DNT','UTK','SVS','DERO','COTI','STORJ','MLN','AETH','TLM','BOND','WAN','DIVI','MTL','TRAC','EPS','ATA','C20','KAI','ROOK','RLY','SURE','CZRX','LON','SUPER','REP','ROSE','DATA','WOOP','QKC','FIDA','CVXCRV','TRYB','VRA','VAI','LYXE','POLS','IRIS','SNM','XCM','NOIA','GNY','FX','DAO','BIFI','BTSE','RFOX','HNS','ELG','SFP','BADGER','SCRT','YFII','ELF','VAL','GAS','QUICK','ERN','BCN','VXV','ZAI','SLP','DVPN','CORE','KMD','XOR','CBAT','RNDR','ECO','TRB','ALICE','SERO','JST','AUCTION','PRQ','PEAK','SYS','ALBT','NRG','BANANA','HTR','CHR','WOZX','KIN','MXC','WPP','DDX','POWR','VRSC','CARDS','AION','API3','RDD','GALA','MFT','FIRO','NFT','LINA','MASK','ATRI','CUMMIES','PVM','YCC','DIA','XHV','MIST','PNK','USDX','HOGE','ZNN','ERSDL','BOR','OXEN','BSCPAD','DVPN','SETH2','STAKE','SBTC','NSBT','LGO','MX','FIO','INSUR','CUSD','KDA','HARD','CRE','SHR','LIT','TRU','SWAP','FXS','XHDX','EMC2','LTO','POND','SLINK','PPT','GET','CXO','CRU','ELA','LDO','BURST','RAMP','AKRO','WEX','XBASE','XYO','BOA','DOCK','CRETH2','KRT','BELT','RGT','RARI','WHALE','VSYS','TT','DUSK','STPT','NULS','CTK','BAR','REQ','VERI','ADX','HEGIC','BLZ','HEZ','AE','SBD','ALPACA','GRS','IOC','LOOMOLD','PNG','PLTC','DRGN','NIM','HAI','DF','SAI','BEAM','ETH2X-FLI','INDEX','TORN','WICC','BTU','VEE','SX','OCC','MUSD','DGD','MAPS','CBK','PCX','ILV','NBR','TLOS','BEL','VTC','PAID','MQQQ','COS','YLD','SKEY','NXS','PIVX','OM','APL','HTB','VSP','MET','EAC','GZIL','DSLA','MAAPL','GHST','ELON','CQT','BMX','MSLV','PBTC','USDK','MAMZN','MGOOGL','MBABA','GXC','MTSLA','RFR','WAULT','MUSO','LQTY','DG', }

# Exclude common words used on crypto reddit that are also crypto names
blacklist = {'I', 'WSB', 'THE', 'A', 'ROPE', 'YOLO', 'TOS', 'CEO', 'DD', 'IT', 'OPEN', 'ATH', 'PM', 'IRS', 'FOR','DEC', 'BE', 'IMO', 'ALL', 'RH', 'EV', 'TOS', 'CFO', 'CTO', 'DD', 'BTFD', 'WSB', 'OK', 'PDT', 'RH', 'KYS', 'FD', 'TYS', 'US', 'USA', 'IT', 'ATH', 'RIP', 'BMW', 'GDP', 'OTM', 'ATM', 'ITM', 'IMO', 'LOL', 'AM', 'BE', 'PR', 'PRAY', 'PT', 'FBI', 'SEC', 'GOD', 'NOT', 'POS', 'FOMO', 'TL;DR', 'EDIT', 'STILL', 'WTF', 'RAW', 'PM', 'LMAO', 'LMFAO', 'ROFL', 'EZ', 'RED', 'BEZOS', 'TICK', 'IS', 'PM', 'LPT', 'GOAT', 'FL', 'CA', 'IL', 'MACD', 'HQ', 'OP', 'PS', 'AH', 'TL', 'JAN', 'FEB', 'JUL', 'AUG', 'SEP', 'SEPT', 'OCT', 'NOV', 'FDA', 'IV', 'ER', 'IPO', 'MILF', 'BUT', 'SSN', 'FIFA', 'USD', 'CPU', 'AT', 'GG', 'Mar'}


# adding crypto reddit to vader to improve sentiment analysis, score: 4.0 to -4.0. Rank each keyword
# add new key words below that you would like to rank

new_words = {
    'lambo': 4.0,
    'rekt': -4.0,
    'citron': -4.0,
    'hidenburg': -4.0,
    'moon': 4.0,
    'Elon': 2.0,
    'hodl': 2.0,
    'highs': 2.0,
    'mooning': 4.0,
    'long': 2.0,
    'short': -2.0,
    'call': 4.0,
    'calls': 4.0,
    'put': -4.0,
    'puts': -4.0,
    'break': 2.0,
    'tendie': 2.0,
    'tendies': 2.0,
    'town': 2.0,
    'overvalued': -3.0,
    'undervalued': 3.0,
    'buy': 4.0,
    'sell': -4.0,
    'gone': -1.0,
    'gtfo': -1.7,
    'fomo': 2.0,
    'paper': -1.7,
    'bullish': 3.7,
    'bearish': -3.7,
    'bagholder': -1.7,
    'stonk': 1.9,
    'green': 1.9,
    'money': 1.2,
    'print': 2.2,
    'rocket': 2.2,
    'bull': 2.9,
    'bear': -2.9,
    'pumping': 1.0,
    'sus': -3.0,
    'offering': -2.3,
    'rip': -4.0,
    'downgrade': -3.0,
    'upgrade': 3.0,
    'maintain': 1.0,
    'pump': 1.9,
    'hot': 2,
    'drop': -2.5,
    'rebound': 1.5,
    'crack': 2.5, }