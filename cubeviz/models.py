from pandas import DataFrame, Series
from dataclasses import dataclass


@dataclass
class TimiksData(DataFrame):
    id: Series
    ms: Series
    data: Series
    puzzle: Series
    scramble: Series
    plus2: Series
    dnf: Series


@dataclass
class CVBase(DataFrame):
    solve_date: Series
    time_sec: Series


@dataclass
class CVEnhanced(DataFrame):
    solve_num: Series
    solve_date: Series
    time_sec: Series
    best_time: Series
    best_time_is_diff: Series
