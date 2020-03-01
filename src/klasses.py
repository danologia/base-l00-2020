"""Tasks for checking knowledge about classes."""
from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    """Checks if student can use ABC package.

    Using the ABC package mark this class and its `process` function
    to be abstract.
    """

    def __init__(self):
        """Inits BaseClass."""
        self._num_processed = 0

    @abstractmethod
    def process(self, item: int) -> int:
        """Maps each given integer value to a new integer value."""
        pass

    def num_processed(self) -> int:
        """Retrieved the number of processed items."""
        return self._num_processed


class MultiplyingProcessor(BaseProcessor):
    """Checks if the student can use inheritance.

    Modify this class to inherit from the `BaseProcessor` class.
    Implement the `process` function to it multiplies each item by `a` and
    it increments the number of processed items.
    Override `num_processed` method from base class and if the are no
    processed items yet, then print following message: 'NO ITEMS PROCESSED',
    then call the base class implementation for this method.
    """

    def __init__(self, a):
        """Inits MultiplyingProcessor."""
        super().__init__()
        self._a = a

    def process(self, item: int) -> int:
        """Return item multiplied by `a`.

        Multiplies item by internal parameter `a` and keeps count
        of number of times it was called
        """
        self._num_processed = self._num_processed + 1

        return item * self._a

    def num_processed(self) -> int:
        """Return how many times process was called."""
        if self._num_processed == 0:
            print("NO ITEMS PROCESSED")

        return super().num_processed()
