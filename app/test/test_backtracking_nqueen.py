from strategies.backtracking_nqueen import BacktrackingNQueensSolver
import pytest


@pytest.mark.parametrize('test_type, n, expect', [
    ('test_quantity_solutions_8_queens', 8, 92),
    ('test_quantity_solutions_9_queens', 9, 352),
    ('test_quantity_solutions_10_queens', 10, 724),
    ('test_quantity_solutions_11_queens', 11, 2680)
])
def test_quantity_solutions_find_all_solutions(test_type, n, expect):
    print(f'Testing quantity of solutions that returns find_all_solutions: {test_type}')
    solver = BacktrackingNQueensSolver(n)
    solutions = solver.find_all_solutions()
    assert len(solutions) == expect


@pytest.mark.xfail(raises=Exception)
def test_nqueens_wrong_type():
    print('Testing BacktrackingNQueensSolver passing a character instead of integer')
    solver = BacktrackingNQueensSolver('a')
    solutions = solver.find_all_solutions()


def test_is_queen_safe_with_queen_aggression_case():
    print('Testing is_queen_safe passing invalid positions with queen aggressions')
    solver = BacktrackingNQueensSolver(8)
    test_safe = solver._is_queen_safe(3, 3, [4, 2])
    assert False == test_safe

    
def test_is_queen_safe_without_queen_aggressions():
    print('Testing is_queen_safe passing valid positions without queen aggressions')
    solver = BacktrackingNQueensSolver(8)
    test_safe = solver._is_queen_safe(3, 3, [4, 5])
    assert True == test_safe


@pytest.mark.parametrize('test_type, n, one_solution', [
    ('test_solution_exists_in_solutions_8_queens', 8, [1, 5, 8, 6, 3, 7, 2, 4]),
    ('test_solution_exists_in_solutions_9_queens', 9, [9, 6, 8, 2, 4, 1, 7, 5, 3]),
    ('test_solution_exists_in_solutions_10_queens', 10, [10, 8, 5, 2, 4, 1, 7, 9, 3, 6]),
    ('test_solution_exists_in_solutions_11_queens', 11, [11, 8, 3, 5, 2, 10, 1, 6, 4, 9, 7])
])
def test_solution_exist_in_solutions_nqueen(test_type, n, one_solution):
    print(f'Testing if solutions exists in solutions set that returns _nqueen: {test_type}')
    solver = BacktrackingNQueensSolver(n)
    solver._nqueen(1, [])
    solutions = solver._solutions_found
    assert one_solution in solutions