from fastapi import FastAPI
from config.database import db
from router import api
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
def startup():
    if db.is_closed():
        db.connect()


@app.on_event('shutdown')
def startup():
    if not db.is_closed():
        db.close()


@app.get("/", response_class=HTMLResponse)
async def read_items():
    print('test')
    return """
    <html>
        <head>
            <meta name="zalo-platform-site-verification" content="EDZbEFZNSM87t_PktCrWULxXiN2ods4kCZW" />
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


@app.post('/')
def post_test():
    return 'ok'


app.include_router(api.router)




