import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.interface import Interface

if __name__ == "__main__":
    interface = Interface()
    interface.start()
