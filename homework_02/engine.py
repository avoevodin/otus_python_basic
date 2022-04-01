"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    """
    Describes an engine entity.
    """
    volume: float
    pistons: int = 4
