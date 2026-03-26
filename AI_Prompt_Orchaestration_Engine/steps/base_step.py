from abc import ABC, abstractmethod


class BaseStep(ABC):

    @abstractmethod
    def execute(self, step_input: str) -> str:
        pass

    @property
    @abstractmethod
    def step_name(self) -> str:
        pass