from pathlib import Path

class Constants:
    root_dir = Path(__file__).resolve().parent.parent

constant: Constants = Constants()