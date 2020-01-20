"""Provides participant API"""

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from numpy import ndarray


class Participant(ABC):
    """An abstract participant for federated learning."""

    @abstractmethod
    def train_round(
        self, weights: List[ndarray], epochs: int, epoch_base: int
    ) -> Tuple[List[ndarray], int, Dict[str, ndarray]]:
        """Train a model in a federated learning round.

        Either a model is given in terms of its weights or the weights have to be initialized by the
        participant. Then the model is trained on the participant's dataset for a number of epochs.
        The weights of the updated model are returned in combination with the number of samples of
        the train dataset and some gathered metrics.

        Args:
            weights (~typing.List[~numpy.ndarray]): The weights of the model to be trained.
            epochs (int): The number of epochs to be trained.
            epoch_base (int): The epoch base number for the optimizer state (in case of epoch
                dependent optimizer parameters).

        Returns:
            ~typing.Tuple[~typing.List[~numpy.ndarray], int, ~typing.Dict[str, ~numpy.ndarray]]: The
                updated model weights, the number of training samples and the gathered metrics.
        """
