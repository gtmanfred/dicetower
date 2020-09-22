import fastapi
import pydantic
import typing
from dicetray import Dicetray

router = fastapi.APIRouter()


class Dice(pydantic.BaseModel):
    result: int
    sides: typing.Union[int, str]


class RollResult(pydantic.BaseModel):
    result: int
    dice: typing.List[Dice]


@router.get("/dice", response_model=RollResult, tags=["dice"], name="roll")
async def roll_a_dice(roll: str = fastapi.Query("1d20")):
    tray = Dicetray(roll)
    tray.roll()
    return {"result": tray.result, "dice": [dice.__dict__() for dice in tray.dice]}
