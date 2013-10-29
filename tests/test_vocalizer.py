import testenv
import robots
import random

# Robot
def test_kin():
    """Test if Vocalizer execute properly"""
    check = True

    robot = robots.VowelModel()

    min_c1, max_c1 = float('+inf'), float('-inf')
    min_c2, max_c2 = float('+inf'), float('-inf')

    for i in range(10000000):
        p = random.random()
        h = random.random()
        r = random.random()
        c1, c2 = robot.execute_order((p, h, r))

        min_c1 = min(min_c1, c1)
        min_c2 = min(min_c2, c2)
        max_c1 = max(max_c1, c1)
        max_c2 = max(max_c2, c2)

    print ((min_c1, max_c1), (min_c2, max_c2))

    return check

tests = [test_kin]

if __name__ == "__main__":
    print("\033[1m%s\033[0m" % (__file__,))
    for t in tests:
        print('%s %s' % ('\033[1;32mPASS\033[0m' if t() else
                         '\033[1;31mFAIL\033[0m', t.__doc__))
