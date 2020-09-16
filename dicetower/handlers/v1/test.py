import fastapi

router = fastapi.APIRouter()


@router.get('/ping')
async def get_ping():
    return {'message': 'success'}
