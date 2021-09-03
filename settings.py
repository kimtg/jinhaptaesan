from os.path import join
import logging

########################################################################################################################
# Connection/Auth
########################################################################################################################

# API URL.
BASE_URL = "https://testnet.bitmex.com/api/v1/"
#BASE_URL = "https://www.bitmex.com/api/v1/" # Once you're ready, uncomment this.

# The BitMEX API requires permanent API keys. Go to https://testnet.bitmex.com/app/apiKeys to fill these out.
API_KEY = ""
API_SECRET = ""


########################################################################################################################
# Target
########################################################################################################################

# Instrument to market make on BitMEX.
SYMBOL = "XBTUSD"

########################################################################################################################
# Order Size & Spread
########################################################################################################################

# How many pairs of buy/sell orders to keep open
#ORDER_PAIRS = 6
ORDER_PAIRS = 6

# ORDER_START_SIZE will be the number of contracts submitted on level 1
# Number of contracts from level 1 to ORDER_PAIRS - 1 will follow the function
# [ORDER_START_SIZE + ORDER_STEP_SIZE (Level -1)]
#ORDER_START_SIZE = 600
#ORDER_START_SIZE = 200
ORDER_START_SIZE = 700
#ORDER_STEP_SIZE = 100
ORDER_STEP_SIZE = 0

# If True, order size is the order-to-balance ratio (ORDER_BALANCE_RATIO) is maintained.
# (example: 0.1 for 10%)
MANAGE_ORDER_SIZE = True
ORDER_BALANCE_RATIO = 0.05

# If True, randomize order size
RANDOM_ORDER_SIZE = False
MIN_ORDER_SIZE = 30
MAX_ORDER_SIZE = ORDER_START_SIZE * 4

# Distance between successive orders, as a percentage (example: 0.005 for 0.5%)
#INTERVAL = 0.005
#INTERVAL = 8002/8000 - 1
#INTERVAL = 0.01
#INTERVAL = 0.1 / 100
#INTERVAL = 0.5 / 100 ###
#INTERVAL = 0.5 / 100
INTERVAL = 0.5 / 100

# Minimum spread to maintain, in percent, between asks & bids
#MIN_SPREAD = 0.01
#MIN_SPREAD = 10040 / 10000 - 1
#MIN_SPREAD = 0.003
#MIN_SPREAD = 4013.5 / 4000 - 1 # Just outside advanced layout orderbook
#MIN_SPREAD = 4020.5 / 4000 - 1 # Just outside basic layout orderbook
#MIN_SPREAD = 0.03 # foreign exchange
#MIN_SPREAD = 4002.5 / 4000 - 1
#MIN_SPREAD = 0.0015 # taker fee * 2
#MIN_SPREAD = INTERVAL * 2
MIN_SPREAD = INTERVAL * 2
#MIN_SPREAD = 1 / 100
#MIN_SPREAD = 0.5 / 100

# If True, market-maker will place orders just inside the existing spread and work the interval % outwards,
# rather than starting in the middle and killing potentially profitable spreads.
MAINTAIN_SPREADS = True
#MAINTAIN_SPREADS = False

# This number defines far much the price of an existing order can be from a desired order before it is amended.
# This is useful for avoiding unnecessary calls and maintaining your ratelimits.
#
# Further information:
# Each order is designed to be (INTERVAL*n)% away from the spread.
# If the spread changes and the order has moved outside its bound defined as
# abs((desired_order['price'] / order['price']) - 1) > settings.RELIST_INTERVAL)
# it will be resubmitted.
#
# 0.01 == 1%
#RELIST_INTERVAL = 0.01
RELIST_INTERVAL = MIN_SPREAD

########################################################################################################################
# Trading Behavior
########################################################################################################################

# Position limits - set to True to activate. Values are in contracts.
# If you exceed a position limit, the bot will log and stop quoting that side.
# POSITION_LIMITS are calculated automatically. #####
CHECK_POSITION_LIMITS = True
#CHECK_POSITION_LIMITS = False
#MIN_POSITION = -100
#MIN_POSITION = -80000
#MAX_POSITION = 0

# POSITION_MULTIPLIER affects MIN_POSITION and MAX_POSITION (in USD Quantity)
POSITION_MULTIPLIER = 1

# If True, will only send orders that rest in the book (ExecInst: ParticipateDoNotInitiate).
# Use to guarantee a maker rebate.
# However -- orders that would have matched immediately will instead cancel, and you may end up with
# unexpected delta. Be careful.
POST_ONLY = True

########################################################################################################################
# Misc Behavior, Technicals
########################################################################################################################

# If true, don't set up any orders, just say what we would do
#DRY_RUN = True
DRY_RUN = False

# How often to re-check and replace orders.
# Generally, it's safe to make this short because we're fetching from websockets. But if too many
# order amend/replaces are done, you may hit a ratelimit. If so, email BitMEX if you feel you need a higher limit.
#LOOP_INTERVAL = 5
LOOP_INTERVAL = 5

# Wait times between orders / errors
API_REST_INTERVAL = 1
API_ERROR_INTERVAL = 10
#TIMEOUT = 7
TIMEOUT = 30

# If we're doing a dry run, use these numbers for BTC balances
#DRY_BTC = 50
DRY_BTC = 100000000 # in XBt. 1 BTC

# Available levels: logging.(DEBUG|INFO|WARN|ERROR)
LOG_LEVEL = logging.INFO

# To uniquely identify orders placed by this bot, the bot sends a ClOrdID (Client order ID) that is attached
# to each order so its source can be identified. This keeps the market maker from cancelling orders that are
# manually placed, or orders placed by another bot.
#
# If you are running multiple bots on the same symbol, give them unique ORDERID_PREFIXes - otherwise they will
# cancel each others' orders.
# Max length is 13 characters.
ORDERID_PREFIX = "mm_bitmex_"

# If any of these files (and this file) changes, reload the bot.
WATCHED_FILES = [join('market_maker', 'market_maker.py'), join('market_maker', 'bitmex.py'), 'settings.py']


########################################################################################################################
# BitMEX Portfolio
########################################################################################################################

# Specify the contracts that you hold. These will be used in portfolio calculations.
CONTRACTS = ['XBTUSD']

# Consider mark price. If true, do not trade against mark price #####
CONSIDER_MARK_PRICE=False
#CONSIDER_MARK_PRICE=True

# If true, try to minimize inventory.
MANAGE_INVENTORY=True

# If MANAGE_INVENTORY==True and the current balance is excessive,
# the buy and sell spread becomes MANAGE_INVENTORY_SKEW:1
# 1 means even.
#MANAGE_INVENTORY_SKEW=2
MANAGE_INVENTORY_SKEW=2

# Consider funding rate. If true, prefer long/short according to funding rate (positive: short) #####
CONSIDER_FUNDING=True
