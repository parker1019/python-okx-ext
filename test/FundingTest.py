import unittest
from okx import Funding


class FundingTest(unittest.TestCase):
    def setUp(self):
        api_key = "your_apiKey"
        api_secret_key = "your_secretKey"
        passphrase = "your_passphrase"
        self.FundingAPI = Funding.FundingAPI(
            api_key,
            api_secret_key,
            passphrase,
            flag="0",
        )

    # Test Get Currencies
    def test_get_currencies(self):
        with self.FundingAPI as funding:
            result = funding.get_currencies(ccy="BTC")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Balances
    def test_get_balances(self):
        with self.FundingAPI as funding:
            result = funding.get_balances()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Non Tradable Assets
    def test_get_non_tradable_assets(self):
        with self.FundingAPI as funding:
            result = funding.get_non_tradable_assets()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Asset Valuation
    def test_get_asset_valuation(self):
        with self.FundingAPI as funding:
            result = funding.get_asset_valuation(ccy="USDT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Funds Transfer
    def test_funds_transfer(self):
        with self.FundingAPI as funding:
            result = funding.funds_transfer(
                ccy="USDT", amt="100", from_="6", to="18"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Transfer State
    def test_transfer_state(self):
        with self.FundingAPI as funding:
            result = funding.transfer_state(transId="11")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Bills Info
    def test_get_bills(self):
        with self.FundingAPI as funding:
            result = funding.get_bills()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Deposit Address
    def test_get_deposit_address(self):
        with self.FundingAPI as funding:
            result = funding.get_deposit_address(ccy="BTC")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Deposit History
    def test_get_deposit_history(self):
        with self.FundingAPI as funding:
            result = funding.get_deposit_history()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Withdrawal
    def test_withdrawal(self):
        with self.FundingAPI as funding:
            result = funding.withdrawal(
                ccy="USDT",
                amt="1",
                dest="3",
                toAddr="18740405107",
                areaCode="86",
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Cancel Withdrawal
    def test_cancel_withdrawal(self):
        with self.FundingAPI as funding:
            result = funding.cancel_withdrawal(wdId="sdhiadhsfdjknvjdaodns")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Withdrawal History
    def test_get_withdrawal_history(self):
        with self.FundingAPI as funding:
            result = funding.get_withdrawal_history()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Deposit Withdraw Status
    def test_get_deposit_withdraw_status(self):
        with self.FundingAPI as funding:
            result = funding.get_deposit_withdraw_status(wdId="84804812")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Get Deposit Lightning
    def test_get_deposit_lightning(self):
        with self.FundingAPI as funding:
            result = funding.get_deposit_lightning(ccy="BTC", amt="10")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    # Test Withdrawal Lightning
    def test_withdrawal_lightning(self):
        with self.FundingAPI as funding:
            rcvrInfo = {
                "walletType": "exchange",
                "exchId": "did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
                "rcvrFirstName": "Bruce",
                "rcvrLastName": "Wayne",
                "rcvrCountry": "United States",
                "rcvrCountrySubDivision": "California",
                "rcvrTownName": "San Jose",
                "rcvrStreetName": "Clementi Avenue 1",
            }
            result = funding.withdrawal_lightning(
                ccy="BTC",
                invoice="lnbc100u1psnnvhtpp5yq2x3q5hhrzsuxpwx7ptphwzc4k4wk0j3stp0099968m44cyjg9sdqqcqzpgxqzjcsp5hz",
                rcvrInfo=rcvrInfo,
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")


if __name__ == "__main__":
    unittest.main()
