from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences(path='data/jobs.csv', word='python') == 1639
    # pass
