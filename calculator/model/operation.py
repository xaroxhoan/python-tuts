from abc import abstractmethod


class IOperation:

    @abstractmethod
    def operate(self) -> str:
        pass