import os


def test_path():
    path=os.path.dirname(os.path.abspath(__file__))
    print(path)

if __name__ == '__main__':
    test_path()
