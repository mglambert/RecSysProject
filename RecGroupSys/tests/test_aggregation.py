import pytest
import pandas as pd
from RecGroupSys import VotingMethods

@pytest.fixture
def sample_data() -> pd.DataFrame:
    """
    Crea un DataFrame con los datos de la Tabla 1.
    """
    data = {
        'A': [10, 1, 10], 'B': [4, 9, 5], 'C': [3, 8, 2],
        'D': [6, 9, 7], 'E': [10, 7, 8], 'F': [9, 9, 8],
        'G': [6, 6, 5], 'H': [8, 9, 6], 'I': [10, 3, 7],
        'J': [8, 8, 6]
    }
    users = ['Pedro', 'Juan', 'Diego']
    return pd.DataFrame(data, index=users)

def test_plurality_voting(sample_data):
    winner = VotingMethods.plurality_voting(sample_data)
    assert winner == 'A'

def test_average(sample_data):
    result = VotingMethods.average(sample_data)
    assert result['B'] == 6.0

def test_multiplicative(sample_data):
    result = VotingMethods.multiplicative(sample_data)
    assert result['B'] == 180

def test_borda_count(sample_data):
    result = VotingMethods.borda_count(sample_data)
    assert result['A'] == 17.0

def test_copeland_score(sample_data):
    result = VotingMethods.copeland_score(sample_data)
    assert result['F'] == 5

def test_approval_voting(sample_data):
    threshold = 6
    result = VotingMethods.approval_voting(sample_data, threshold)
    assert result['B'] == 1
    assert result['F'] == 3

def test_least_misery(sample_data):
    result = VotingMethods.least_misery(sample_data)
    assert result['B'] == 4

def test_most_pleasure(sample_data):
    result = VotingMethods.most_pleasure(sample_data)
    assert result['B'] == 9

def test_average_without_misery(sample_data):
    threshold = 4
    result = VotingMethods.average_without_misery(sample_data, threshold)
    assert 'A' not in result.index
    assert 'C' not in result.index
    assert pytest.approx(result['J'], 0.01) == 7.33

def test_fairness(sample_data):
    user_order = ['Pedro', 'Juan', 'Diego']
    # La salida determinista con la regla de desempate (primer ítem)
    expected_order = ['A', 'B', 'E', 'I', 'D', 'F', 'H', 'C', 'J', 'G']
    result = VotingMethods.fairness(sample_data, user_order)
    assert result == expected_order

def test_most_respected_person(sample_data):
    juan_result = VotingMethods.most_respected_person(sample_data, 'Juan')
    diego_result = VotingMethods.most_respected_person(sample_data, 'Diego')
    assert juan_result['A'] == 1
    assert diego_result['A'] == 10