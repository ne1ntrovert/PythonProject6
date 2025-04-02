import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "acc, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("9876543210123456", "9876 54** **** 3456"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("4000111122223333", "4000 11** **** 3333")
    ],
)
def test_get_mask_card_number(acc: str, expected: str) -> None:
    assert get_mask_card_number(acc) == expected


@pytest.mark.parametrize(
    "acc1, expected1",
    [
        ("1234567890123456", "**3456"),
        ("987654321", "**4321"),
        ("11112222", "**2222"),
        ("4000", "**4000")
    ],
)
def test_get_mask_account(acc1: str, expected1: str) -> None:
    assert get_mask_account(acc1) == expected1
