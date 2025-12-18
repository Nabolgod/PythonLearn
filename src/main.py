import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.interface import Interface
from src.repositories.laptop import LaptopRepository

if __name__ == "__main__":
    obj = LaptopRepository().add()
    print(obj)

