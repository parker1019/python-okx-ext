import json

from .okxclient import OkxClient
from .consts import *


class TradeAPI(OkxClient):

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

    # Place Order
    def place_order(
        self,
        instId,
        tdMode,
        side,
        ordType,
        sz,
        ccy="",
        clOrdId="",
        tag="",
        posSide="",
        px="",
        pxUsd="",
        pxVol="",
        reduceOnly=False,
        tgtCcy="",
        banAmend=False,
        quickMgnType="",
        stpId="",
        stpMode="",
        attachAlgoOrds=None,
    ):
        params = {
            "instId": instId,
            "tdMode": tdMode,
            "side": side,
            "ordType": ordType,
            "sz": sz,
            "ccy": ccy,
            "clOrdId": clOrdId,
            "tag": tag,
            "posSide": posSide,
            "px": px,
            "pxUsd": pxUsd,
            "pxVol": pxVol,
            "reduceOnly": reduceOnly,
            "tgtCcy": tgtCcy,
            "banAmend": banAmend,
            "quickMgnType": quickMgnType,
            "stpId": stpId,
            "stpMode": stpMode,
        }
        if attachAlgoOrds:
            params["attachAlgoOrds"] = attachAlgoOrds
        return self._request_with_params(POST, PLACR_ORDER, params)

    # Batch Orders
    def place_multiple_orders(self, orders_data):
        return self._request_with_params(POST, BATCH_ORDERS, orders_data)

    # Cancel Order
    def cancel_order(self, instId, ordId="", clOrdId=""):
        params = {"instId": instId, "ordId": ordId, "clOrdId": clOrdId}
        return self._request_with_params(POST, CANCEL_ORDER, params)

    # Cancel Batch Orders
    def cancel_multiple_orders(self, orders_data):
        return self._request_with_params(
            POST, CANCEL_BATCH_ORDERS, orders_data
        )

    # Amend Order
    def amend_order(
        self,
        instId,
        ordId="",
        clOrdId="",
        cxlOnFail=False,
        reqId="",
        newSz="",
        newPx="",
        newPxUsd="",
        newPxVol="",
        attachAlgoOrds=None,
    ):
        params = {
            "instId": instId,
            "cxlOnFail": cxlOnFail,
            "ordId": ordId,
            "clOrdId": clOrdId,
            "reqId": reqId,
            "newSz": newSz,
            "newPx": newPx,
            "newPxUsd": newPxUsd,
            "newPxVol": newPxVol,
        }
        if attachAlgoOrds:
            params["attachAlgoOrds"] = attachAlgoOrds
        return self._request_with_params(POST, AMEND_ORDER, params)

    # Amend Batch Orders
    def amend_batch_orders(self, orders_data):
        return self._request_with_params(POST, AMEND_BATCH_ORDER, orders_data)

    # Close Position
    def close_positions(
        self,
        instId,
        mgnMode,
        posSide="",
        ccy="",
        autoCxl=False,
        clOrdId="",
        tag="",
    ):
        params = {
            "instId": instId,
            "mgnMode": mgnMode,
            "posSide": posSide,
            "ccy": ccy,
            "autoCxl": autoCxl,
            "clOrdId": clOrdId,
            "tag": tag,
        }
        return self._request_with_params(POST, CLOSE_POSITION, params)

    # Order Info
    def get_order(self, instId, ordId="", clOrdId=""):
        params = {"instId": instId, "ordId": ordId, "clOrdId": clOrdId}
        return self._request_with_params(GET, ORDER_INFO, params)

    # Order Pending
    def get_order_pending(
        self,
        instType="",
        uly="",
        instFamily="",
        instId="",
        ordType="",
        state="",
        after="",
        before="",
        limit="",
    ):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
            "ordType": ordType,
            "state": state,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, ORDERS_PENDING, params)

    # Order History
    def get_orders_history(
        self,
        instType,
        uly="",
        instFamily="",
        instId="",
        ordType="",
        state="",
        category="",
        after="",
        before="",
        begin="",
        end="",
        limit="",
    ):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
            "ordType": ordType,
            "state": state,
            "category": category,
            "after": after,
            "before": before,
            "begin": begin,
            "end": end,
            "limit": limit,
        }
        return self._request_with_params(GET, ORDERS_HISTORY, params)

    # Order History Archive
    def get_orders_history_archive(
        self,
        instType,
        uly="",
        instFamily="",
        instId="",
        ordType="",
        state="",
        category="",
        after="",
        before="",
        begin="",
        end="",
        limit="",
    ):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
            "ordType": ordType,
            "state": state,
            "category": category,
            "after": after,
            "before": before,
            "begin": begin,
            "end": end,
            "limit": limit,
        }
        return self._request_with_params(GET, ORDERS_HISTORY_ARCHIVE, params)

    # Order Fills
    def get_fills(
        self,
        instType="",
        uly="",
        instFamily="",
        instId="",
        ordId="",
        subType="",
        after="",
        before="",
        begin="",
        end="",
        limit="",
    ):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
            "ordId": ordId,
            "subType": subType,
            "after": after,
            "before": before,
            "begin": begin,
            "end": end,
            "limit": limit,
        }
        return self._request_with_params(GET, ORDER_FILLS, params)

    # Order Fills History
    def get_fills_history(
        self,
        instType,
        uly="",
        instFamily="",
        instId="",
        ordId="",
        subType="",
        after="",
        before="",
        begin="",
        end="",
        limit="",
    ):
        params = {
            "instType": instType,
            "uly": uly,
            "instFamily": instFamily,
            "instId": instId,
            "ordId": ordId,
            "subType": subType,
            "after": after,
            "before": before,
            "begin": begin,
            "end": end,
            "limit": limit,
        }
        return self._request_with_params(GET, ORDERS_FILLS_HISTORY, params)

    # Easy Convert Currency List
    def get_easy_convert_currency_list(self, source="1"):
        params = {"source": source}
        return self._request_with_params(
            GET, EASY_CONVERT_CURRENCY_LIST, params
        )

    # Easy Convert
    def easy_convert(self, fromCcy=[], toCcy="", source="1"):
        params = {"fromCcy": fromCcy, "toCcy": toCcy, "source": source}
        return self._request_with_params(POST, EASY_CONVERT, params)

    # Easy Convert History
    def get_easy_convert_history(self, after="", before="", limit=""):
        params = {"after": after, "before": before, "limit": limit}
        return self._request_with_params(GET, CONVERT_EASY_HISTORY, params)

    # One Click Repay Support
    def get_oneclick_repay_list(self, debtType=""):
        params = {"debtType": debtType}
        return self._request_with_params(GET, ONE_CLICK_REPAY_SUPPORT, params)

    # One Click Repay
    def oneclick_repay(self, debtCcy=[], repayCcy=""):
        params = {"debtCcy": debtCcy, "repayCcy": repayCcy}
        return self._request_with_params(POST, ONE_CLICK_REPAY, params)

    # One Click Repay History
    def oneclick_repay_history(self, after="", before="", limit=""):
        params = {"after": after, "before": before, "limit": limit}
        return self._request_with_params(GET, ONE_CLICK_REPAY_HISTORY, params)

    # Mass Cancel
    def mass_cancel(self, instType, instFamily, lockInterval="0"):
        params = {
            "instType": instType,
            "instFamily": instFamily,
            "lockInterval": lockInterval,
        }
        return self._request_with_params(POST, MASS_CANCEL, params)

    # Cancel All After
    def cancel_all_after(self, timeOut, tag=""):
        params = {"timeOut": timeOut, "tag": tag}
        return self._request_with_params(POST, CANCEL_ALL_AFTER, params)

    # Account Rate Limit
    def get_account_rate_limit(self):
        return self._request_without_params(GET, ACCOUNT_RATE_LIMIT)

    # Order Precheck
    def order_precheck(
        self,
        instId,
        tdMode,
        side,
        ordType,
        sz,
        posSide="",
        px="",
        reduceOnly=False,
        tgtCcy="",
        attachAlgoOrds=None,
    ):
        params = {
            "instId": instId,
            "tdMode": tdMode,
            "side": side,
            "ordType": ordType,
            "sz": sz,
            "posSide": posSide,
            "px": px,
            "reduceOnly": reduceOnly,
            "tgtCcy": tgtCcy,
        }
        if attachAlgoOrds:
            params["attachAlgoOrds"] = attachAlgoOrds
        return self._request_with_params(POST, ORDER_PRECHECK, params)

    # Place Algo Order
    def place_algo_order(
        self,
        instId,
        tdMode,
        side,
        ordType,
        sz="",
        ccy="",
        posSide="",
        tgtCcy="",
        algoClOrdId="",
        closeFraction="",
        tag="",
        tpTriggerPx="",
        tpTriggerPxType="",
        tpOrdPx="",
        tpOrdKind="",
        slTriggerPx="",
        slTriggerPxType="",
        slOrdPx="",
        cxlOnClosePos=False,
        reduceOnly=False,
        chaseType="",
        chaseVal="",
        maxChaseType="",
        maxChaseVal="",
        triggerPx="",
        orderPx="",
        triggerPxType="",
        callbackRatio="",
        callbackSpread="",
        activePx="",
        pxVar="",
        pxSpread="",
        szLimit="",
        pxLimit="",
        timeInterval="",
        quickMgnType="",
        attachAlgoOrds=None,
    ):
        params = {
            "instId": instId,
            "tdMode": tdMode,
            "side": side,
            "ordType": ordType,
            "sz": sz,
            "ccy": ccy,
            "posSide": posSide,
            "tgtCcy": tgtCcy,
            "algoClOrdId": algoClOrdId,
            "closeFraction": closeFraction,
            "tag": tag,
            "tpTriggerPx": tpTriggerPx,
            "tpTriggerPxType": tpTriggerPxType,
            "tpOrdPx": tpOrdPx,
            "tpOrdKind": tpOrdKind,
            "slTriggerPx": slTriggerPx,
            "slTriggerPxType": slTriggerPxType,
            "slOrdPx": slOrdPx,
            "cxlOnClosePos": cxlOnClosePos,
            "reduceOnly": reduceOnly,
            "chaseType": chaseType,
            "chaseVal": chaseVal,
            "maxChaseType": maxChaseType,
            "maxChaseVal": maxChaseVal,
            "triggerPx": triggerPx,
            "orderPx": orderPx,
            "triggerPxType": triggerPxType,
            "callbackRatio": callbackRatio,
            "callbackSpread": callbackSpread,
            "activePx": activePx,
            "pxVar": pxVar,
            "pxSpread": pxSpread,
            "szLimit": szLimit,
            "pxLimit": pxLimit,
            "timeInterval": timeInterval,
            "quickMgnType": quickMgnType,
        }
        if attachAlgoOrds:
            params["attachAlgoOrds"] = attachAlgoOrds
        return self._request_with_params(POST, PLACE_ALGO_ORDER, params)

    # Cancel Algo Order
    def cancel_algo_order(self, algoId, instId):
        params = {"algoId": algoId, "instId": instId}
        return self._request_with_params(POST, CANCEL_ALGOS, params)

    # Amend Algo Order
    def amend_algo_order(
        self,
        instId="",
        algoId="",
        algoClOrdId="",
        cxlOnFail=False,
        reqId="",
        newSz="",
        newTpTriggerPx="",
        newTpOrdPx="",
        newSlTriggerPx="",
        newSlOrdPx="",
        newTpTriggerPxType="",
        newSlTriggerPxType="",
        newTriggerPx="",
        newOrderPx="",
        newTriggerPxType="",
        attachAlgoOrds=None,
    ):
        params = {
            "instId": instId,
            "algoId": algoId,
            "algoClOrdId": algoClOrdId,
            "cxlOnFail": cxlOnFail,
            "reqId": reqId,
            "newSz": newSz,
            "newTpTriggerPx": newTpTriggerPx,
            "newTpOrdPx": newTpOrdPx,
            "newSlTriggerPx": newSlTriggerPx,
            "newSlOrdPx": newSlOrdPx,
            "newTpTriggerPxType": newTpTriggerPxType,
            "newSlTriggerPxType": newSlTriggerPxType,
            "newTriggerPx": newTriggerPx,
            "newOrderPx": newOrderPx,
            "newTriggerPxType": newTriggerPxType,
        }
        if attachAlgoOrds:
            params["attachAlgoOrds"] = attachAlgoOrds
        return self._request_with_params(POST, AMEND_ALGO_ORDER, params)

    # Cancel Advance Algo Order
    def cancel_advance_algo_order(self, algoId, instId):
        params = {"algoId": algoId, "instId": instId}
        return self._request_with_params(POST, CANCEL_ADVANCE_ALGOS, params)

    # Get Algo Order Details
    def get_algo_order_details(self, algoId="", algoClOrdId=""):
        params = {"algoId": algoId, "algoClOrdId": algoClOrdId}
        return self._request_with_params(GET, GET_ALGO_ORDER_DETAILS, params)

    # Order Algo List
    def order_algos_list(
        self,
        algoId="",
        instType="",
        instId="",
        ordType="",
        after="",
        before="",
        limit="",
        algoClOrdId="",
    ):
        params = {
            "algoId": algoId,
            "instType": instType,
            "instId": instId,
            "ordType": ordType,
            "after": after,
            "before": before,
            "limit": limit,
            "algoClOrdId": algoClOrdId,
        }
        return self._request_with_params(GET, ORDERS_ALGO_PENDING, params)

    # Order Algo History
    def order_algos_history(
        self,
        ordType,
        state="",
        algoId="",
        instType="",
        instId="",
        after="",
        before="",
        limit="",
    ):
        params = {
            "ordType": ordType,
            "state": state,
            "algoId": algoId,
            "instType": instType,
            "instId": instId,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, ORDERS_ALGO_HISTORY, params)
