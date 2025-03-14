import unittest
from loguru import logger
from okx import Trade


class TradeTest(unittest.TestCase):
    def setUp(self):
        api_key = "your_apiKey"
        api_secret_key = "your_secretKey"
        passphrase = "your_secretKey"
        self.tradeApi = Trade.TradeAPI(
            api_key, api_secret_key, passphrase, flag="1"
        )

    def test_place_order(self):
        with self.tradeAPI as trade:
            result = trade.place_order(
                instId="BTC-USDT",
                tdMode="cross",
                side="buy",
                ordType="limit",
                sz="0.01",
                px="18000",
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_place_multiple_orders(self):
        with self.tradeAPI as trade:
            orders = [
                {
                    "instId": "BTC-USDT",
                    "tdMode": "cross",
                    "side": "buy",
                    "ordType": "limit",
                    "sz": "0.01",
                    "px": "18000",
                },
                {
                    "instId": "ETH-USDT",
                    "tdMode": "cross",
                    "side": "buy",
                    "ordType": "limit",
                    "sz": "0.1",
                    "px": "1200",
                },
            ]
            result = trade.place_multiple_orders(orders)
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_cancel_order(self):
        with self.tradeAPI as trade:
            result = trade.cancel_order(instId="BTC-USDT", ordId="123456")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_cancel_multiple_orders(self):
        with self.tradeAPI as trade:
            orders = [
                {"instId": "BTC-USDT", "ordId": "123456"},
                {"instId": "ETH-USDT", "ordId": "123457"},
            ]
            result = trade.cancel_multiple_orders(orders)
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_amend_order(self):
        with self.tradeAPI as trade:
            result = trade.amend_order(
                instId="BTC-USDT", ordId="123456", newSz="0.02"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_amend_batch_orders(self):
        with self.tradeAPI as trade:
            orders = [
                {"instId": "BTC-USDT", "ordId": "123456", "newSz": "0.02"},
                {"instId": "ETH-USDT", "ordId": "123457", "newSz": "0.2"},
            ]
            result = trade.amend_batch_orders(orders)
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_close_positions(self):
        with self.tradeAPI as trade:
            result = trade.close_positions(
                instId="BTC-USDT-SWAP", mgnMode="cross", posSide="long"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_order(self):
        with self.tradeAPI as trade:
            result = trade.get_order(instId="BTC-USDT", ordId="123456")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_order_pending(self):
        with self.tradeAPI as trade:
            result = trade.get_order_pending(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_orders_history(self):
        with self.tradeAPI as trade:
            result = trade.get_orders_history(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_orders_history_archive(self):
        with self.tradeAPI as trade:
            result = trade.get_orders_history_archive(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_fills(self):
        with self.tradeAPI as trade:
            result = trade.get_fills(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_fills_history(self):
        with self.tradeAPI as trade:
            result = trade.get_fills_history(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_place_algo_order(self):
        with self.tradeAPI as trade:
            result = trade.place_algo_order(
                instId="BTC-USDT",
                tdMode="cross",
                side="buy",
                ordType="conditional",
                sz="0.01",
                tpTriggerPx="21000",
                tpOrdPx="20900",
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_easy_convert_currency_list(self):
        with self.tradeAPI as trade:
            result = trade.get_easy_convert_currency_list()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_easy_convert(self):
        with self.tradeAPI as trade:
            result = trade.easy_convert(
                fromCcy="BTC", toCcy="USDT", source="1"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_easy_convert_history(self):
        with self.tradeAPI as trade:
            result = trade.get_easy_convert_history()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_oneclick_repay_list(self):
        with self.tradeAPI as trade:
            result = trade.get_oneclick_repay_list()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_oneclick_repay(self):
        with self.tradeAPI as trade:
            result = trade.oneclick_repay(debtCcy=["BTC"], repayCcy="USDT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_oneclick_repay_history(self):
        with self.tradeAPI as trade:
            result = trade.oneclick_repay_history()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_mass_cancel(self):
        with self.tradeAPI as trade:
            result = trade.mass_cancel(instType="SPOT", instFamily="BTC")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_cancel_all_after(self):
        with self.tradeAPI as trade:
            result = trade.cancel_all_after(timeOut="1000", tag="test")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_account_rate_limit(self):
        with self.tradeAPI as trade:
            result = trade.get_account_rate_limit()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_order_precheck(self):
        with self.tradeAPI as trade:
            result = trade.order_precheck(
                instId="BTC-USDT",
                tdMode="cross",
                side="buy",
                ordType="limit",
                sz="0.01",
                posSide="long",
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_place_algo_order(self):
        with self.tradeAPI as trade:
            result = trade.place_algo_order(
                instId="BTC-USDT",
                tdMode="cross",
                side="buy",
                ordType="market",
                sz="0.01",
                posSide="long",
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_cancel_algo_order(self):
        with self.tradeAPI as trade:
            result = trade.cancel_algo_order(
                algoId="123456", instId="BTC-USDT"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_amend_algo_order(self):
        with self.tradeAPI as trade:
            result = trade.amend_algo_order(
                instId="BTC-USDT",
                algoId="123456",
                newSz="0.02",
                newTpTriggerPx="21000",
                newTpOrdPx="20900",
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_cancel_advance_algos(self):
        with self.tradeAPI as trade:
            result = trade.cancel_advance_algo_order(
                algoId="123456", instId="BTC-USDT"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_algo_order_details(self):
        with self.tradeAPI as trade:
            result = trade.get_algo_order_details(algoId="123456")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_algo_order_list(self):
        with self.tradeAPI as trade:
            result = trade.order_algos_list(ordType="conditional")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_algo_order_history(self):
        with self.tradeAPI as trade:
            result = trade.order_algos_history(ordType="conditional")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")


if __name__ == "__main__":
    unittest.main()
