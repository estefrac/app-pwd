from abc import abstractmethod, ABC

class ControllerInterface(ABC):
    
    @staticmethod
    @abstractmethod
    def get_all():
        pass

    @staticmethod
    @abstractmethod
    def show(id:int):
        pass

    @staticmethod
    @abstractmethod
    def update(request:dict, id:int):
        pass

    @staticmethod
    @abstractmethod
    def create(request:dict):
        pass

    @staticmethod
    @abstractmethod
    def destroy(id:int):
        pass
