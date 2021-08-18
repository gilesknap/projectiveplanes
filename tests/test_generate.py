from planes.projective import Projective


def test_project3():
    p = Projective(3)

    p.associate()
    all_cards = p.add_infinite_incidences()

    assert p.verify(all_cards)
