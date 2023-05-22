from stock_calculator.calculator_base import CalculatorBase
from stock_calculator.stock_transactions import StockTransactionsDataFrame


class StockCalculatorSimple(CalculatorBase):

    def get_average_price(self, previous_average_price=0, previous_average_amount=0) -> float:
        price = self.df_stock.get_price()
        amount = self.df_stock.get_amount()
        brokerage_fee = self.df_stock.get_fee()
        is_purchase_operation = self.df_stock.is_purchase_operations()

        average_price = previous_average_price
        average_amount = previous_average_amount
        for i in range(0, len(price)):
            if is_purchase_operation.iloc[i]:
                average_price = self._calc_average_price(
                    price=price.iloc[i],
                    amount=amount.iloc[i],
                    brokerage_fee=brokerage_fee.iloc[i],
                    average_price=average_price,
                    average_amount=average_amount
                )
                average_amount = self._calc_average_purchase_amount(
                    amount=amount.iloc[i],
                    average_amount=average_amount
                )
            else:
                average_amount = self._calc_average_sales_amount(
                    amount=amount.iloc[i],
                    average_amount=average_amount
                )

            print(f"average_price {average_price} average_amount {average_amount}")

        print()
        return average_price

    @staticmethod
    def _calc_average_price(
            price: float,
            amount: int,
            brokerage_fee: float,
            average_price: float = 0,
            average_amount: int = 0
    ) -> float:
        """
        :param price: Stock purchase price (PC)
        :param amount: Stock amount (QC)
        :param brokerage_fee: Stock brokerage fee (TC)
        :param average_price: Stock average price, initially zero (PM)
        :param average_amount: Stock average amount, initially zero (QM)
        :return: New calculated average price (PM)
        """
        previous_average_amount = average_amount
        average_amount = StockCalculatorSimple._calc_average_purchase_amount(
            amount=amount,
            average_amount=average_amount
        )
        x = price * amount + brokerage_fee
        average_price = (average_price * previous_average_amount + x) / average_amount
        return average_price

    def get_average_amount(self) -> int:
        amount = self.df_stock.get_amount()
        is_purchase_operation = self.df_stock.is_purchase_operations()
        average_amount = 0
        for i in range(0, len(amount)):
            if is_purchase_operation.iloc[i]:
                average_amount = self._calc_average_purchase_amount(amount=amount.iloc[i], average_amount=average_amount)
            else:
                average_amount = self._calc_average_sales_amount(amount=amount.iloc[i], average_amount=average_amount)
        return average_amount

    @staticmethod
    def _calc_average_purchase_amount(amount: int, average_amount: int = 0) -> int:
        """
        :param amount: Stock amount (QC)
        :param average_amount: Stock average amount, initially zero (QM)
        :return: New calculated average amount (QM)
        """
        average_amount = average_amount + amount
        return average_amount
    @staticmethod
    def _calc_average_sales_amount(amount: int, average_amount: int = 0) -> int:
        """
        :param amount: Stock amount (QC)
        :param average_amount: Stock average amount, initially zero (QM)
        :return: New calculated average amount (QM)
        """
        average_amount = average_amount - amount
        return average_amount

    def get_measured_result(self, average_price: float = None) -> float:
        average_price = average_price or self.get_average_price()
        measured_result_list = []
        df_stock = self.df_stock.filter_sales_operations()
        price = df_stock.get_price()
        amount = df_stock.get_amount()
        fee = df_stock.get_fee()
        for i in range(0, len(price)):
            measured_result = self._calc_measured_result(
                price=price.iloc[i],
                average_price=average_price,
                amount=amount.iloc[i],
                fee=fee.iloc[i]
            )
            measured_result_list.append(measured_result)
        measured_result_monthly = sum(measured_result_list)
        return measured_result_monthly

    @staticmethod
    def _calc_measured_result(
            price: float,
            average_price: float,
            amount: int,
            fee: float
    ) -> float:
        measured_result = (price - average_price) * amount - fee
        return measured_result

    def get_measured_loss(self):
        measured_result = self.get_measured_result()
        return self._calc_measured_loss(measured_result=measured_result)

    @staticmethod
    def _calc_measured_loss(
            measured_result: float,
            measured_loss: float = 0
    ) -> float:
        if measured_result < 0:
            measured_loss = measured_loss + measured_result
        else:
            measured_loss = measured_loss - min(measured_result, measured_loss)
        return measured_loss

    def get_taxes(self, measured_result: float = None):
        measured_result = measured_result or self.get_measured_result()
        measured_loss = self.get_measured_loss()
        return self._calc_taxes(measured_result=measured_result, measured_loss=measured_loss)

    @staticmethod
    def _calc_taxes(
            measured_result: float,
            measured_loss: float
    ) -> float:
        taxes = (measured_result - min(measured_result, measured_loss)) * 0.15
        return taxes
