import unittest
from loguru import logger
from okx import Account


class AccountTest(unittest.TestCase):
    def setUp(self):
        api_key = "52049394-3c72-4c06-8d87-d6399450c264"
        api_secret_key = "E532EB5AF81E6E50A2875225FEDC9150"
        passphrase = "Fixedloan2024!"
        self.AccountAPI = Account.AccountAPI(
            api_key, api_secret_key, passphrase, flag="1"
        )

    def test_get_instruments(self):
        with self.AccountAPI as account:
            result = account.get_instruments(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_account_balance(self):
        with self.AccountAPI as account:
            result = account.get_account_balance(ccy="USDT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_positions(self):
        with self.AccountAPI as account:
            result = account.get_positions(instType="SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_positions_history(self):
        with self.AccountAPI as account:
            result = account.get_positions_history(instType="SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_position_risk(self):
        with self.AccountAPI as account:
            result = account.get_position_risk(instType="SWAP")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_account_bills(self):
        with self.AccountAPI as account:
            result = account.get_account_bills(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_account_bills_archive(self):
        with self.AccountAPI as account:
            result = account.get_account_bills_archive(
                begin="1715780962300", end="1716998400000"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_account_config(self):
        with self.AccountAPI as account:
            result = account.get_account_config()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_set_position_mode(self):
        with self.AccountAPI as account:
            result = account.set_position_mode(posMode="net_mode")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_set_leverage(self):
        with self.AccountAPI as account:
            result = account.set_leverage(
                lever="5", mgnMode="isolated", instId="BTC-USDT"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_max_order_size(self):
        with self.AccountAPI as account:
            result = account.get_max_order_size(
                instId="BTC-USDT", tdMode="cash"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_max_avail_size(self):
        with self.AccountAPI as account:
            result = account.get_max_avail_size(
                instId="BTC-USDT", tdMode="cash"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_adjustment_margin(self):
        with self.AccountAPI as account:
            result = account.adjustment_margin(
                instId="BTC-USDT-SWAP", posSide="net", type="add", amt="1"
            )
            status_code = result.get("code")
            self.assertEqual(
                status_code, "59300"
            )  # 59300: The position is not found

    def test_get_leverage(self):
        with self.AccountAPI as account:
            result = account.get_leverage(mgnMode="cross", ccy="USDT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_max_loan(self):
        with self.AccountAPI as account:
            result = account.get_max_loan(
                mgnMode="cross", instId="BTC-USDT", ccy="BTC", mgnCcy="USDT"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_fee_rates(self):
        with self.AccountAPI as account:
            result = account.get_fee_rates(instType="SPOT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_interest_accrued(self):
        with self.AccountAPI as account:
            result = account.get_interest_accrued()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_interest_rate(self):
        with self.AccountAPI as account:
            result = account.get_interest_rate(ccy="USDT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_set_greeks(self):
        with self.AccountAPI as account:
            result = account.set_greeks(greeksType="BS")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_set_isolated_mode(self):
        with self.AccountAPI as account:
            result = account.set_isolated_mode(
                isoMode="automatic", type="MARGIN"
            )
            status_code = result.get("code")
            self.assertEqual(
                status_code, "51010"
            )  # 51010: The account mode does not support this operation

    def test_get_max_withdrawal(self):
        with self.AccountAPI as account:
            result = account.get_max_withdrawal(ccy="USDT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_account_position_risk(self):
        with self.AccountAPI as account:
            result = account.get_account_position_risk()
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_interest_limits(self):
        with self.AccountAPI as account:
            result = account.get_interest_limits(ccy="USDT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_spot_manual_borrow_repay(self):
        with self.AccountAPI as account:
            result = account.spot_manual_borrow_repay(
                ccy="USDT", side="borrow", amt=1
            )
            status_code = result.get("code")
            self.assertEqual(
                status_code, "59410"
            )  # 59410: The account does not support loan

    def test_set_auto_repay(self):
        with self.AccountAPI as account:
            result = account.set_auto_repay(autoRepay=True)
            status_code = result.get("code")
            self.assertEqual(
                status_code, "51010"
            )  # 51010: The account mode does not support this operation

    def test_spot_borrow_repay_history(self):
        with self.AccountAPI as account:
            result = account.spot_borrow_repay_history(
                ccy="USDT", type="auto_borrow", after="1597026383085"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_position_builder(self):
        with self.AccountAPI as account:
            sim_pos = [
                {"instId": "BTC-USDT-SWAP", "pos": "10", "avgPx": "100000"},
                {"instId": "ETH-USDT-SWAP", "pos": "10", "avgPx": "3000"},
            ]
            sim_asset = [{"ccy": "USDT", "amt": "1000000"}]

            result = account.position_builder(
                inclRealPosAndEq=False,
                simPos=sim_pos,
                simAsset=sim_asset,
                greeksType="CASH",
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_greeks(self):
        with self.AccountAPI as account:
            result = account.get_greeks(ccy="USDT")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_account_position_tiers(self):
        with self.AccountAPI as account:
            result = account.get_account_position_tiers(
                instType="SWAP", instFamily="BTC-USDT"
            )
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_activate_option(self):
        with self.AccountAPI as account:
            result = account.activate_option()
            status_code = result.get("code")
            self.assertEqual(
                status_code, "50050"
            )  # 50050: The account has already been activated

    def test_set_auto_loan(self):
        with self.AccountAPI as account:
            result = account.set_auto_loan(autoLoan="true")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_set_account_level(self):
        with self.AccountAPI as account:
            result = account.set_account_level(acctLv="2")
            status_code = result.get("code")
            self.assertEqual(
                status_code, "59001"
            )  # 59001: The account have loan

    def test_get_simulated_margin(self):
        with self.AccountAPI as account:
            result = account.get_simulated_margin(instType="SWAP")
            status_code = result.get("code")
            self.assertEqual(
                status_code, 404
            )  # 404: The interface is under maintenance

    def test_borrow_repay(self):
        with self.AccountAPI as account:
            result = account.borrow_repay(ccy="BTC", side="borrow", amt="1.0")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_borrow_repay_history(self):
        with self.AccountAPI as account:
            result = account.borrow_repay_history(ccy="BTC")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_vip_interest_accrued_data(self):
        with self.AccountAPI as account:
            result = account.get_vip_interest_accrued_data(ccy="BTC")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_vip_interest_deducted_data(self):
        with self.AccountAPI as account:
            result = account.get_vip_interest_deducted_data(ccy="BTC")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_vip_loan_order_list(self):
        with self.AccountAPI as account:
            result = account.get_vip_loan_order_list(ccy="BTC")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")

    def test_get_vip_loan_order_detail(self):
        with self.AccountAPI as account:
            result = account.get_vip_loan_order_detail(ccy="BTC", ordId="1")
            status_code = result.get("code")
            self.assertEqual(status_code, "0")


if __name__ == "__main__":
    unittest.main()
