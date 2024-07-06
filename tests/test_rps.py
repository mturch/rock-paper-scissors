import pytest
from .code.rock_paper_scissors.rps import get_user_input

def test_get_user_input_valid_lower_r(mocker):
	mocker.patch('builtins.input', return_value='r')
	assert get_user_input() == 'R'

def test_get_user_input_valid_upper_p(mocker):
	mocker.patch('builtins.input', return_value='P')
	assert get_user_input() == 'P'

def test_get_user_input_valid_lower_s(mocker):
	mocker.patch('builtins.input', return_value='s')
	assert get_user_input() == 'S'

def test_get_user_input_invalid(mocker):
	mocker.patch('builtins.input', return_value='x')
	with pytest.raises(SystemExit):
		get_user_input()

def test_get_user_input_case_sensitivity(mocker):
	mocker.patch('builtins.input', return_value='p')
	assert get_user_input() == 'P'