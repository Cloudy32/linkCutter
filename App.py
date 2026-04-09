from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def root():
    return {"message": "Status OK"}

@router.get('/roots')
def roots():
    return "У вас есть права админа"

@router.post('/links')
def link(new_link: str):
    links_list = []
    links_list.append(new_link)
    return links_list

