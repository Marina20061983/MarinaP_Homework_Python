empty_dict = {}



football_stats = {
    "Число стран": 48,
    "Страна": "Катар"
    "Участники" : ["Австралия", "Англия", "Бельгия", "Аргентина", "еще 42 страны", "Эквадор", "Япония",
                   ]
}

def test_empty_dict():
    assert len(empty_dict) == 0

    def test_read_value():
        count = football_stats.get("Число стран")
        assert count == 48