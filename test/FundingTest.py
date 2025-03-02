import unittest
from okx import Funding


class FundingTest(unittest.TestCase):
    def setUp(self):
        api_key = "your_apiKey"
        api_secret_key = "your_secretKey"
        passphrase = "your_secretKey"
        self.FundingAPI = Funding.FundingAPI(
            api_key,
            api_secret_key,
            passphrase,
            flag="0",
        )

    # Test Get Currencies
    def test_get_currencies(self):
        print(self.FundingAPI.get_currencies("BTC"))

    # Test Get Balances
    def test_get_balances(self):
        print(self.FundingAPI.get_balances())

    # Test Get Non Tradable Assets
    def test_get_non_tradable_assets(self):
        print(self.FundingAPI.get_non_tradable_assets())

    # Test Get Asset Valuation
    def test_get_asset_valuation(self):
        print(self.FundingAPI.get_asset_valuation("USDT"))

    # Test Funds Transfer
    def test_funds_transfer(self):
        print(self.FundingAPI.funds_transfer("USDT", "100", "6", "18"))

    # Test Get Transfer State
    def test_transfer_state(self):
        print(self.FundingAPI.transfer_state("11"))

    # Test Get Bills Info
    def test_get_bills(self):
        print(self.FundingAPI.get_bills())

    # Test Get Deposit Address
    def test_get_deposit_address(self):
        print(self.FundingAPI.get_deposit_address("BTC"))

    # Test Get Deposit History
    def test_get_deposit_history(self):
        print(self.FundingAPI.get_deposit_history())

    # Test Withdrawal
    def test_withdrawal(self):
        print(
            self.FundingAPI.withdrawal(
                ccy="USDT",
                amt="1",
                dest="3",
                toAddr="18740405107",
                areaCode="86",
            )
        )

    # Test Cancel Withdrawal
    def test_cancel_withdrawal(self):
        print(self.FundingAPI.cancel_withdrawal("sdhiadhsfdjknvjdaodns"))

    # Test Get Withdrawal History
    def test_get_withdrawal_history(self):
        print(self.FundingAPI.get_withdrawal_history())

    # Test Get Deposit Withdraw Status
    def test_get_deposit_withdraw_status(self):
        print(self.FundingAPI.get_deposit_withdraw_status(wdId="84804812"))

    # Test Get Deposit Lightning
    def test_get_deposit_lightning(self):
        print(self.FundingAPI.get_deposit_lightning("BTC", "10"))

    # Test Withdrawal Lightning
    def test_withdrawal_lightning(self):
        print(self.FundingAPI.withdrawal_lightning("BTC", "jdsnjvhofhenogvne", memo="222"))



if __name__ == "__main__":
    unittest.main()
