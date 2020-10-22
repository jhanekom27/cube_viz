from pandas import DataFrame, Series
from dataclasses import dataclass


MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


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
    solve_date_time: Series
    time_sec: Series


@dataclass
class CVEnhanced(DataFrame):
    solve_num: Series
    solve_date_time: Series
    solve_date: Series
    time_sec: Series
    best_time: Series
    best_time_is_diff: Series


@dataclass
class CVGroupedDaily(DataFrame):
    solve_date: Series
    num_solves: Series
    time_sec_mean: Series
    time_sec_std: Series
    year: Series
    month: Series
    day: Series
