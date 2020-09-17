import fastapi
import python_dice as dice
import pydantic

router = fastapi.APIRouter()
interp = dice.PythonDiceInterpreter()


class RollResult(pydantic.BaseModel):
    result: int


@router.get('/dice', response_model=RollResult, tags=['dice'], name='roll')
async def roll_a_dice(roll: str = fastapi.Query('1d20')):
    return {'result': interp.roll([roll])['stdout']}
