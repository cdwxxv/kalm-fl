import pytest

from kalmfl.multistanza.tests import *

from kalmfl.multistanza.models.ner import trainer

pytestmark = [pytest.mark.travis, pytest.mark.pipeline]

def test_fix_singleton_tags():
    TESTS = [
        (["O"], ["O"]),
        (["B-PER"], ["S-PER"]),
        (["B-PER", "I-PER"], ["B-PER", "I-PER"]),
        (["B-PER", "O", "B-PER"], ["S-PER", "O", "S-PER"]),
        (["B-PER", "B-PER", "I-PER"], ["S-PER", "B-PER", "I-PER"]),
        (["B-PER", "I-PER", "O", "B-PER"], ["B-PER", "I-PER", "O", "S-PER"]),
        (["B-PER", "B-PER", "I-PER", "B-PER"], ["S-PER", "B-PER", "I-PER", "S-PER"]),
        (["B-PER", "I-ORG", "O", "B-PER"], ["S-PER", "I-ORG", "O", "S-PER"]),
        (["B-PER", "I-PER", "E-PER", "O", "B-PER", "E-PER"], ["B-PER", "I-PER", "E-PER", "O", "B-PER", "E-PER"]),
        (["S-PER", "B-PER", "E-PER"], ["S-PER", "B-PER", "E-PER"]),
    ]
             
    for unfixed, expected in TESTS:
        assert trainer.fix_singleton_tags(unfixed) == expected
