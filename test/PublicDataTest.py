import unittest
from loguru import logger
from okx import PublicData


class PublicDataTest(unittest.TestCase):
    def setUp(self):
        api_key = "your_apiKey"
        api_secret_key = "your_secretKey"
        passphrase = "your_secretKey"
        self.publicDataApi = PublicData.PublicAPI(
            api_key,
            api_secret_key,
            passphrase,
            flag="1",
        )

    def test_get_instruments(self):
        with self.publicDataApi as api:
            result = api.get_instruments(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_estimated_price(self):
        with self.publicDataApi as api:
            result = api.get_estimated_price(instId="BTCUSD-20250316")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_delivery_exercise_history(self):
        with self.publicDataApi as api:
            result = api.get_delivery_exercise_history(
                instType="FUTURES", uly="BTC-USD"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_estimated_settlement_info(self):
        with self.publicDataApi as api:
            result = api.get_estimated_settlement_info(instId="BTC-USD-SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_settlement_history(self):
        with self.publicDataApi as api:
            result = api.get_settlement_history(instFamily="BTC-USD")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_funding_rate(self):
        with self.publicDataApi as api:
            result = api.get_funding_rate(instId="BTC-USD-SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_funding_rate_history(self):
        with self.publicDataApi as api:
            result = api.funding_rate_history(instId="BTC-USD-SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_open_interest(self):
        with self.publicDataApi as api:
            result = api.get_open_interest(instType="SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_price_limit(self):
        with self.publicDataApi as api:
            result = api.get_price_limit(instId="BTC-USD-SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_opt_summary(self):
        with self.publicDataApi as api:
            result = api.get_opt_summary(uly="BTC-USD")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_discount_interest_free_quota(self):
        with self.publicDataApi as api:
            result = api.discount_interest_free_quota(ccy="ETH")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_system_time(self):
        with self.publicDataApi as api:
            result = api.get_system_time()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_mark_price(self):
        with self.publicDataApi as api:
            result = api.get_mark_price(instType="SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_position_tiers(self):
        with self.publicDataApi as api:
            result = api.get_position_tiers(
                instType="SWAP", tdMode="cross", uly="ETH-USD"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_interest_rate_loan_quota(self):
        with self.publicDataApi as api:
            result = api.get_interest_rate_loan_quota()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_underlying(self):
        with self.publicDataApi as api:
            result = api.get_underlying(instType="SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_insurance_fund(self):
        with self.publicDataApi as api:
            result = api.get_insurance_fund(instType="SWAP", uly="BTC-USD")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_convert_contract_coin(self):
        with self.publicDataApi as api:
            result = api.get_convert_contract_coin(
                instId="BTC-USD-SWAP", sz="1", px="27000"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_option_tickBands(self):
        with self.publicDataApi as api:
            result = api.get_option_tickBands(instType="OPTION")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_premium_history(self):
        with self.publicDataApi as api:
            result = api.get_premium_history(instId="BTC-USD-SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_economic_calendar(self):
        with self.publicDataApi as api:
            result = api.get_economic_calendar()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_option_trades(self):
        with self.publicDataApi as api:
            result = api.get_option_trades(instFamily="BTC-USD")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_block_trades(self):
        with self.publicDataApi as api:
            result = api.get_block_trades(instId="BTC-USD-SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_vip_interest_rate_loan_quota(self):
        with self.publicDataApi as api:
            result = api.get_vip_interest_rate_loan_quota()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")


if __name__ == "__main__":
    unittest.main()
