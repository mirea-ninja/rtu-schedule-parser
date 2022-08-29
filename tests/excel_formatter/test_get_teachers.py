

def test_get_teacher_0(excel_formatter):
    result = excel_formatter.get_teachers("Козлова Г.Г.\nИсаев Р.А.")
    correct_result = ["Козлова Г.Г.", "Исаев Р.А."]
    assert result == correct_result


def test_get_teacher_1(excel_formatter):
    result = excel_formatter.get_teachers("Шеверева Е.А., Богатырев С.И.")
    correct_result = ["Шеверева Е.А.", "Богатырев С.И."]
    assert result == correct_result


def test_get_teacher_2(excel_formatter):
    result = excel_formatter.get_teachers(
        "Симонов М.А. Симонов М.А. Симонов М.А. Жлуткова"
    )
    correct_result = ["Симонов М.А.", "Симонов М.А.", "Симонов М.А.", "Жлуткова"]
    assert result == correct_result


def test_get_teacher_3(excel_formatter):
    result = excel_formatter.get_teachers("Симонов М.А. Жлуткова И.В.")
    correct_result = ["Симонов М.А.", "Жлуткова И.В."]
    assert result == correct_result


def test_get_teacher_4(excel_formatter):
    result = excel_formatter.get_teachers("Симонов М.А. . Жлуткова И.В.")
    correct_result = ["Симонов М.А.", "Жлуткова И.В."]
    assert result == correct_result


def test_get_teacher_5(excel_formatter):
    result = excel_formatter.get_teachers("Эйстрих-Геллер В.Ю.")
    correct_result = ["Эйстрих-Геллер В.Ю."]
    assert result == correct_result


def test_get_teacher_6(excel_formatter):
    result = excel_formatter.get_teachers("Рогачев")
    correct_result = ["Рогачев"]
    assert result == correct_result


def test_get_teacher_7(excel_formatter):
    result = excel_formatter.get_teachers("Рогачев Горелик")
    correct_result = ["Рогачев", "Горелик"]
    assert result == correct_result

def test_get_teacher_8(excel_formatter):
    result = excel_formatter.get_teachers("Новосёлова Е.В.")
    correct_result = ["Новосёлова Е.В."]
    assert result == correct_result


def test_get_teacher_9(excel_formatter):
    result = excel_formatter.get_teachers("Новосёлова Е.В.\nКомарова М,И.")
    correct_result = ["Новосёлова Е.В.", "Комарова М.И."]
    assert result == correct_result


def test_get_teacher_10(excel_formatter):
    result = excel_formatter.get_teachers("Беглов И.А., Верещагина Т.А.")
    correct_result = ["Беглов И.А.", "Верещагина Т.А."]
    assert result == correct_result
