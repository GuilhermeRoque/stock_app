from stock_calculator.stock_transactions import StockTransactionsDataFrame


class StockCalculatorSimple:
    def __init__(self, df_stock: StockTransactionsDataFrame):
        self.df_stock = df_stock

    def get_average_price(self) -> float:
        df_stock = self.df_stock.filter_purchase_operations()
        price = df_stock.get_price()
        amount = df_stock.get_amount()
        brokerage_fee = df_stock.get_fee()

        average_price = 0
        average_amount = 0
        for i in range(0, len(price)):
            average_price = self._calc_average_price(
                price=price[i],
                amount=amount[i],
                brokerage_fee=brokerage_fee[i],
                average_price=average_price,
                average_amount=average_amount
            )
            average_amount = self._calc_average_purchase_amount(
                amount=amount[i],
                average_amount=average_amount
            )
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

    def get_average_purchase_amount(self) -> int:
        df_stock = self.df_stock.filter_purchase_operations()
        amount = df_stock.get_amount()
        average_amount = 0
        for i in amount:
            average_amount = self._calc_average_purchase_amount(amount=i, average_amount=average_amount)
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

    def get_measured_result(self, average_price: float = None) -> float:
        average_price = average_price or self.get_average_price()
        measured_result_list = []
        df_stock = self.df_stock.filter_sales_operations()
        price = df_stock.get_price()
        amount = df_stock.get_amount()
        fee = df_stock.get_fee()
        for i in range(0, len(price)):
            measured_result = self._calc_measured_result(
                price=price[i],
                average_price=average_price,
                amount=amount[i],
                fee=fee[i]
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

    def get_taxes(self):
        measured_result = self.get_measured_result()
        measured_loss = self.get_measured_loss()
        return self._calc_taxes(measured_result=measured_result, measured_loss=measured_loss)

    @staticmethod
    def _calc_taxes(
            measured_result: float,
            measured_loss: float
    ) -> float:
        taxes = (measured_result - min(measured_result, measured_loss)) * 0.15
        return taxes
