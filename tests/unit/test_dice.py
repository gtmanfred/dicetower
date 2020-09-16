import pytest


@pytest.mark.parametrize(
    'roll,min_val,max_val', [
        ('1d20', 1, 20),
        ('1d8 + 4', 5, 24),
        ('1d10 + 1d12', 2, 22),
        ('3dF', -3, +3),
    ],
)
async def test_roll(client, roll, min_val, max_val):
    resp = await client.get('/api/v1/dice', params={'roll': roll})

    assert resp.json()['result'] <= max_val
    assert resp.json()['result'] >= min_val
