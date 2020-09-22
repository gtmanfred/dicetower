import fastapi
import pydantic
from dicetray import Dicetray

router = fastapi.APIRouter()


class RollResult(pydantic.BaseModel):
    result: int


@router.get("/dice", response_model=RollResult, tags=["dice"], name="roll")
async def roll_a_dice(roll: str = fastapi.Query("1d20")):
    return {"result": Dicetray(roll).roll()}
