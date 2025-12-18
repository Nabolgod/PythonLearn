import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.laboratory_3.interface import Interface
from src.laboratory_3.repositories.laptop import LaptopRepository


def start_laboratory_3():
    interface = Interface(LaptopRepository())
    interface.start()


if __name__ == "__main__":
    start_laboratory_3()
