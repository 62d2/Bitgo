from fastapi import FastAPI

app = FastAPI()


@app.post("/v1/notice")
def create_notice():
    """
    this will create new notice to the system
    :return:
    """
    return {"Hello": "World"}


@app.get("/v1/notice")
def list_notice():
    """
    This will list all the availabe notice in the sustem
    :return:
    """
    return {"Hello": "World"}


@app.delete("/v1/notice/{notice_id}")
def delete_notice(notice_id: int):
    return {"item_id": notice_id}


@app.post("/v1/notice/{notice_id}/send")
def send_email(notice_id: int):
    return {"item_id": notice_id}
