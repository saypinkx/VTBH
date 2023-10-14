from main import app
from fastapi.middleware.cors import CORSMiddleware
#
# origins = [
#     "http://localhost:8080",
#     "http://31.129.101.225:8080"
# ]
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Authorization",
                   "Access-Control-Allow-Credentials"],
)

# # origins = ['https://localhost:3000', 'https://localhost:8080']
# # app.add_middleware(CORSMiddleware, allow_origins=[origins], allow_credentials=True, allow_methods=["*"],
# #                    allow_headers=["*"])
# app.add_middleware(CORSMiddleware, allow_origins=['https://localhost:8080'], allow_credentials=True,
#                           allow_methods=["*"], allow_headers=["*"])
