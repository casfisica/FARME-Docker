from fastapi import FastAPI
#To include the new routes from the folder routes
#from routers.users import user
from r

app = FastAPI()
#Then include into the app
app.include_router(user)

@app.get("/")
def read_root():
	return {"Hello":"World"}
