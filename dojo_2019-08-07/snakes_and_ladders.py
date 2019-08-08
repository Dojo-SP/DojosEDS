def test_empty():
    assert min_rolls() == 17

def test_single_ladder_finish_81():
    assert min_rolls([2, 81]) == 5
    assert min_rolls([5, 81]) == 5
    assert min_rolls([7, 81]) == 5
    assert min_rolls([8, 81]) == 6
    assert min_rolls([9, 81]) == 6
    assert min_rolls([13, 81]) == 6
    assert min_rolls([14, 81]) == 7
    assert min_rolls([19, 81]) == 7
    assert min_rolls([20, 81]) == 8
    assert min_rolls([25, 81]) == 8
    assert min_rolls([26, 81]) == 9
    assert min_rolls([80, 81]) == 17

def test_single_ladder_finish_87():
    assert min_rolls([2, 87]) == 4
    assert min_rolls([5, 87]) == 4
    assert min_rolls([7, 87]) == 4
    assert min_rolls([8, 87]) == 5
    assert min_rolls([9, 87]) == 5
    assert min_rolls([13, 87]) == 5
    assert min_rolls([14, 87]) == 6
    assert min_rolls([19, 87]) == 6
    assert min_rolls([20, 87]) == 7
    assert min_rolls([25, 87]) == 7
    assert min_rolls([26, 87]) == 8
    assert min_rolls([86, 87]) == 17

def test_single_ladder_finish_88():
    assert min_rolls([2, 88]) == 3
    assert min_rolls([5, 88]) == 3
    assert min_rolls([7, 88]) == 3
    assert min_rolls([8, 88]) == 4
    assert min_rolls([9, 88]) == 4
    assert min_rolls([13, 88]) == 4
    assert min_rolls([14, 88]) == 5
    assert min_rolls([19, 88]) == 5
    assert min_rolls([20, 88]) == 6
    assert min_rolls([25, 88]) == 6
    assert min_rolls([26, 88]) == 7
    assert min_rolls([87, 88]) == 17

def test_single_ladder_finish_92():
    assert min_rolls([91, 92]) == 17

def test_single_ladder_finish_93():
    assert min_rolls([2, 93]) == 3
    assert min_rolls([5, 93]) == 3
    assert min_rolls([7, 93]) == 3
    assert min_rolls([8, 93]) == 4
    assert min_rolls([9, 93]) == 4
    assert min_rolls([13, 93]) == 4
    assert min_rolls([14, 93]) == 5
    assert min_rolls([19, 93]) == 5
    assert min_rolls([20, 93]) == 6
    assert min_rolls([25, 93]) == 6
    assert min_rolls([26, 93]) == 7
    assert min_rolls([91, 93]) == 17
    assert min_rolls([92, 93]) == 17

def test_single_ladder_finish_94():
    assert min_rolls([2, 94]) == 2
    assert min_rolls([5, 94]) == 2
    assert min_rolls([7, 94]) == 2
    assert min_rolls([8, 94]) == 3
    assert min_rolls([9, 94]) == 3
    assert min_rolls([13, 94]) == 3
    assert min_rolls([14, 94]) == 4
    assert min_rolls([19, 94]) == 4
    assert min_rolls([20, 94]) == 5
    assert min_rolls([25, 94]) == 5
    assert min_rolls([26, 94]) == 6
    assert min_rolls([91, 94]) == 16
    assert min_rolls([92, 94]) == 17
    assert min_rolls([93, 94]) == 17

def test_single_ladder_finish_95():
    assert min_rolls([2, 95]) == 2
    assert min_rolls([5, 95]) == 2
    assert min_rolls([7, 95]) == 2
    assert min_rolls([8, 95]) == 3
    assert min_rolls([9, 95]) == 3
    assert min_rolls([13, 95]) == 3
    assert min_rolls([14, 95]) == 4
    assert min_rolls([19, 95]) == 4
    assert min_rolls([20, 95]) == 5
    assert min_rolls([25, 95]) == 5
    assert min_rolls([26, 95]) == 6
    assert min_rolls([91, 95]) == 16
    assert min_rolls([92, 95]) == 17
    assert min_rolls([94, 95]) == 17

def test_single_ladder_finish_99():
    assert min_rolls([2, 99]) == 2
    assert min_rolls([5, 99]) == 2
    assert min_rolls([7, 99]) == 2
    assert min_rolls([8, 99]) == 3
    assert min_rolls([9, 99]) == 3
    assert min_rolls([13, 99]) == 3
    assert min_rolls([14, 99]) == 4
    assert min_rolls([19, 99]) == 4
    assert min_rolls([20, 99]) == 5
    assert min_rolls([25, 99]) == 5
    assert min_rolls([26, 99]) == 6
    assert min_rolls([91, 99]) == 16
    assert min_rolls([92, 99]) == 17
    assert min_rolls([97, 99]) == 17
    assert min_rolls([98, 99]) == 17

def test_one_step():
    assert min_rolls([2, 100]) == 1

def test_single_ladder_finish_in_100():
    assert min_rolls([5, 100]) == 1
    assert min_rolls([6, 100]) == 1
    assert min_rolls([7, 100]) == 1
    assert min_rolls([8, 100]) == 2
    assert min_rolls([9, 100]) == 2
    assert min_rolls([13, 100]) == 2
    assert min_rolls([14, 100]) == 3
    assert min_rolls([19, 100]) == 3
    assert min_rolls([20, 100]) == 4
    assert min_rolls([25, 100]) == 4
    assert min_rolls([26, 100]) == 5
    assert min_rolls([99, 100]) == 17

def min_rolls(*ladders):
    if not ladders:
        return 17
    ladder = ladders[0]
    return min(((ladder[0] - 2) // 6) + 
               (100 - ladder[1] + 5) // 6 + 1 , 17)
