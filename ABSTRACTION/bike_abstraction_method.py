from abc import ABC,abstractmethod
class Bike(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def acceleration(self):
        pass

    @acceleration
    def stop(self):
        pass

class Dominar(Bike):
    def start(self):
        print("dominar start method")

    def acceleration(self):
        print("dominar acceleration method")

    def stop(self):
        print("dominar stop method")

dominar_instance=Dominar()
dominar_instance.start()
dominar_instance.stop()
