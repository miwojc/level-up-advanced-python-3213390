# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_average_race_time.ipynb.

# %% auto 0
__all__ = ['get_data', 'get_rhines_times', 'get_average']

# %% ../nbs/00_average_race_time.ipynb 3
import re
import datetime
from pathlib import Path

# %% ../nbs/00_average_race_time.ipynb 4
def get_data(path: Path | str = "../challenge/10k_racetimes.txt") -> str:
    """Return content from the file at path, default: 10k_racetimes.txt"""
    content = Path(path).read_text(encoding="utf-8")
    return content

# %% ../nbs/00_average_race_time.ipynb 5
def get_rhines_times() -> list[str]:
    """Return a list of Jennifer Rhines' race times"""
    races = get_data().split("\n")
    rhines_times = []
    for row in races[1:-1]:
        race_time, fname, lname, *_ = row.split()
        if fname == "Jennifer" and lname.startswith("Rhines"):
            rhines_times.append(race_time)
    return rhines_times

# %% ../nbs/00_average_race_time.ipynb 6
def get_average() -> str:
    """Return Jennifer Rhines' average race time in the format:
    mm:ss:M where :
    m corresponds to a minutes digit
    s corresponds to a seconds digit
    M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()
    for racetime in racetimes:
        try:
            mins, secs, ms = re.split(r"[:.]", racetime)
            total += datetime.timedelta(
                minutes=int(mins), seconds=int(secs), milliseconds=int(ms)
            )
        except ValueError:
            mins, secs = re.split(r"[:.]", racetime)
            total += datetime.timedelta(minutes=int(mins), seconds=int(secs))
    return f"{total / len(racetimes)}"[2:-5]
