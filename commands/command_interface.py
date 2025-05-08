"""
Command Interface module defining the base Command abstract class
"""
from abc import ABC, abstractmethod
from typing import List, Any, Dict

class Command(ABC):
    """
    Abstract base class for command pattern implementation.
    All calculator commands must inherit from this class.
    """
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the command with given arguments
        Must be implemented by all command subclasses
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Return a description of what the command does
        Must be implemented by all command subclasses
        """
        pass

    @property
    @abstractmethod
    def usage(self) -> str:
        """
        Return usage information on how to use the command
        Must be implemented by all command subclasses
        """
        pass
