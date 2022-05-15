from enum import Enum
from app.algorithms.MinimaxSearch import MinimaxSearch
from app.algorithms.AlphaBetaPruning import AlphaBetaPruning
from app.algorithms.Quiescence import QuiescenceSearch

ALGORITHMS = {
  "minmax": MinimaxSearch(),
  "abp": AlphaBetaPruning(),
  "quiescence": QuiescenceSearch(),
}