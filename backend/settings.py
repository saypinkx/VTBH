from main import app
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8080",
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# origins = ['https://localhost:3000', 'https://localhost:8080']
# app.add_middleware(CORSMiddleware, allow_origins=[origins], allow_credentials=True, allow_methods=["*"],
#                    allow_headers=["*"])
app.add_middleware(CORSMiddleware, allow_origins=['https://localhost:8080'], allow_credentials=True,
                          allow_methods=["*"], allow_headers=["*"])
