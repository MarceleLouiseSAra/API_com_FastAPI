from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # end point
def read_root():
    return {'message': 'busquem conhecimento'}
