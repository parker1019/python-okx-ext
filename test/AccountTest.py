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
        print(self.AccountAPI.get_instruments(instType="SPOT"))

    def test_get_account_balance(self):
        print(self.AccountAPI.get_account_balance(ccy="USDT"))

    def test_get_positions(self):
        print(self.AccountAPI.get_positions(instType="SWAP"))

    def test_get_positions_history(self):
        print(self.AccountAPI.get_positions_history(instType="SWAP"))

    def test_get_position_risk(self):
        print(self.AccountAPI.get_position_risk(instType="SWAP"))

    def test_get_account_bills(self):
        print(self.AccountAPI.get_account_bills(instType="SPOT"))

    def test_get_account_bills_archive(self):
        print(
            self.AccountAPI.get_account_bills_archive(
                begin="1715780962300", end="1716998400000"
            )
        )

    def test_get_account_config(self):
        print(self.AccountAPI.get_account_config())

    def test_set_position_mode(self):
        print(self.AccountAPI.set_position_mode(posMode="long_short_mode"))

    def test_set_leverage(self):
        print(
            self.AccountAPI.set_leverage(
                lever="5", mgnMode="isolated", instId="BTC-USDT"
            )
        )

    def test_get_max_order_size(self):
        print(
            self.AccountAPI.get_max_order_size(
                instId="BTC-USDT", tdMode="cash"
            )
        )

    def test_get_max_avail_size(self):
        print(
            self.AccountAPI.get_max_avail_size(
                instId="BTC-USDT", tdMode="cash"
            )
        )

    def test_adjustment_margin(self):
        print(
            self.AccountAPI.adjustment_margin(
                instId="BTC-USDT", posSide="net", type="add", amt="1"
            )
        )

    def test_get_leverage(self):
        print(self.AccountAPI.get_leverage(mgnMode="cross", ccy="USDT"))

    def test_get_max_loan(self):
        print(self.AccountAPI.get_max_loan(mgnMode="isolated", ccy="USDT"))

    def test_get_fee_rates(self):
        print(self.AccountAPI.get_fee_rates(instType="SPOT"))

    def test_get_interest_accrued(self):
        print(self.AccountAPI.get_interest_accrued())

    def test_get_interest_rate(self):
        print(self.AccountAPI.get_interest_rate(ccy="USDT"))

    def test_set_greeks(self):
        print(self.AccountAPI.set_greeks(greeksType="BS"))

    def test_set_isolated_mode(self):
        print(
            self.AccountAPI.set_isolated_mode(
                isoMode="automatic", type="MARGIN"
            )
        )

    def test_get_max_withdrawal(self):
        print(self.AccountAPI.get_max_withdrawal(ccy="USDT"))

    def test_get_account_position_risk(self):
        print(self.AccountAPI.get_account_position_risk())

    def test_get_interest_limits(self):
        print(self.AccountAPI.get_interest_limits(ccy="USDT"))

    def test_spot_manual_borrow_repay(self):
        logger.debug(
            f'{self.AccountAPI.spot_manual_borrow_repay(ccy="USDT", side="borrow", amt=1)}'
        )

    def test_set_auto_repay(self):
        logger.info(f"{self.AccountAPI.set_auto_repay(autoRepay=True)}")

    def test_spot_borrow_repay_history(self):
        logger.debug(
            self.AccountAPI.spot_borrow_repay_history(
                ccy="USDT", type="auto_borrow", after="1597026383085"
            )
        )

    def test_position_builder(self):
        print("Both real and virtual positions and assets are calculated")
        sim_pos = [
            {"instId": "BTC-USDT-SWAP", "pos": "10"},
            {"instId": "BTC-USDT-SWAP", "pos": "10"},
        ]
        sim_asset = [{"ccy": "USDT", "amt": "100"}]
        print(
            self.AccountAPI.position_builder(
                inclRealPosAndEq=False,
                simPos=sim_pos,
                simAsset=sim_asset,
                greeksType="CASH",
            )
        )

        print("Only existing real positions are calculated")
        print(
            self.AccountAPI.position_builder(
                inclRealPosAndEq=True, greeksType="CASH"
            )
        )

        print("Only virtual positions are calculated")
        print(
            self.AccountAPI.position_builder(
                inclRealPosAndEq=False, simPos=sim_pos
            )
        )

    def test_get_greeks(self):
        print(self.AccountAPI.get_greeks(ccy="USDT"))

    def test_get_account_position_tiers(self):
        print(self.AccountAPI.get_account_position_tiers(instType="SWAP"))

    def test_activate_option(self):
        print(self.AccountAPI.activate_option())

    def test_set_auto_loan(self):
        print(self.AccountAPI.set_auto_loan(autoLoan="true"))

    def test_set_account_level(self):
        print(self.AccountAPI.set_account_level(acctLv="1"))

    def test_get_simulated_margin(self):
        print(self.AccountAPI.get_simulated_margin(instType="SWAP"))

    def test_borrow_repay(self):
        print(
            self.AccountAPI.borrow_repay(ccy="BTC", side="borrow", amt="1.0")
        )

    def test_borrow_repay_history(self):
        print(self.AccountAPI.borrow_repay_history(ccy="BTC"))

    def test_get_vip_interest_accrued_data(self):
        print(self.AccountAPI.get_vip_interest_accrued_data(ccy="BTC"))

    def test_get_vip_interest_deducted_data(self):
        print(self.AccountAPI.get_vip_interest_deducted_data(ccy="BTC"))

    def test_get_vip_loan_order_list(self):
        print(self.AccountAPI.get_vip_loan_order_list(ccy="BTC"))

    def test_get_vip_loan_order_detail(self):
        print(self.AccountAPI.get_vip_loan_order_detail(ccy="BTC", ordId="1"))


if __name__ == "__main__":
    unittest.main()
