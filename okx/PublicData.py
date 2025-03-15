from .okxclient import OkxClient
from .consts import *


class PublicAPI(OkxClient):

    def __init__(
        self,
        api_key="-1",
        api_secret_key="-1",
        passphrase="-1",
        use_server_time=None,
        flag="1",
        domain="https://www.okx.com",
        debug=False,
        proxy=None,
    ):
        OkxClient.__init__(
            self,
            api_key,
            api_secret_key,
            passphrase,
            use_server_time,
            flag,
            domain,
            debug,
            proxy,
        )

    # Get Instruments
    def get_instruments(self, instType, uly="", instFamily="", instId=""):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
        }
        return self._request_with_params(GET, INSTRUMENT_INFO, params)

    # Get Estimated Delivery/Excercise Price
    def get_estimated_price(self, instId):
        params = {"instId": instId}
        return self._request_with_params(GET, ESTIMATED_PRICE, params)

    # Get Delivery/Exercise History
    def get_delivery_exercise_history(
        self, instType, uly="", instFamily="", after="", before="", limit=""
    ):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, DELIVERY_EXERCISE, params)

    # Get Estimated Settlement Info
    def get_estimated_settlement_info(self, instId):
        params = {"instId": instId}
        return self._request_with_params(
            GET, ESTIMATED_SETTLEMENT_INFO, params
        )

    # Get Settlement History
    def get_settlement_history(
        self, instFamily, after="", before="", limit=""
    ):
        params = {
            "instFamily": instFamily,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, SETTLEMENT_HISTORY, params)

    # Get Funding Rate
    def get_funding_rate(self, instId):
        params = {"instId": instId}
        return self._request_with_params(GET, FUNDING_RATE, params)

    # Get Funding Rate History
    def funding_rate_history(self, instId, after="", before="", limit=""):
        params = {
            "instId": instId,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, FUNDING_RATE_HISTORY, params)

    # Get Open Interest
    def get_open_interest(self, instType, uly="", instFamily="", instId=""):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
        }
        return self._request_with_params(GET, OPEN_INTEREST, params)

    # Get Limit Price
    def get_price_limit(self, instId):
        params = {"instId": instId}
        return self._request_with_params(GET, PRICE_LIMIT, params)

    # Get Option Market Data
    def get_opt_summary(self, uly="", instFamily="", expTime=""):
        params = {"uly": uly, "instFamily": instFamily, "expTime": expTime}
        return self._request_with_params(GET, OPT_SUMMARY, params)

    # Get Discount Rate And Interest-Free Quota
    def discount_interest_free_quota(self, ccy=""):
        params = {"ccy": ccy}
        return self._request_with_params(GET, DICCOUNT_INTETEST_INFO, params)

    # Get System Time
    def get_system_time(self):
        return self._request_without_params(GET, SYSTEM_TIME)

    # Get Mark Price
    def get_mark_price(self, instType, uly="", instFamily="", instId=""):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
        }
        return self._request_with_params(GET, MARK_PRICE, params)

    # Get Tier
    def get_position_tiers(
        self,
        instType,
        tdMode,
        uly="",
        instFamily="",
        instId="",
        ccy="",
        tier="",
    ):
        params = {
            "instType": instType,
            "tdMode": tdMode,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
            "ccy": ccy,
            "tier": tier,
        }
        return self._request_with_params(GET, TIER, params)

    # GET /api/v5/public/interest-rate-loan-quota
    def get_interest_rate_loan_quota(self):
        return self._request_without_params(GET, INTEREST_LOAN)

    # GET /api/v5/public/underlying
    def get_underlying(self, instType=""):
        params = {"instType": instType}
        return self._request_with_params(GET, UNDERLYING, params)

    # GET /api/v5/public/insurance-fund
    def get_insurance_fund(
        self,
        instType,
        type="",
        uly="",
        instFamily="",
        ccy="",
        before="",
        after="",
        limit="",
    ):
        params = {
            "instType": instType,
            "type": type,
            "uly": uly,
            "instFamily": instFamily,
            "ccy": ccy,
            "before": before,
            "after": after,
            "limit": limit,
        }
        return self._request_with_params(GET, INSURANCE_FUND, params)

    # GET /api/v5/public/convert-contract-coin
    def get_convert_contract_coin(
        self, type="", instId="", sz="", px="", unit="", opType=""
    ):
        params = {
            "type": type,
            "instId": instId,
            "sz": sz,
            "px": px,
            "unit": unit,
            "opType": opType,
        }
        return self._request_with_params(GET, CONVERT_CONTRACT_COIN, params)

    # Get option tickBands
    def get_option_tickBands(self, instType, instFamily=""):
        params = {"instType": instType, "instFamily": instFamily}
        return self._request_with_params(GET, GET_OPTION_TICKBANDS, params)

    # Get Premium History
    def get_premium_history(self, instId, after="", before="", limit=""):
        params = {
            "instId": instId,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, PREMIUM_HISTORY, params)

    # Get Economic Calendar
    def get_economic_calendar(
        self, region="", importance="", after="", before="", limit=""
    ):
        params = {
            "region": region,
            "importance": importance,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, ECONOMIC_CALENDAR, params)

    # Get option trades
    def get_option_trades(self, instId="", instFamily="", optType=""):
        params = {
            "instId": instId,
            "instFamily": instFamily,
            "optType": optType,
        }
        return self._request_with_params(GET, GET_OPTION_TRADES, params)

    # Get Block Trades
    def get_block_trades(self, instId):
        params = {
            "instId": instId,
        }
        return self._request_with_params(GET, PUBLIC_BLOCK_TRADES, params)

    # GET /api/v5/public/vip-interest-rate-loan-quota
    def get_vip_interest_rate_loan_quota(self):
        return self._request_without_params(GET, VIP_INTEREST_RATE_LOAN_QUOTA)
