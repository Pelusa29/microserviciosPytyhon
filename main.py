from importlib import reload
import fastapi
from models.movie_model import MovieModel
import uvicorn
import movie_data


app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "meessage":"Hello World."
    }

@app.get('/api/movie/{title}', response_model=MovieModel)
async def movie_search(title: str):
   item = await movie_data.get_movie(title)
   
   if not item:
       raise fastapi.HTTPException(status_code=404)
   
   return item



if __name__ == "__main__":
    #uvicorn.run(app)
    uvicorn.run("main:app",host="127.0.0.1",reload=True, port=8080)