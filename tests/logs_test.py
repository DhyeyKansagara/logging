import os

def test_info_log():
    assert os.path.exists('./app/logs/info.log') == True

def test_debug_log():
    assert os.path.exists('./app/logs/debug.log') == True
