from task import Task
from read_data import ReadData
from gui import Gui

task = Task("test.json")


def test_2a():
    x, y = task.task_2_a("1-1")
    countries = ['ES', 'MX', 'CR']
    for i, j in enumerate(x):
        assert j == countries[i]
    viewers = [3, 1, 1]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_2a_wrong_doc():
    result, param2 = task.task_2_a("1-13")
    assert result is False


def test_2a_wrong_file():
    task = Task("test")
    result, param2 = task.task_2_a("1-13")
    assert result is False


def test_2a_single_item():
    x, y = task.task_2_a("4-4")
    countries = ['ES']
    for i, j in enumerate(x):
        assert j == countries[i]
    viewers = [1]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_2a_different_doc():
    x, y = task.task_2_a("2-2")
    countries = ['ES']
    for i, j in enumerate(x):
        assert j == countries[i]
    viewers = [5]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_2b():
    x, y = task.task_2_b("1-1")
    continents = ['Europe', 'North America']
    viewers = [3, 2]
    for i, j in enumerate(x):
        assert j == continents[i]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_2b_wrong_doc():
    result, param2 = task.task_2_b("1-3")
    assert result is False


def test_2b_wrong_file():
    task = Task("test")
    result, param2 = task.task_2_b("1-3")
    assert result is False


def test_2b_single_doc():
    x, y = task.task_2_b("3-3")
    continents = ['Europe']
    viewers = [2]
    for i, j in enumerate(x):
        assert j == continents[i]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_2b_different_doc():
    x, y = task.task_2_b("2-2")
    continents = ['Europe']
    viewers = [5]
    for i, j in enumerate(x):
        assert j == continents[i]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_3a():
    x, y = task.task_3_a()
    browsers = ['Chrome', 'Opera', 'Firefox', 'IE', 'Amazon Silk']
    views = [5, 1, 1, 1, 5]
    for i, j in enumerate(x):
        assert j == browsers[i]
    for i, j in enumerate(y):
        assert j == views[i]


def test_3a_wrong_file():
    task = Task("test")
    x, y = task.task_3_a()
    assert x is False


def test_3b():
    task = Task("test.json")
    x, y = task.task_3_b()
    browsers = ['Chrome', 'Opera', 'Firefox', 'IE', 'Other']
    views = [5, 1, 1, 1, 3]
    for i, j in enumerate(x):
        assert j == browsers[i]
    for i, j in enumerate(y):
        assert j == views[i]


def test_3b_wrong_file():
    task = Task("test")
    x, y = task.task_3_b()
    assert x is False


def test_4():
    x, y = task.task_4()
    user_ids = ['8a', '3a', '10a', '1a', '6a', '5a', '4a', '7a', '2a', '9a']
    readtimes = [999, 932, 713, 580, 555, 535, 364, 258, 147, 128]
    for i, j in enumerate(x):
        assert j == user_ids[i]
    for i, j in enumerate(y):
        assert j == readtimes[i]


def test_4_wrong_file():
    task = Task("test")
    x, y = task.task_4()
    assert x is False


def test_5d():
    x, y, z = task.task_5_d("1-1", "1a")
    docs = ['1-1', '3-3']
    viewers = [5, 2]
    for i, j in enumerate(x):
        assert j == docs[i]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_5d_no_visitor_id():
    x, y, z = task.task_5_d("1-1")
    docs = ['1-1', '3-3']
    viewers = [5, 2]
    for i, j in enumerate(x):
        assert j == docs[i]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_5d_different_doc_id():
    x, y, z = task.task_5_d("2-2")
    docs = ['2-2', '3-3']
    viewers = [5, 2]
    for i, j in enumerate(x):
        assert j == docs[i]
    for i, j in enumerate(y):
        assert j == viewers[i]


def test_5d_incorrect_doc_id():
    x, y = task.task_5_d("2-5")
    assert x is False


def test_5d_check_visitor_has_not_read_doc():
    x, y, z = task.task_5_d("1-1", "10a")
    assert z is False


def test_5d_check_visitor_has_read_doc():
    x, y, z = task.task_5_d("1-1", "1a")
    assert z is True


def test_6_check_has_read_true():
    x, y = task.task_6("1-1", "1a")
    assert y is True


def test_6_check_has_read_false():
    x, y = task.task_6("1-1", "11a")
    assert y is False
