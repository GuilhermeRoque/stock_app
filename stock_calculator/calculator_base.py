import abc


class CalculatorInterface(abc.ABC):
    @abc.abstractmethod
    def get_average_price(self):
        pass

    @abc.abstractmethod
    def get_average_purchase_amount(self) -> int:
        pass

    @abc.abstractmethod
    def get_measured_result(self, average_price: float = None):
        pass

    @abc.abstractmethod
    def get_measured_loss(self):
        pass

    @abc.abstractmethod
    def get_taxes(self):
        pass
