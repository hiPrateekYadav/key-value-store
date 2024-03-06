from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.responses import JSONResponse
from tasks import add_to_store, remove_from_store
from utils import getData, writeData

app = FastAPI()

def get_key_value_store():
    key_value_store = getData()
    if not key_value_store:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return key_value_store

@app.get("/get/{key}", response_class=JSONResponse)
async def get_value(key: str, key_value_store: dict = Depends(get_key_value_store)):
    value = key_value_store.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

@app.post("/set", response_class=JSONResponse)
async def set_value(key: str = Body(...), value: str = Body(...), key_value_store: dict = Depends(get_key_value_store)):
    try:
        add_to_store(key, value)
        return {"message": "Setting value in progress", "key": key, "value": value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.delete("/delete/{key}", response_class=JSONResponse)
async def delete_value(key: str, key_value_store: dict = Depends(get_key_value_store)):
    try:
        remove_from_store(key)
        return {"message": "Deletion in progress", "key": key}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
