from .okxclient import OkxClient
from .consts import *


class FundingAPI(OkxClient):

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

    # Get Currencies
    def get_currencies(self, ccy=""):
        params = {"ccy": ccy}
        return self._request_with_params(GET, CURRENCY_INFO, params)

    # Get Balance
    def get_balances(self, ccy=""):
        params = {"ccy": ccy}
        return self._request_with_params(GET, GET_BALANCES, params)

    # Get Non Tradable Assets
    def get_non_tradable_assets(self, ccy= ""):
        params = {"ccy": ccy}
        return self._request_with_params(GET, NON_TRADABLE_ASSETS, params)

    # Get Asset Valuation
    def get_asset_valuation(self, ccy=""):
        params = {"ccy": ccy}
        return self._request_with_params(GET, ASSET_VALUATION, params)

    # Funds Transfer
    def funds_transfer(
        self,
        ccy,
        amt,
        from_,
        to,
        type="0",
        subAcct="",
        loanTrans=False,
        omitPosRisk=False,
        clientId="",
    ):
        params = {
            "ccy": ccy,
            "amt": amt,
            "from": from_,
            "to": to,
            "type": type,
            "subAcct": subAcct,
            "loanTrans": loanTrans,
            "omitPosRisk": omitPosRisk,
            "clientId": clientId,
        }
        return self._request_with_params(POST, FUNDS_TRANSFER, params)

    # Get Transfer State
    def transfer_state(self, transId="", clientId="", type=""):
        params = {"transId": transId, "clientId": clientId, "type": type}
        return self._request_with_params(GET, TRANSFER_STATE, params)

    # Get Bills Info
    def get_bills(self, ccy="", type="", clientId="", after="", before="", limit=""):
        params = {
            "ccy": ccy,
            "type": type,
            "clientId": clientId,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, BILLS_INFO, params)

    # Get Deposit Address
    def get_deposit_address(self, ccy):
        params = {"ccy": ccy}
        return self._request_with_params(GET, DEPOSIT_ADDRESS, params)

    # Get Deposit History
    def get_deposit_history(
        self,
        ccy="",
        depId="",
        fromWdId="",
        txId="",
        type="",
        state="",
        after="",
        before="",
        limit="",
    ):
        params = {
            "ccy": ccy,
            "type": type,
            "state": state,
            "after": after,
            "before": before,
            "limit": limit,
            "txId": txId,
            "depId": depId,
            "fromWdId": fromWdId,
        }
        return self._request_with_params(GET, DEPOSIT_HISTORY, params)

    # Withdrawal
    def withdrawal(
        self, ccy, amt, dest, toAddr, chain="", areaCode="", rcvrInfo=None, clientId=""
    ):
        params = {
            "ccy": ccy,
            "amt": amt,
            "dest": dest,
            "toAddr": toAddr,
            "chain": chain,
            "areaCode": areaCode,
            "clientId": clientId,
        }
        if rcvrInfo:
            params["rcvrInfo"] = rcvrInfo
        return self._request_with_params(POST, WITHDRAWAL_COIN, params)

    # Cancel Withdrawal
    def cancel_withdrawal(self, wdId=""):
        params = {"wdId": wdId}
        return self._request_with_params(POST, CANCEL_WITHDRAWAL, params)

    # Get Withdrawal History
    def get_withdrawal_history(
        self,
        ccy="",
        wdId="",
        clientId="",
        txId="",
        type="",
        state="",
        after="",
        before="",
        limit="",
    ):
        params = {
            "ccy": ccy,
            "wdId": wdId,
            "clientId": clientId,
            "txId": txId,
            "type": type,
            "state": state,
            "after": after,
            "before": before,
            "limit": limit,
        }
        return self._request_with_params(GET, WITHDRAWAL_HISTORY, params)

    # Get Deposit Withdraw Status
    def get_deposit_withdraw_status(
        self, wdId="", txId="", ccy="", to="", chain=""
    ):
        params = {
            "wdId": wdId,
            "txId": txId,
            "ccy": ccy,
            "to": to,
            "chain": chain,
        }
        return self._request_with_params(
            GET, GET_DEPOSIT_WITHDRAW_STATUS, params
        )

    # Get Deposit Lightning
    def get_deposit_lightning(self, ccy, amt, to=""):
        params = {"ccy": ccy, "amt": amt}
        if to:
            params = {"to": to}
        return self._request_with_params(GET, DEPOSIT_LIGHTNING, params)

    # Withdrawal Lightning
    def withdrawal_lightning(self, ccy, invoice, memo=""):
        params = {"ccy": ccy, "invoice": invoice, "memo": memo}
        return self._request_with_params(POST, WITHDRAWAL_LIGHTNING, params)
