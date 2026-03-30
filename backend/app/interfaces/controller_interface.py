from abc import abstractmethod, ABC
from typing import Any

class ControllerInterface(ABC):
    
    @staticmethod
    @abstractmethod
    def get_all() -> Any:
        pass

    @staticmethod
    @abstractmethod
    def show(id: int) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def update(request: dict, id: int) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def create(request: dict) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def destroy(id: int) -> Any:
        pass
