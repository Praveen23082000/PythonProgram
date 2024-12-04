from abc import ABC,abstractmethod
class Editor(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def write(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def executive(self):
        pass
class VsCode(Editor):
    def open(self):
        print("vscode open method")
    def write(self):
        print("vscode write method")
    def debug(self):
        print("vscode debug method")
    def executive(self):
        print("vscode executive")

vscode_instance=VsCode()
vscode_instance.open()